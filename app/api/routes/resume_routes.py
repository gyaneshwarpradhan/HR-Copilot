from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

from app.services.resume_service import extract_resume_text
from app.services.resume_parser import parse_resume


router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    allowed_extensions = [".pdf", ".docx"]
    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported."
        )

    file_path = UPLOAD_DIR / file.filename

    file_content = await file.read()

    with open(file_path, "wb") as saved_file:
        saved_file.write(file_content)

    try:
        resume_text = extract_resume_text(str(file_path))
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Could not extract resume text: {str(error)}"
        )

    parsed_data = parse_resume(resume_text)

    return {
        "message": "Resume uploaded and processed successfully",
        "filename": file.filename,
        "text": resume_text,
        "candidate": parsed_data
    }