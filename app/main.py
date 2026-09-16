from app.api.routes.job_routes import router as job_router
from fastapi import FastAPI
from app.api.routes.resume_routes import router as resume_router

app = FastAPI(
    title="AI HR Resume Screening System",
    description="AI-powered resume screening and candidate ranking API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI HR Resume Screening System"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(resume_router)
app.include_router(job_router)