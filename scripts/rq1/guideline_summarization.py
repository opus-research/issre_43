import json
import os
import openai
from pathlib import Path

# Configuration
DATA_PATH = Path("./data/")
OUTPUT_PATH = Path("./data/summarized_guidelines")
PROMPTS_PATH = Path("./prompts")

def main():
    # Get configuration from environment variables
    MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")  # Default to gpt-4o if not specified
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    # Create output directory
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Load the project list
    with open(DATA_PATH / "raw" / "projects_by_language.json", "r", encoding="utf-8") as f:
        projects = json.load(f)["projects"]

    # Dictionary to store guidelines per project
    project_guidelines = {}

    for project in projects:
        owner = project["owner"]
        repo = project["repo"]
        filename = f"{owner}-{repo}.json"
        file_path = DATA_PATH / "gpt-4o-guidelines" / filename

        if not file_path.exists():
            print(f"⚠️ File not found: {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            content = json.load(f)

        # Collect guideline titles into a set
        guideline_titles = set()
        contributing_data = content.get("CONTRIBUTING", {})
        for section in contributing_data.values():
            guidelines = section.get("guidelines", [])
            for guideline in guidelines:
                title = guideline.get("title")
                if title:
                    guideline_titles.add(title)

        project_key = f"{owner}/{repo}"
        project_guidelines[project_key] = sorted(guideline_titles)

    # Save the result to a JSON file
    output_file = OUTPUT_PATH / "projects_guidelines.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(project_guidelines, f, indent=2, ensure_ascii=False)

    print(f"✅ Guideline titles saved to {output_file}")

if __name__ == "__main__":
    main()