import json
import os
import bson
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
languages = ["C#", "Java", "Javascript", "Python"]
projects = []

def extract_owner_repo(pr_url):
    parts = pr_url.strip().split("/")
    if len(parts) >= 5:
        return parts[3], parts[4]
    return None, None

for language in languages:
    base_dir = f"../data/{language}/dump/"
    for project_dir in os.listdir(base_dir):
        project_path = os.path.join(base_dir, project_dir)
        if not os.path.isdir(project_path):
            continue

        print(f"\n📂 Importing project: {project_dir}")
        project_db = client[project_dir]

        collection = project_db['pull_requests']
        pr = collection.find_one({})
        if not pr:
            try:
                for file_name in os.listdir(project_path):
                    if not file_name.endswith(".bson"):
                        continue

                    collection_name = file_name.replace(".bson", "")
                    file_path = os.path.join(project_path, file_name)

                    try:
                        with open(file_path, "rb") as f:
                            data = bson.decode_all(f.read())
                            if data:
                                collection = project_db[collection_name]
                                collection.insert_many(data)
                                #print(f"✅ Imported {len(data)} docs into '{project_dir}.{collection_name}'")
                    except Exception as e:
                        pass
                        #print(f"❌ Error processing {file_name} in {project_dir}: {e}")
            except:
                pass
        owner, repo = extract_owner_repo(pr['html_url'])
        projects.append({"owner": owner, "repo": repo, "language": language})

projects_data = {"projects": projects}

with open("../../data/raw/projects_by_language.json", "w", encoding="utf-8") as f:
    json.dump(projects_data, f, indent=4)