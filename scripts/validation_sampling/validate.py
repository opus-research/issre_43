import json
import os
from config.paths import MD_URLS_JSON, MD_URLS_CHECKED_JSON
from utils.github import is_url_valid, parse_github_url, fix_github_url

def validate_urls():
    """Validate and fix GitHub URLs in the dataset."""
    # Load URLs to validate
    with open(MD_URLS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    fixed_data = {}
    print("🔍 Checking and fixing URLs...")

    for project_key, url in data.items():
        if is_url_valid(url):
            fixed_data[project_key] = url
            continue

        print(f"⚠️ 404 on: {url}")

        # Try fixing URL
        lang, broken_key = project_key.split("/", 1)
        if "-" in broken_key:
            org, repo = broken_key.split("-", 1)
            guessed_org = org + "-" + repo.split("-")[0]
            guessed_repo = "-".join(repo.split("-")[1:])
            
            fixed_url = fix_github_url(url, guessed_org, guessed_repo)
            if fixed_url and is_url_valid(fixed_url):
                fixed_key = f"{lang}/{guessed_org}-{guessed_repo}"
                fixed_data[fixed_key] = fixed_url
                print(f"✅ Fixed: {url} → {fixed_url}")
                continue

        print(f"❌ Could not fix: {url}")

    # Save results
    os.makedirs(os.path.dirname(MD_URLS_CHECKED_JSON), exist_ok=True)
    with open(MD_URLS_CHECKED_JSON, "w", encoding="utf-8") as f:
        json.dump(fixed_data, f, indent=2)

    print(f"\n✅ Done. Valid URLs saved to: {MD_URLS_CHECKED_JSON}")
    print(f"Total valid: {len(fixed_data)}")

if __name__ == "__main__":
    validate_urls()