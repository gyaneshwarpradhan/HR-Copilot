from app.ai.ai_service import analyze_candidate


candidate = {
    "name": "Rahul Kumar",
    "email": "rahul@gmail.com",
    "phone": "9876543210",
    "skills": [
        "Python",
        "SQL",
        "FastAPI",
        "Git"
    ]
}

screening_result = {
    "match_score": 80,
    "matched_skills": [
        "Python",
        "SQL",
        "FastAPI",
        "Git"
    ],
    "missing_skills": [
        "MongoDB"
    ]
}

result = analyze_candidate(
    candidate,
    screening_result
)

print(result)