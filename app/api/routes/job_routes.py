from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pathlib import Path

from app.services.resume_service import extract_resume_text
from app.services.resume_parser import parse_resume
from app.services.screening_service import screen_candidate
from app.ai.ai_service import analyze_candidate


router = APIRouter(
    prefix="/job",
    tags=["Job"]
)


class JobDescription(BaseModel):
    title: str
    required_skills: list[str]


class ResumeScreenRequest(BaseModel):
    filename: str


@router.post("/screen-resume")
def screen_uploaded_resume(
    job: JobDescription,
    resume: ResumeScreenRequest
):
    # 1. Find uploaded resume
    file_path = Path("uploads") / Path(resume.filename).name

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Resume not found. Please upload the resume first."
        )

    # 2. Extract resume text
    try:
        resume_text = extract_resume_text(str(file_path))
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Could not extract resume text: {str(error)}"
        )

    # 3. Parse candidate information
    candidate = parse_resume(resume_text)

    # 4. Match candidate skills with job requirements
    screening_result = screen_candidate(
        candidate["skills"],
        job.required_skills
    )

    # 5. Generate AI analysis
    ai_analysis = analyze_candidate(
        candidate,
        screening_result
    )

    # 6. Return complete result
    return {
        "job_title": job.title,
        "resume": resume.filename,
        "candidate": candidate,
        "screening_result": screening_result,
        "ai_analysis": ai_analysis
    }