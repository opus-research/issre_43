import csv
import json

input_json_path = "markdown_files_urls_checked.json"
output_csv_path = "markdown_urls_validation.csv"

# Load validated URLs
with open(input_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Write CSV
with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["language", "contributing_file_url", "validation"])

    for project_key, url in data.items():
        language = project_key.split("/")[0]
        writer.writerow([language, url, "✅"])

print(f"✅ CSV saved to {output_csv_path}")