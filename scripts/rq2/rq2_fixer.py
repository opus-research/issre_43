import json
import os
import re
from utils.paths import get_project_paths

# Get project paths
PATHS = get_project_paths()
DATA_DIR = PATHS["data"]
RESULTS_DIR = PATHS["results"]
PROMPTS_DIR = PATHS["prompts"]

def extract_and_fix_json_list(text):
    text = text.strip()
    if text.startswith("```json") or text.startswith("```"):
        text = text.strip("```json").strip("```").strip()

    # Attempt full load first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Step 1: Remove outer brackets if needed
    if text.startswith("[") and not text.endswith("]"):
        text = text.rstrip(", \n")

    # Step 2: Try parsing object-by-object manually
    valid_objects = []
    depth = 0
    buffer = ""
    in_string = False
    escape = False

    for char in text:
        buffer += char

        if char == '\\' and not escape:
            escape = True
            continue

        if char == '"' and not escape:
            in_string = not in_string

        escape = False

        if not in_string:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1

        if depth == 0 and buffer.strip().startswith("{") and buffer.strip().endswith("}"):
            try:
                obj = json.loads(buffer)
                valid_objects.append(obj)
                buffer = ""
            except json.JSONDecodeError:
                break  # Stop at first broken object

    return valid_objects

def compile_project_results(project_name):
    raw_dir = RESULTS_DIR / "rq2" / f"{project_name}_raw_batches"
    output_path = RESULTS_DIR / "rq2" / f"{project_name}_guideline_compliance_output.json"
    all_results = []

    if not os.path.exists(raw_dir):
        return

    batch_files = sorted([f for f in os.listdir(raw_dir) if f.endswith(".txt")])
    for batch_file in batch_files:
        with open(raw_dir / batch_file, "r", encoding="utf-8") as f:
            raw_text = f.read()
            parsed = extract_and_fix_json_list(raw_text)
            all_results.extend(parsed)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)

    print(f"✅ Compiled {len(all_results)} results for {project_name}")

def merge_compliance_results(owner, repo):
    project_name = f"{owner}_{repo}"
    base_path = RESULTS_DIR / "rq2" / f"{project_name}_guideline_compliance_output.json"
    extra_path = RESULTS_DIR / "rq2" / "compliance" / f"{repo}_guideline_compliance_output.json"
    output_path = RESULTS_DIR / "rq2" / "merged" / f"{project_name}_guideline_compliance_output.json"

    if not os.path.exists(base_path) or not os.path.exists(extra_path):
        print(f"⛔ Missing files for {project_name}")
        return

    with open(base_path, "r", encoding="utf-8") as f1:
        base_data = {pr["pull_request_id"]: pr["guideline_compliance"] for pr in json.load(f1)}

    with open(extra_path, "r", encoding="utf-8") as f2:
        extra_data = {pr["pull_request_id"]: pr["guideline_compliance"] for pr in json.load(f2)}

    all_ids = set(base_data.keys()).union(extra_data.keys())
    merged_results = []

    for pr_id in all_ids:
        g1 = base_data.get(pr_id, {})
        g2 = extra_data.get(pr_id, {})
        all_guidelines = set(g1.keys()).union(g2.keys())
        merged = {}

        for guideline in all_guidelines:
            val1 = g1.get(guideline)
            val2 = g2.get(guideline)
            merged[guideline] = "yes" if val1 == "yes" or val2 == "yes" else "no"

        merged_results.append({
            "pull_request_id": pr_id,
            "guideline_compliance": merged
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged_results, f, indent=2)

    print(f"✅ Merged result saved: {output_path}")

with open(DATA_DIR / "raw" / "projects_by_language4.json", "r", encoding="utf-8") as f:
    projects = json.load(f)["projects"]

for project in projects:
    owner = project["owner"]
    repo = project["repo"]
    project_name = f"{owner}_{repo}"

    # compile_project_results(project_name)
    merge_compliance_results(owner, repo)