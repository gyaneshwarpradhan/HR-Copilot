import re


def extract_email(text: str):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return None


def extract_phone(text: str):
    pattern = r'(?:\+91[\s-]?)?[6-9]\d{9}'
    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return None


def extract_name(text: str):
    lines = text.strip().split("\n")

    for line in lines[:5]:
        line = line.strip()

        if line and len(line.split()) <= 4:
            if not any(char.isdigit() for char in line):
                if "@" not in line:
                    return line

    return None


def extract_skills(text: str):
    common_skills = [
        "Python",
        "Java",
        "JavaScript",
        "React",
        "Node.js",
        "FastAPI",
        "Django",
        "Flask",
        "SQL",
        "MySQL",
        "MongoDB",
        "HTML",
        "CSS",
        "Git",
        "GitHub",
        "Machine Learning",
        "Artificial Intelligence",
        "Excel",
        "Power BI",
        "AWS"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in common_skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def parse_resume(text: str):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }