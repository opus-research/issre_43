import os
import json
import random
import glob
from collections import defaultdict
from ..config.paths import (
    DATA_DIR, PR_DIR, SAMPLES_DIR,
    NUM_PRS, MAX_MD_FILES, TARGET_FILES_PER_LANGUAGE
)

def sample_pull_requests():
    """Sample pull requests with comments from the dataset."""
    all_prs_with_comments = []
    
    for file in os.listdir(PR_DIR):
        if file.endswith(".json"):
            path = os.path.join(PR_DIR, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    prs = json.load(f)
                    for pr in prs:
                        if isinstance(pr.get("comments"), list) and pr["comments"]:
                            pr["source_file"] = path
                            all_prs_with_comments.append(pr)
            except Exception as e:
                print(f"⚠️ Failed to load {path}: {e}")
    
    return random.sample(all_prs_with_comments, min(NUM_PRS, len(all_prs_with_comments)))

def sample_markdown_files():
    """Sample README.md and CONTRIBUTING.md files from the dataset."""
    # Find all markdown files
    all_md_files = glob.glob(os.path.join(DATA_DIR, "**", "**", "**", "*.md"), recursive=True)
    
    # Group files by project
    project_files = defaultdict(list)
    for path in all_md_files:
        parts = path.split(os.sep)
        if len(parts) >= 4:
            project_key = os.path.join(parts[1], parts[2])
            project_files[project_key].append(path)
    
    # Sample files
    selected_files = {}
    extra_files = []
    
    # Ensure at least one file per project
    for project_key, files in project_files.items():
        random.shuffle(files)
        selected_files[project_key] = [files[0]]
        extra_files.extend((project_key, f) for f in files[1:])
    
    # Fill up to max_total if needed
    remaining_slots = MAX_MD_FILES - len(selected_files)
    random.shuffle(extra_files)
    
    for project_key, file_path in extra_files:
        if len(selected_files) >= MAX_MD_FILES:
            break
        if file_path not in selected_files.get(project_key, []):
            selected_files.setdefault(project_key, []).append(file_path)
    
    return selected_files

def sample_by_language(projects_by_language):
    """Sample projects equally across languages."""
    urls_by_project = {}
    quota = TARGET_FILES_PER_LANGUAGE
    
    for lang in projects_by_language:
        projects = list(projects_by_language[lang].items())
        random.shuffle(projects)
        selected = projects[:quota]
        for project_key, url in selected:
            urls_by_project[project_key] = url
    
    # Fill remainder if needed
    remaining = [
        (project_key, url)
        for lang_dict in projects_by_language.values()
        for project_key, url in lang_dict.items()
        if project_key not in urls_by_project
    ]
    
    random.shuffle(remaining)
    for project_key, url in remaining:
        if len(urls_by_project) >= MAX_MD_FILES:
            break
        urls_by_project[project_key] = url
    
    return urls_by_project 