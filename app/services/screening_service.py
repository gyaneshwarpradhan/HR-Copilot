def calculate_match_score(candidate_skills, required_skills):
    """
    Calculate how many required skills
    are present in the candidate's skills.
    """

    candidate_skills = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    required_skills = {
        skill.lower().strip()
        for skill in required_skills
    }

    if not required_skills:
        return 0

    matched_skills = candidate_skills.intersection(required_skills)

    score = (len(matched_skills) / len(required_skills)) * 100

    return round(score, 2)


def find_missing_skills(candidate_skills, required_skills):
    """
    Find skills required by the job
    but missing from the candidate's resume.
    """

    candidate_skills = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    missing_skills = [
        skill
        for skill in required_skills
        if skill.lower().strip() not in candidate_skills
    ]

    return missing_skills


def screen_candidate(candidate_skills, required_skills):
    """
    Perform complete candidate screening.
    """

    candidate_skills = list(candidate_skills)
    required_skills = list(required_skills)

    matched_skills = [
        skill
        for skill in required_skills
        if skill.lower().strip() in {
            candidate.lower().strip()
            for candidate in candidate_skills
        }
    ]

    missing_skills = find_missing_skills(
        candidate_skills,
        required_skills
    )

    score = calculate_match_score(
        candidate_skills,
        required_skills
    )

    return {
        "match_score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }