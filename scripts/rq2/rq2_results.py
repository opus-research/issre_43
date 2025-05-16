import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from utils.paths import get_project_paths

# Get project paths
PATHS = get_project_paths()
DATA_DIR = PATHS["data"]
RESULTS_DIR = PATHS["results"]
PROMPTS_DIR = PATHS["prompts"]

# === Load project metadata ===
with open(DATA_DIR / "raw" / "projects_by_language4.json", "r") as f:
    projects = json.load(f)["projects"]

# === Aggregate compliance by language ===
compliance_by_language = defaultdict(lambda: defaultdict(list))  # language → guideline → [bools]

for project in projects:
    owner = project["owner"]
    repo = project["repo"]
    language = project["language"]
    filepath = RESULTS_DIR / "rq2" / "merged" / f"{owner}_{repo}_guideline_compliance_output.json"

    if not os.path.exists(filepath):
        print(f"Skipping {repo} (file not found)")
        continue

    with open(filepath, "r") as f:
        prs = json.load(f)
        for pr in prs:
            for guideline, status in pr["guideline_compliance"].items():
                compliance_by_language[language][guideline].append(status == "yes")

# === Calculate average compliance per language ===
records = []
for language, guidelines in compliance_by_language.items():
    total = len(next(iter(guidelines.values()))) if guidelines else 0
    row = {"language": language}
    for guideline, results in guidelines.items():
        row[guideline] = round(sum(results) / total * 100, 2) if total > 0 else 0.0
    records.append(row)

df = pd.DataFrame(records).set_index("language")

# === Add overall average across all languages ===
overall = defaultdict(list)
for guidelines in compliance_by_language.values():
    for g, results in guidelines.items():
        overall[g].extend(results)

overall_row = {"language": "Overall Avg"}
total = len(next(iter(overall.values()))) if overall else 0
for guideline, results in overall.items():
    overall_row[guideline] = round(sum(results) / total * 100, 2) if total > 0 else 0.0

# Append to the DataFrame
df = pd.concat([df, pd.DataFrame([overall_row]).set_index("language")])

# === Plot all languages side by side INCLUDING Overall ===
df.T.plot(kind="bar", figsize=(14, 8))
plt.title("Guideline Compliance by Language (Including Avg)")
plt.xlabel("Guideline")
plt.ylabel("Compliance Percentage (%)")
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "rq2" / "rq2_guideline_compliance_by_language_with_overall.png", bbox_inches="tight")
plt.show()

# === Plot overall compliance separately ===
df.loc[["Overall Avg"]].T.plot(kind="bar", figsize=(10, 6), legend=False)
plt.title("Overall Guideline Compliance")
plt.xlabel("Guideline")
plt.ylabel("Compliance Percentage (%)")
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig(RESULTS_DIR / "rq2" / "rq2_overall_guideline_compliance.png", bbox_inches="tight")
plt.show()

# === Save data ===
df.to_csv(RESULTS_DIR / "rq2" / "guideline_compliance_by_language_incl_overall.csv")
df.loc[["Overall Avg"]].to_csv(RESULTS_DIR / "rq2" / "overall_guideline_compliance.csv")