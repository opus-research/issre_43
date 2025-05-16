import os
import json
import csv
import re
import openai
from pathlib import Path

# Configuration
DATA_PATH = Path("./data/")
OUTPUT_PATH = Path("./data/processed_guidelines")
PROMPTS_PATH = Path("./prompts")

def main():
    # Get configuration from environment variables
    MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")  # Default to gpt-4o if not specified
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    # Create output directory
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Read the guideline presence data
    with open(DATA_PATH / "rq1" / "guideline_presence_by_project.json", 'r') as f:
        guideline_data = json.load(f)

    # Get all projects from guideline data
    guideline_projects = set()
    for item in guideline_data:
        guideline_projects.update(item.keys())

    # Read the contributing.csv to get the list of projects and their languages
    projects_info = {}
    missing_projects = []
    with open(DATA_PATH / "raw" / "contributing.csv", 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Extract repository name from URL
            url = row['Contribution Guideline File']
            match = re.search(r'github\.com/([^/]+/[^/]+)', url)
            if match:
                repo_name = match.group(1)
                projects_info[repo_name] = {
                    'language': row['Language'],
                    'url': url
                }
                if repo_name not in guideline_projects:
                    missing_projects.append((repo_name, row['Language']))

    print(f"Total projects in guideline data: {len(guideline_projects)}")
    print(f"Total projects in contributing data: {len(projects_info)}")
    print(f"Number of missing projects: {len(missing_projects)}")
    print("\nMissing projects:")
    for repo, lang in missing_projects:
        print(f"{repo} ({lang})")

    # Create output CSV with the same structure as contributing.csv
    output_rows = []
    for item in guideline_data:
        for repo_name, guidelines in item.items():
            if repo_name in projects_info:
                row = {
                    'Language': projects_info[repo_name]['language'],
                    'Contribution Guideline File': projects_info[repo_name]['url'],
                    'Submit Pull Requests': guidelines.get('Submit Pull Requests', 'no').upper(),
                    'Fork and Clone the Repository': guidelines.get('Fork and Clone the Repository', 'no').upper(),
                    'Follow Code Style Guidelines': guidelines.get('Follow Code Style Guidelines', 'no').upper(),
                    'Create Feature Branches': guidelines.get('Create Feature Branches', 'no').upper(),
                    'Sign Contributor License Agreement (CLA)': guidelines.get('Sign Contributor License Agreement (CLA)', 'no').upper(),
                    'Code of Conduct': guidelines.get('Code of Conduct', 'no').upper(),
                    'Review and Address Feedback': guidelines.get('Review and Address Feedback', 'no').upper(),
                    'Document Your Changes': guidelines.get('Document Your Changes', 'no').upper(),
                    'Report Issues': guidelines.get('Report Issues', 'no').upper(),
                    'Respect Project Maintainers': guidelines.get('Respect Project Maintainers', 'no').upper(),
                    'Engage in Code Reviews': guidelines.get('Engage in Code Reviews', 'no').upper(),
                    'Update Documentation': guidelines.get('Update Documentation', 'no').upper(),
                    'Use Clear and Descriptive Commit Messages': guidelines.get('Use Clear and Descriptive Commit Messages', 'no').upper(),
                    'Write Automated Tests': guidelines.get('Write Automated Tests', 'no').upper(),
                    'Engage with Community': guidelines.get('Engage with Community', 'no').upper()
                }
                output_rows.append(row)

    # Write the output CSV
    fieldnames = [
        'Language', 'Contribution Guideline File', 'Submit Pull Requests',
        'Fork and Clone the Repository', 'Follow Code Style Guidelines',
        'Create Feature Branches', 'Sign Contributor License Agreement (CLA)',
        'Code of Conduct', 'Review and Address Feedback', 'Document Your Changes',
        'Report Issues', 'Respect Project Maintainers', 'Engage in Code Reviews',
        'Update Documentation', 'Use Clear and Descriptive Commit Messages',
        'Write Automated Tests', 'Engage with Community'
    ]

    with open(OUTPUT_PATH / "guideline_presence.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

if __name__ == "__main__":
    main() 