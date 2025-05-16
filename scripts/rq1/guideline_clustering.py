import os
import json
import string
import nltk
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
import openai

# Configuration
DATA_PATH = Path("./data/")
OUTPUT_PATH = Path("./data/guidelines_clustered.json")
PROMPTS_PATH = Path("./prompts")

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

def preprocess_text(txt: str) -> str:
    """
    Preprocess text by:
    1. Converting to lowercase
    2. Removing punctuation
    3. Tokenizing
    4. Lemmatizing
    5. Removing stopwords
    """
    txt = txt.lower()
    txt = ''.join([char for char in txt if char not in string.punctuation])
    tokens = nltk.word_tokenize(txt)
    lemmatizer = nltk.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in nltk.corpus.stopwords.words('english')]
    return ' '.join(tokens)

def cluster_guidelines(guidelines: list):
    """
    Cluster guidelines using TF-IDF and Agglomerative Clustering.
    """
    print("Clustering data...")
    guidelines_preprocessed = [preprocess_text(guideline) for guideline in guidelines]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(guidelines_preprocessed)

    num_clusters = 100
    clustering = AgglomerativeClustering(n_clusters=num_clusters)
    clustering.fit(tfidf_matrix.toarray())

    labels = clustering.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print(f"Estimated number of clusters: {n_clusters_}")

    # Create clusters dictionary
    clusters = {i: [] for i in range(num_clusters)}
    for topic, cluster_label in zip(guidelines, clustering.labels_):
        clusters[cluster_label].append(topic)

    # Save clusters
    output_path = os.path.join(DATA_PATH, "gpt-4o-clusters")
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, "all_projects.json")
    with open(output_file, "w") as f:
        json.dump(clusters, f, indent=2)

def extract_guidelines(project_data):
    """
    Extract guidelines from project data, handling nested structures.
    """
    guidelines = []
    
    # Process CONTRIBUTING guidelines
    if "CONTRIBUTING" in project_data:
        for commit in project_data["CONTRIBUTING"].values():
            if "guidelines" not in commit:
                continue
            current_level = commit["guidelines"]
            while current_level:
                current_item = current_level.pop()
                if "guidelines" in current_item:
                    current_level.extend(current_item["guidelines"])
                    continue
                title = current_item.get("title", current_item.get("Title", ""))
                if title:
                    guidelines.append(title)

    # Process README guidelines
    if "README" in project_data:
        for commit in project_data["README"].values():
            if "guidelines" not in commit:
                continue
            current_level = commit["guidelines"]
            while current_level:
                current_item = current_level.pop()
                if "guidelines" in current_item:
                    current_level.extend(current_item["guidelines"])
                    continue
                title = current_item.get("title", current_item.get("Title", ""))
                if title:
                    guidelines.append(title)

    return guidelines

def main():
    """
    Main function to process and cluster guidelines from all projects.
    """
    # Download required NLTK data
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/wordnet')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading required NLTK data...")
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('stopwords')

    # Get list of projects
    projects = [name.removesuffix(".json") for name in os.listdir(OUTPUT_PATH)]
    print(f"Found {len(projects)} projects to process")

    # Collect all guidelines
    global_guidelines = []
    project_guidelines = {}

    for project in projects:
        print(f"Processing {project}...")
        try:
            with open(os.path.join(OUTPUT_PATH, f"{project}.json"), "r") as f:
                project_data = json.load(f)
            
            # Extract guidelines for this project
            project_guidelines[project] = extract_guidelines(project_data)
            global_guidelines.extend(project_guidelines[project])
            
        except Exception as e:
            print(f"Error processing {project}: {str(e)}")
            continue

    print(f"Total guidelines collected: {len(global_guidelines)}")
    
    # Cluster the guidelines
    cluster_guidelines(global_guidelines)

if __name__ == "__main__":
    main() 