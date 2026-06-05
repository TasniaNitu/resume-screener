# AI Resume Screener

Live Demo:
https://tasnianitu-resume-screener.streamlit.app/

## Overview

AI Resume Screener is a machine learning-powered applicant screening tool that automatically ranks resumes against a job description.

The application:

- Extracts text from PDF resumes
- Encodes job descriptions and resumes using Sentence Transformers
- Calculates semantic similarity using cosine similarity
- Ranks candidates automatically
- Displays match percentages and visual score bars
- Supports multiple resume uploads simultaneously

---

## Live Demo

https://tasnianitu-resume-screener.streamlit.app/

---

## Features

- Upload multiple PDF resumes
- Paste any job description
- AI-powered semantic matching
- Automatic candidate ranking
- Match score visualization
- Fast local inference
- No API key required

---

## Tech Stack

- Python
- Streamlit
- Pandas
- PyPDF2
- Sentence Transformers
- Scikit-learn
- Hugging Face Transformers

---

## Project Structure

resume-screener/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│ ├── parser.py
│ └── scorer.py
│
├── data/
│ └── evaluation.csv
│
├── evaluate.py
└── generate_dataset.py

---

## Installation

Clone the repository:

```bash
git clone https://github.com/TasniaNitu/resume-screener.git
cd resume-screener
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

---

## Evaluation

The ranking system was evaluated using 600 synthetic candidate profiles generated across multiple job categories.

Metrics:

- Top-1 Accuracy: 100%
- Top-3 Accuracy: 100%

Evaluation includes:

- AI Engineer
- Data Scientist
- Software Engineer
- Business Analyst
- Marketing roles

with overlapping skill distributions and hard-negative candidate profiles.

---

## Example Workflow

1. Paste job description
2. Upload resume PDFs
3. Click "Screen Resumes"
4. View ranked candidates
5. Compare match percentages

---

## Future Improvements

- Skill extraction
- Resume keyword highlighting
- Candidate explanations
- Export results to CSV
- Recruiter dashboard
- LLM-based feedback generation

---

## Author

Tasnia Nitu

GitHub:
https://github.com/TasniaNitu

Live App:
https://tasnianitu-resume-screener.streamlit.app/
