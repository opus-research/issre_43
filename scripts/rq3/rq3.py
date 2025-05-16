import json
from collections import defaultdict
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import chi2_contingency
import seaborn as sns
from pathlib import Path

from utils.paths import get_project_paths

# Get project paths
PATHS = get_project_paths()
DATA_DIR = PATHS["data"]
RESULTS_DIR = PATHS["results"]

def main():
    projects_file = DATA_DIR / "raw" / "projects_by_language.json"

    # === Create output folders ===
    os.makedirs(RESULTS_DIR / "rq3/overall_guideline_summary", exist_ok=True)
    os.makedirs(RESULTS_DIR / "rq3/plots", exist_ok=True)

    # === Initialize counters ===
    overall_counts = defaultdict(lambda: {"merged_yes": 0, "merged_no": 0})
    language_counts = defaultdict(lambda: defaultdict(lambda: {"merged_yes": 0, "merged_no": 0}))
    global_merged_total = 0
    global_not_merged_total = 0

    # === Load and process each project ===
    with open(projects_file, "r", encoding="utf-8") as f:
        projects = json.load(f)["projects"]

    for project in projects:
        owner = project["owner"]
        repo = project["repo"]
        language = project["language"]
        print(f"Processing {owner}/{repo} ({language})...")

        try:
            with open(RESULTS_DIR / f"rq2/merged/{owner}_{repo}_guideline_compliance_output.json", 'r', encoding='utf-8') as f:
                compliance_data = json.load(f)
            with open(DATA_DIR / f"pull_requests/{owner}_{repo}_aggregated_issues.json", 'r', encoding='utf-8') as f:
                pull_requests_data = json.load(f)
        except FileNotFoundError:
            print(f"❌ Missing files for {repo}, skipping...")
            continue

        merged_status = {pr["_id"]: pr.get("was_merged", False) for pr in pull_requests_data}

        for pr in compliance_data:
            pr_id = pr["pull_request_id"]
            guidelines = pr["guideline_compliance"]
            was_merged = merged_status.get(pr_id, False)

            if was_merged:
                global_merged_total += 1
            else:
                global_not_merged_total += 1

            for guideline, status in guidelines.items():
                if status.lower() == "yes":
                    if was_merged:
                        overall_counts[guideline]["merged_yes"] += 1
                        language_counts[language][guideline]["merged_yes"] += 1
                    else:
                        overall_counts[guideline]["merged_no"] += 1
                        language_counts[language][guideline]["merged_no"] += 1

    print("\n✅ Finished processing all projects!\n")

    # === Process counts into DataFrame ===
    def process_counts(counts_dict, total_merged, total_not_merged):
        summary = []
        for guideline, counts in counts_dict.items():
            merged_yes = counts["merged_yes"]
            not_merged_yes = counts["merged_no"]

            percent_merged = (merged_yes / total_merged * 100) if total_merged > 0 else 0
            percent_not_merged = (not_merged_yes / total_not_merged * 100) if total_not_merged > 0 else 0

            summary.append({
                "Guideline": guideline,
                "Yes When Merged": merged_yes,
                "Yes When Not Merged": not_merged_yes,
                "% Yes When Merged": round(percent_merged, 2),
                "% Yes When Not Merged": round(percent_not_merged, 2)
            })

        return pd.DataFrame(summary).sort_values("Guideline")

    # === Overall summary ===
    df_overall = process_counts(overall_counts, global_merged_total, global_not_merged_total)
    df_overall.to_csv(RESULTS_DIR / "rq3/overall_guideline_summary/overall_guideline_summary.csv", index=False)
    df_overall.to_json(RESULTS_DIR / "rq3/overall_guideline_summary/overall_guideline_summary.json", orient="records", indent=2, force_ascii=False)

    # === Plot overall ===
    plt.figure(figsize=(14, 8))
    bar_width = 0.4
    x = range(len(df_overall))

    plt.bar(x, df_overall["% Yes When Merged"], width=bar_width, label="% Merged", align="center")
    plt.bar([i + bar_width for i in x], df_overall["% Yes When Not Merged"], width=bar_width, label="% Not Merged", align="center")

    plt.xticks([i + bar_width/2 for i in x], df_overall["Guideline"], rotation=90)
    plt.xlabel("Guideline")
    plt.ylabel("Percentage of 'Yes'")
    plt.title("Guideline Presence by Merge Status")
    plt.legend()
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "rq3/plots/rq3_guideline_presence_percentages.png", dpi=300)
    plt.close()

    # === Process by language ===
    for language, counts_dict in language_counts.items():
        print(f"Saving results for language: {language}")
        df_lang = process_counts(counts_dict, global_merged_total, global_not_merged_total)
        lang_safe = language.replace(" ", "_").lower()

        df_lang.to_csv(RESULTS_DIR / f"rq3/overall_guideline_summary/{lang_safe}_guideline_summary.csv", index=False)
        df_lang.to_json(RESULTS_DIR / f"rq3/overall_guideline_summary/{lang_safe}_guideline_summary.json", orient="records", indent=2, force_ascii=False)

        plt.figure(figsize=(14, 8))
        x = range(len(df_lang))
        plt.bar(x, df_lang["% Yes When Merged"], width=bar_width, label="% Merged", align="center")
        plt.bar([i + bar_width for i in x], df_lang["% Yes When Not Merged"], width=bar_width, label="% Not Merged", align="center")
        plt.xticks([i + bar_width/2 for i in x], df_lang["Guideline"], rotation=90)
        plt.xlabel("Guideline")
        plt.ylabel("Percentage of 'Yes'")
        plt.title(f"{language} - Guideline Presence by Merge Status")
        plt.legend()
        plt.tight_layout()
        plt.savefig(RESULTS_DIR / f"rq3/plots/{lang_safe}_guideline_compliance_percentages.png", dpi=300)
        plt.close()

    # === Binary Matrix for Chi-Square and Random Forest ===
    print("\nRunning Chi-Square Test and Feature Importance...")

    binary_rows = []
    for project in projects:
        owner = project["owner"]
        repo = project["repo"]

        try:
            with open(RESULTS_DIR / f"rq2/{owner}_{repo}_guideline_compliance_output.json", 'r', encoding='utf-8') as f:
                compliance_data = json.load(f)
            with open(DATA_DIR / f"pull_requests/{owner}_{repo}_aggregated_issues.json", 'r', encoding='utf-8') as f:
                pull_requests_data = json.load(f)
        except:
            continue

        merged_status = {pr["_id"]: pr.get("was_merged", False) for pr in pull_requests_data}

        for pr in compliance_data:
            pr_id = pr["pull_request_id"]
            guidelines = pr["guideline_compliance"]
            merged = merged_status.get(pr_id, False)
            row = {"merged": int(merged)}
            for g in overall_counts.keys():
                row[g] = 1 if guidelines.get(g, "no").lower() == "yes" else 0
            binary_rows.append(row)

    df_bin = pd.DataFrame(binary_rows)
    df_bin.to_csv(RESULTS_DIR / "rq3/overall_guideline_summary/binary_guideline_matrix.csv", index=False)

    # === Chi-Square Test ===
    chi_results = []
    for g in overall_counts.keys():
        contingency = pd.crosstab(df_bin[g], df_bin["merged"])
        if contingency.shape == (2, 2):
            chi2, p, _, _ = chi2_contingency(contingency)
            chi_results.append({
                "Guideline": g,
                "p-value": round(p, 5),
                "Significant (p<0.05)": p < 0.05
            })

    df_chi = pd.DataFrame(chi_results).sort_values("p-value")
    df_chi.to_csv(RESULTS_DIR / "rq3/overall_guideline_summary/chi_square_results.csv", index=False)

    # === Random Forest Feature Importance ===
    print("Training Random Forest for Feature Importance...")
    X = df_bin.drop(columns=["merged"])
    y = df_bin["merged"]
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    importance_df = pd.DataFrame({
        "Guideline": X.columns,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False)

    importance_df.to_csv(RESULTS_DIR / "rq3/overall_guideline_summary/random_forest_importance.csv", index=False)

    # Plot feature importance
    plt.figure(figsize=(12, 6))
    sns.barplot(data=importance_df, x="Importance", y="Guideline")
    plt.title("Random Forest Feature Importance - Overall")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / "rq3/plots/random_forest_importance.png", dpi=300)
    plt.close()

    # === Generate LaTeX Tables ===
    latex_output_folder = RESULTS_DIR / "rq3/latex_tables"
    os.makedirs(latex_output_folder, exist_ok=True)

    # Chi-Square LaTeX
    with open(latex_output_folder / "chi_square_table.tex", "w", encoding="utf-8") as f:
        f.write(df_chi.to_latex(index=False, caption="Chi-Square Test Results for Guideline Compliance", label="tab:chi_square", float_format="%.5f"))

    # Random Forest LaTeX
    with open(latex_output_folder / "random_forest_table.tex", "w", encoding="utf-8") as f:
        f.write(importance_df.to_latex(index=False, caption="Random Forest Feature Importance for Guideline Compliance", label="tab:random_forest", float_format="%.5f"))

if __name__ == "__main__":
    main()