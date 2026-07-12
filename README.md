# AI Resume Screener

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://tasnianitu-resume-screener.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Sentence Transformers](https://img.shields.io/badge/Sentence%20Transformers-NLP-FFD21E?style=for-the-badge)

An NLP-powered application that ranks PDF resumes against a job description using sentence-transformer embeddings and cosine similarity.

🌐 **Live Application:**  
[https://tasnianitu-resume-screener.streamlit.app/](https://tasnianitu-resume-screener.streamlit.app/)

<!-- Upload assets/demo.gif before enabling this line:
![AI Resume Screener Demo](assets/demo.gif)
-->

---

## Overview

AI Resume Screener helps users compare multiple resumes against a job description through semantic text matching.

Instead of relying only on exact keyword overlap, the application converts job descriptions and resume text into sentence embeddings and calculates their cosine similarity. Candidates are then ranked according to their resulting match scores.

The scores represent semantic similarity and are intended to assist human review—not replace professional recruitment decisions.

---

## Features

- Upload multiple PDF resumes simultaneously
- Paste any job description
- Extract text from PDF files
- Generate semantic sentence embeddings
- Calculate resume-to-job similarity scores
- Rank candidates automatically
- Display match percentages and visual score bars
- Run without a paid external API key
- Access the application through a public Streamlit deployment

---

## How It Works

1. The user enters a job description.
2. Resume text is extracted from uploaded PDF files.
3. The job description and resumes are encoded using a Sentence Transformers model.
4. Cosine similarity is calculated between the job-description embedding and each resume embedding.
5. Candidates are ranked from highest to lowest semantic similarity.
6. The application presents the scores through an interactive Streamlit interface.

The project uses the `all-MiniLM-L6-v2` sentence-transformer model for text embeddings.

---

## Tech Stack

- **Programming:** Python
- **Interface:** Streamlit
- **Embeddings:** Sentence Transformers, Hugging Face
- **Similarity calculation:** scikit-learn
- **PDF processing:** PyPDF2
- **Data processing:** Pandas

---

## Project Structure

```text
resume-screener/
├── app.py
├── evaluate.py
├── generate_dataset.py
├── requirements.txt
├── README.md
├── utils/
│   ├── parser.py
│   └── scorer.py
└── data/
    └── evaluation.csv
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/TasniaNitu/resume-screener.git
cd resume-screener
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application should open in the default browser.

---

## Usage

1. Paste a job description into the text field.
2. Upload two or more PDF resumes.
3. Click **Screen Resumes**.
4. Review the ranked candidates.
5. Compare their semantic match percentages.

---

## Evaluation

The ranking system was evaluated on an internally generated synthetic benchmark containing **600 candidate profiles** across several job categories.

The benchmark includes:

- AI Engineer
- Data Scientist
- Software Engineer
- Business Analyst
- Marketing roles

Candidate profiles include overlapping skill distributions and hard-negative examples intended to make ranking more challenging.

| Metric | Synthetic benchmark result |
|---|---:|
| Top-1 Accuracy | 100% |
| Top-3 Accuracy | 100% |

The evaluation can be reproduced with:

```bash
python evaluate.py
```

### Evaluation limitations

These results measure performance only on the generated synthetic benchmark. They do not establish equivalent performance on real applicant resumes, unfamiliar industries, unusual formatting, or real recruitment decisions.

Future evaluation should include anonymized human-reviewed resumes, ranking metrics such as Mean Reciprocal Rank or nDCG, and analysis across a wider range of job descriptions.

---

## Responsible Use and Limitations

- Match percentages represent semantic similarity, not a candidate’s complete suitability.
- High textual similarity does not guarantee professional competence or job performance.
- The model may overlook transferable skills, unusual terminology, or experience described differently.
- Human review should remain part of every recruitment decision.
- The application should not be used to make autonomous hiring or rejection decisions.
- Image-only and scanned PDFs may not work because the current PDF parser does not perform OCR.
- Production use would require stronger privacy, security, fairness, and data-retention controls.

---

## Future Improvements

- Skill and experience extraction
- Resume keyword highlighting
- Candidate-match explanations
- CSV result export
- Recruiter dashboard
- OCR support for scanned resumes
- Additional ranking metrics
- Bias and fairness evaluation
- LLM-assisted candidate feedback

---

## Author

**Kazi Tasnia Nitu**

- GitHub: [github.com/TasniaNitu](https://github.com/TasniaNitu)
- Portfolio: [tasnianitu.github.io](https://tasnianitu.github.io)
- LinkedIn: [linkedin.com/in/tasnia-ai](https://www.linkedin.com/in/tasnia-ai)
- Live Application: [AI Resume Screener](https://tasnianitu-resume-screener.streamlit.app/)
