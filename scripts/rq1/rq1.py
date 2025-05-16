from collections import defaultdict

import numpy as np
import openai
import json
import os
import matplotlib.pyplot as plt
from pathlib import Path

# === Configuration ===
DATA_PATH = Path("./data/")
OUTPUT_PATH = Path("./data/rq1_results")
PROMPTS_PATH = Path("./prompts")

# Get configuration from environment variables
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")  # Default to gpt-4o if not specified
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Create output directories
os.makedirs(OUTPUT_PATH, exist_ok=True)
os.makedirs(OUTPUT_PATH / "plots", exist_ok=True)

def cluster_guidelines():
    # Load the prompt text
    with open("../../prompts/openai_rq1.txt", "r", encoding="utf-8") as f:
        base_prompt = f.read()

    # Load clustered guideline input JSON
    with open(DATA_PATH / "guidelines_clustered.json", "r", encoding="utf-8") as f:
        guidelines = json.load(f)

    full_prompt = f"{base_prompt.strip()}\n\nHere is the clustered guideline data:\n{json.dumps(guidelines, indent=2)}"

    # Send to OpenAI
    print("Sending prompt to OpenAI...")
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that organizes open source contribution guidelines."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.2
    )

    # Extract reply
    reply = response.choices[0].message.content

    # Write raw output
    with open(OUTPUT_PATH / "response_output.txt", "w", encoding="utf-8") as f:
        f.write(reply)

    # Try to parse JSON
    try:
        result_json = json.loads(reply)
    except json.JSONDecodeError:
        print("⚠️ Could not decode response as JSON. Saving raw text.")
        result_json = {"raw_response": reply}

    # Save final result
    with open(OUTPUT_PATH / "guidelines.json", "w", encoding="utf-8") as f:
        json.dump(result_json, f, indent=2, ensure_ascii=False)

    print("✅ Output saved to data/rq1_results/guidelines.json")

def guideline_presence_by_project():
    # Load the prompt text
    with open(PROMPTS_PATH / "guideline_collection.txt", "r", encoding="utf-8") as f:
        base_prompt = f.read()

    # Load final standard guidelines
    with open(OUTPUT_PATH / "guidelines.json", "r", encoding="utf-8") as f:
        final_guidelines = json.load(f)

    guidelines = final_guidelines['response']['final_guidelines']

    # Load project guideline mentions
    with open(DATA_PATH / "summarized_guidelines" / "projects_guidelines.json", "r", encoding="utf-8") as f:
        project_guidelines = json.load(f)

    full_prompt = f"{base_prompt.strip()}\n\nStandard Guidelines:\n{json.dumps(guidelines, indent=2)}\n\nProject Guidelines:\n{json.dumps(project_guidelines, indent=2)}"

    # Send to OpenAI
    print("Sending prompt to OpenAI...")
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an assistant that checks which standardized contribution guidelines are present in different GitHub projects."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.2
    )

    # Extract reply
    reply = response.choices[0].message.content

    # Write raw output
    with open(OUTPUT_PATH / "presence_output.txt", "w", encoding="utf-8") as f:
        f.write(reply)

    # Try to parse JSON
    try:
        result_json = json.loads(reply)
    except json.JSONDecodeError:
        print("⚠️ Could not decode response as JSON. Saving raw text.")
        result_json = {"raw_response": reply}

    # Save final result
    with open(OUTPUT_PATH / "guideline_presence_by_project.json", "w", encoding="utf-8") as f:
        json.dump(result_json, f, indent=2, ensure_ascii=False)

    print("✅ Output saved to data/rq1_results/guideline_presence_by_project.json")

def compile_data_by_project():
    # === Load data ===
    with open(OUTPUT_PATH / "guideline_presence_by_project.json", "r", encoding="utf-8") as f:
        presence_data = json.load(f)

    with open(DATA_PATH / "raw" / "projects_by_language.json", "r", encoding="utf-8") as f:
        project_metadata = json.load(f)

    # === Map project full names to languages ===
    project_lang_map = {
        f"{proj['owner']}/{proj['repo']}": proj["language"]
        for proj in project_metadata["projects"]
    }

    # === Initialize counters ===
    total_counts = defaultdict(lambda: {"yes": 0, "total": 0})
    language_counts = defaultdict(lambda: defaultdict(lambda: {"yes": 0, "total": 0}))

    # === Process each project ===
    for project_entry in presence_data:
        for project_name, guideline_results in project_entry.items():
            language = project_lang_map.get(project_name, "Unknown")
            for guideline, result in guideline_results.items():
                total_counts[guideline]["total"] += 1
                language_counts[language][guideline]["total"] += 1
                if result == "yes":
                    total_counts[guideline]["yes"] += 1
                    language_counts[language][guideline]["yes"] += 1

    # === Compute percentages ===
    summary = {
        "overall": {},
        "by_language": {}
    }

    for guideline, counts in total_counts.items():
        percentage = (counts["yes"] / counts["total"]) * 100
        summary["overall"][guideline] = round(percentage, 2)

    for language, guidelines in language_counts.items():
        summary["by_language"][language] = {}
        for guideline, counts in guidelines.items():
            percentage = (counts["yes"] / counts["total"]) * 100
            summary["by_language"][language][guideline] = round(percentage, 2)

    # === Output summary ===
    print("\n✅ Overall Guideline Presence (% of Projects):")
    for guideline, percent in summary["overall"].items():
        print(f"- {guideline}: {percent:.2f}%")

    print("\n✅ Guideline Presence by Language:")
    for lang, guidelines in summary["by_language"].items():
        print(f"\n📚 Language: {lang}")
        for guideline, percent in guidelines.items():
            print(f"  - {guideline}: {percent:.2f}%")

    # === Save summary ===
    with open(OUTPUT_PATH / "guideline_presence_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("\n📄 Saved to data/rq1_results/guideline_presence_summary.json")

def plot_grouped():
    # === Load the summary JSON ===
    with open(OUTPUT_PATH / "guideline_presence_summary.json", "r", encoding="utf-8") as f:
        summary = json.load(f)

    overall = summary["overall"]
    by_language = summary["by_language"]

    # Include 'Overall' in the language list
    by_language_with_overall = dict(by_language)  # shallow copy
    by_language_with_overall["Overall"] = overall

    # === 1. Grouped bar chart: Guidelines × Languages (including Overall) ===
    guidelines = list(overall.keys())
    languages = list(by_language_with_overall.keys())
    x = np.arange(len(guidelines))  # label locations
    width = 0.8 / len(languages)  # total width split per language

    plt.figure(figsize=(14, 6))
    for i, lang in enumerate(languages):
        lang_scores = [by_language_with_overall[lang].get(g, 0) for g in guidelines]
        plt.bar(x + i * width, lang_scores, width, label=lang)

    plt.ylabel("Presence (%)")
    plt.title("Guideline Presence by Language (Grouped, Including Overall)")
    plt.xticks(x + width * (len(languages) - 1) / 2, guidelines, rotation=45, ha="right")
    plt.ylim(0, 100)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH / "plots" / "guideline_presence_grouped_by_language_incl_overall.png")
    plt.close()

    # === 2. Per-language charts: Guidelines per language ===
    for lang, guideline_data in by_language_with_overall.items():
        plt.figure(figsize=(10, 5))
        g_names = list(guideline_data.keys())
        g_values = [guideline_data[g] for g in g_names]

        plt.barh(g_names, g_values)
        plt.xlim(0, 100)
        plt.xlabel("Presence (%)")
        plt.title(f"Guideline Presence for Language: {lang}")
        plt.tight_layout()

        lang_filename = lang.lower().replace(" ", "_").replace("/", "_")
        plt.savefig(OUTPUT_PATH / "plots" / f"guideline_presence_per_language_{lang_filename}.png")
        plt.close()

    print("✅ Grouped and per-language charts saved to data/rq1_results/plots/")

if __name__ == "__main__":
    cluster_guidelines()
    guideline_presence_by_project()
    compile_data_by_project()
    plot_grouped()