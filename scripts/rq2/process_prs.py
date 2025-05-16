import csv
import json
import os
from pathlib import Path
from utils.paths import get_project_paths

# Get project paths
PATHS = get_project_paths()
DATA_DIR = PATHS["data"]
RESULTS_DIR = PATHS["results"]
PROMPTS_DIR = PATHS["prompts"]

def get_project_name_from_url(url):
    # Extract owner/repo from GitHub URL
    parts = url.split('/')
    owner = parts[3]
    repo = parts[4]
    return f"{owner}_{repo}"

def get_pr_number_from_url(url):
    # Extract PR number from URL
    return url.split('/')[-1]

def main():
    # Input and output paths
    prs_csv_path = RESULTS_DIR / "prs.csv"
    merged_dir = RESULTS_DIR / "rq2" / "merged"
    output_csv_path = RESULTS_DIR / "prs_processed.csv"

    # Read the PRs CSV file
    with open(prs_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        prs_data = list(reader)

    # Prepare output data
    output_data = []
    fieldnames = reader.fieldnames

    # Process each PR
    for pr in prs_data:
        project_name = get_project_name_from_url(pr['Pull Request URL'])
        pr_number = get_pr_number_from_url(pr['Pull Request URL'])
        
        # Find the corresponding JSON file
        json_files = list(Path(merged_dir).glob(f"{project_name}_guideline_compliance_output.json"))
        
        if not json_files:
            print(f"Warning: No JSON file found for {project_name}")
            continue
            
        json_file = json_files[0]
        
        # Read and process the JSON file
        with open(json_file, 'r') as f:
            json_data = json.load(f)
            
        # Find the specific PR in the JSON data
        pr_data = None
        for entry in json_data:
            if entry['pull_request_id'] == pr_number:
                pr_data = entry
                break
                
        if not pr_data:
            print(f"Warning: PR {pr_number} not found in {json_file}")
            continue
            
        # Create new row with actual guideline compliance data
        new_row = {
            'Language': pr['Language'],
            'Pull Request URL': pr['Pull Request URL']
        }
        
        # Add guideline compliance data
        for guideline, value in pr_data['guideline_compliance'].items():
            new_row[guideline] = value.lower() == 'yes'
            
        output_data.append(new_row)

    # Write the output CSV file
    with open(output_csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_data)

    print(f"Processing complete. Output written to {output_csv_path}")

if __name__ == '__main__':
    main() 