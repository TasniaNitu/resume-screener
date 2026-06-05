import pandas as pd

from utils.scorer import score

df = pd.read_csv(
    "data/evaluation.csv"
)

top1_correct = 0
top3_correct = 0
total_cases = 0

for job_desc in df["job_description"].unique():

    subset = df[
        df["job_description"] == job_desc
    ].copy()

    subset["score"] = subset["resume_text"].apply(
        lambda x: score(job_desc, x)
    )

    ranked = subset.sort_values(
        "score",
        ascending=False
    )

    top1 = ranked.iloc[0]

    if top1["relevant"] == 1:
        top1_correct += 1

    if ranked.head(3)["relevant"].sum() > 0:
        top3_correct += 1

    total_cases += 1

top1_accuracy = (
    top1_correct / total_cases
) * 100

top3_accuracy = (
    top3_correct / total_cases
) * 100

print(
    f"Top-1 Accuracy: {top1_accuracy:.2f}%"
)

print(
    f"Top-3 Accuracy: {top3_accuracy:.2f}%"
)