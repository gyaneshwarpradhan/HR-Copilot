from fastapi import APIRouter, UploadFile, File
from pathlib import Path

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    file_content = await file.read()

    with open(file_path, "wb") as saved_file:
        saved_file.write(file_content)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "saved_path": str(file_path)
    }