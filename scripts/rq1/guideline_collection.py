import os
import pathlib
import json
import time

import markdown
import bs4
import openai
from tqdm.auto import tqdm

# Configuration
DATA_PATH = pathlib.Path("./data/")
OUTPUT_PATH = pathlib.Path("./data/gpt-4o-guidelines")
PROMPTS_PATH = pathlib.Path("./prompts")

# Get configuration from environment variables
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")  # Default to gpt-4o if not specified
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

def load_prompt(prompt_name: str) -> str:
    """
    Load a prompt from the prompts directory.
    """
    prompt_path = os.path.join(PROMPTS_PATH, f"{prompt_name}.txt")
    try:
        with open(prompt_path, "r") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error loading prompt {prompt_name}: {str(e)}")
        return None

def summarize_doc(document):
    """
    Summarize a document using ChatGPT to extract contribution guidelines.
    """
    while True:
        try:
            # Convert markdown to plain text
            html = markdown.markdown(document)
            soup = bs4.BeautifulSoup(html, features='html.parser')
            doc = soup.get_text()

            # Load and format prompt
            prompt_template = load_prompt("guideline_collection")
            if not prompt_template:
                raise Exception("Failed to load prompt template")
            
            prompt = prompt_template.format(doc=doc)

            # Call ChatGPT
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that extracts and summarizes contribution guidelines from documentation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )

            # Extract the response
            result = response.choices[0].message.content.strip()
            
            # Validate that the response is valid JSON
            json.loads(result)
            return result

        except json.JSONDecodeError:
            print("Invalid JSON response, retrying...")
            time.sleep(1)
            continue
        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(1)
            continue

def process_project(language, project_name, index, total_projects):
    """
    Process a single project's documentation.
    """
    print(f"\nProcessing {language}/{project_name} ({index + 1}/{total_projects})...", flush=True)
    project_result = {
        'CONTRIBUTING': {},
        'README': {}
    }
    
    project_path = os.path.join(DATA_PATH, language, project_name)

    # Process files
    try:
        commits = [name for name in os.listdir(project_path)]
    except FileNotFoundError:
        print(f"Project directory not found: {project_path}")
        return None

    for commit in tqdm(commits, desc=f"Processing {project_name}"):
        # Process CONTRIBUTING.md
        contributing_path = os.path.join(project_path, commit, "CONTRIBUTING.md")
        if os.path.exists(contributing_path):
            try:
                with open(contributing_path, "r", encoding="utf-8", errors="replace") as f:
                    file_content = f.read()
                project_result['CONTRIBUTING'][commit] = json.loads(summarize_doc(file_content))
            except Exception as e:
                print(f"Error processing CONTRIBUTING.md for {commit}: {str(e)}")

        # Process README.md
        readme_path = os.path.join(project_path, commit, "README.md")
        if os.path.exists(readme_path):
            try:
                with open(readme_path, "r", encoding="utf-8", errors="replace") as f:
                    file_content = f.read()
                project_result['README'][commit] = json.loads(summarize_doc(file_content))
            except Exception as e:
                print(f"Error processing README.md for {commit}: {str(e)}")

    return project_result

def main():
    """
    Main function to process all projects.
    """
    # Create output directory
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Load projects from JSON file
    try:
        with open(os.path.join(DATA_PATH, "raw", "projects_by_language.json"), "r") as f:
            projects_data = json.load(f)
    except Exception as e:
        print(f"Error loading projects data: {str(e)}")
        return

    # Process each language and its projects
    total_projects = sum(len(projects) for projects in projects_data.values())
    processed_count = 0

    for language, projects in projects_data.items():
        for project_name in projects:
            # Convert project name to the format used in the output files
            output_project_name = project_name.replace('/', '-')
            output_file_path = os.path.join(OUTPUT_PATH, f"{output_project_name}.json")
            
            # Skip if already processed
            if os.path.exists(output_file_path):
                print(f"Skipping {language}/{project_name} - already processed")
                processed_count += 1
                continue

            # Process project
            project_result = process_project(language, project_name, processed_count, total_projects)
            processed_count += 1

            # Only save if we have either CONTRIBUTING or README guidelines
            if project_result and (project_result['CONTRIBUTING'] or project_result['README']):
                # Save results
                with open(output_file_path, "w", encoding="utf-8") as f:
                    json.dump(project_result, f, indent=2)

if __name__ == "__main__":
    main() 