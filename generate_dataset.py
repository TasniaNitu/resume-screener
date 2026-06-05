import pandas as pd
import random

jobs = {
    "AI Engineer": [
        "Python", "Machine Learning", "Deep Learning",
        "PyTorch", "Transformers", "NLP"
    ],

    "Data Scientist": [
        "Python", "Pandas", "NumPy",
        "Statistics", "Machine Learning", "SQL"
    ],

    "Machine Learning Engineer": [
        "Python", "TensorFlow",
        "Machine Learning", "MLOps", "Docker"
    ],

    "Backend Developer": [
        "Python", "FastAPI",
        "Docker", "SQL", "Git"
    ],

    "Data Analyst": [
        "Excel", "Power BI",
        "SQL", "Python", "Pandas"
    ]
}

rows = []

for job, skills in jobs.items():

    for scenario in range(40):

        good_resume = " ".join(skills)

        rows.append({
            "job_description": f"Looking for a {job} with experience in {' '.join(skills)}",
            "resume_name": f"{job}_GOOD_{scenario}",
            "resume_text": good_resume,
            "relevant": 1
        })

        other_jobs = [j for j in jobs if j != job]

        hard_negative_job = random.choice(other_jobs)

        hard_negative_resume = " ".join(
            jobs[hard_negative_job]
        )

        rows.append({
            "job_description": f"Looking for a {job} with experience in {' '.join(skills)}",
            "resume_name": f"{hard_negative_job}_HARD_NEGATIVE_{scenario}",
            "resume_text": hard_negative_resume,
            "relevant": 0
        })

        soft_negative = random.sample([
            "Marketing",
            "Sales",
            "Accounting",
            "Finance",
            "Teaching",
            "Customer Service",
            "Photography"
        ], 3)

        rows.append({
            "job_description": f"Looking for a {job} with experience in {' '.join(skills)}",
            "resume_name": f"SOFT_NEGATIVE_{scenario}",
            "resume_text": " ".join(soft_negative),
            "relevant": 0
        })

df = pd.DataFrame(rows)

df.to_csv(
    "data/evaluation.csv",
    index=False
)

print(
    f"Generated {len(df)} resumes"
)