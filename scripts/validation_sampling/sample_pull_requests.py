import os
import json
import csv
import random
from collections import defaultdict
from config.paths import (
    PROJECTS_FILE, PR_SAMPLE_CSV, PR_SAMPLE_JSON,
    NUM_PRS
)
from utils.sampling import sample_pull_requests

# Paths
PR_DIR = os.path.join(os.path.dirname(__file__), '../../data/pull_requests')

def load_project_language_map():
    """Load the mapping of projects to their languages."""
    with open(PROJECTS_FILE, 'r') as f:
        data = json.load(f)
    return {
        f"{proj['owner']}_{proj['repo']}": proj['language']
        for proj in data['projects']
    }

def get_pr_files():
    return [f for f in os.listdir(PR_DIR) if f.endswith('.json')]

def sample_pull_requests():
    project_language = load_project_language_map()
    pr_files = get_pr_files()
    all_candidates = []
    per_project = defaultdict(list)
    per_language = defaultdict(list)

    for pr_file in pr_files:
        project_key = pr_file.replace('_aggregated_issues.json', '')
        language = project_language.get(project_key)
        if not language:
            continue
        with open(os.path.join(PR_DIR, pr_file), 'r') as f:
            try:
                prs = json.load(f)
            except Exception:
                continue
        for pr in prs:
            if pr.get('comments') and pr.get('commit_messages'):
                url = f"https://github.com/{project_key.replace('_', '/', 1)}/pull/{pr['number']}"
                row = {
                    'language': language,
                    'url': url,
                    'validation': ''
                }
                all_candidates.append(row)
                per_project[project_key].append(row)
                per_language[language].append(row)

    # Sample 50 projects per language
    selected = []
    for language in ['Python', 'Javascript', 'Java', 'C#']:
        language_candidates = per_language.get(language, [])
        if language_candidates:
            selected.extend(random.sample(language_candidates, min(50, len(language_candidates))))

    # Ensure at least one PR per project
    project_prs = defaultdict(list)
    for row in selected:
        project_key = row['url'].split('/pull/')[0].split('github.com/')[1].replace('/', '_')
        project_prs[project_key].append(row)

    final_selected = []
    for project, rows in project_prs.items():
        if rows:
            final_selected.append(random.choice(rows))

    # Fill up to 200
    remaining = [row for row in all_candidates if row not in final_selected]
    random.shuffle(remaining)
    final_selected += remaining[:max(0, 200 - len(final_selected))]
    return final_selected[:200]

def write_csv(rows):
    """Write sampled pull requests to CSV file."""
    os.makedirs(os.path.dirname(PR_SAMPLE_CSV), exist_ok=True)
    with open(PR_SAMPLE_CSV, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['language', 'url', 'validation'])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def main():
    # Load project-language mapping
    project_language = load_project_language_map()
    
    # Sample pull requests
    sampled_prs = sample_pull_requests()
    
    # Convert to CSV format
    rows = []
    for pr in sampled_prs:
        project_key = pr['source_file'].split('/')[-1].replace('_aggregated_issues.json', '')
        language = project_language.get(project_key)
        if language:
            url = f"https://github.com/{project_key.replace('_', '/', 1)}/pull/{pr['number']}"
            rows.append({
                'language': language,
                'url': url,
                'validation': ''
            })
    
    # Save results
    write_csv(rows)
    print(f"Wrote {len(rows)} rows to {PR_SAMPLE_CSV}")

if __name__ == '__main__':
    main() 