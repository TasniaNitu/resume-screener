import streamlit as st
import pandas as pd

from utils.parser import extract_text
from utils.scorer import score


# Page settings
st.set_page_config(page_title="AI Resume Screener")

# Title
st.title("AI Resume Screener")


# Section A: Job Description
job_description = st.text_area(
    "Paste Job Description",
    height=200
)


# Section B: Resume Upload
uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)


# Screen resumes button
if st.button("Screen Resumes"):

    if not job_description:
        st.warning("Please enter a job description.")

    elif not uploaded_files:
        st.warning("Please upload at least one resume.")

    else:

        results = []

        # Process each uploaded resume
        for file in uploaded_files:

            # Extract text from PDF
            resume_text = extract_text(file)

            # Calculate similarity score
            similarity_score = score(
                job_description,
                resume_text
            )

            results.append({
                "Resume": file.name,
                "Match %": round(similarity_score * 100, 2)
            })

        # Create DataFrame
        df = pd.DataFrame(results)

        # Sort by score descending
        df = df.sort_values(
            by="Match %",
            ascending=False
        )

        # Add ranking column
        df = df.reset_index(drop=True)

        df.insert(
            0,
            "Rank",
            range(1, len(df) + 1)
        )

        # Section C: Results Table
        st.subheader("Candidate Rankings")
        st.dataframe(
    df,
    hide_index=True,
    use_container_width=True
)

        # Visual score bars
        st.subheader("Candidate Match Scores")

        for _, row in df.iterrows():

            st.write(
                f"#{row['Rank']} — {row['Resume']} ({row['Match %']}%)"
            )

            st.progress(
                row["Match %"] / 100
            )