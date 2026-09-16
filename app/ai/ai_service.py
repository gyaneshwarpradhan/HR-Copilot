# app/ai/ai_service.py

def generate_candidate_summary(candidate):
    name = candidate.get("name") or "The candidate"
    skills = candidate.get("skills", [])

    if skills:
        skill_text = ", ".join(skills)
        return (
            f"{name} has a technical background with experience or knowledge "
            f"in {skill_text}."
        )

    return f"{name} has submitted a resume, but no recognized technical skills were found."


def analyze_candidate(candidate, screening_result):
    summary = generate_candidate_summary(candidate)

    return {
        "candidate_summary": summary,
        "matched_skills": screening_result["matched_skills"],
        "missing_skills": screening_result["missing_skills"],
        "match_score": screening_result["match_score"],
        "recommendation_reason": (
            f"The candidate matches "
            f"{screening_result['match_score']}% of the required skills."
        )
    }