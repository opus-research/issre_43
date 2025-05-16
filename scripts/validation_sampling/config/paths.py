import os

# Project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
PR_DIR = os.path.join(DATA_DIR, 'pull_requests')
RESULTS_DIR = os.path.join(PROJECT_ROOT, 'results')

# Input files
PROJECTS_FILE = os.path.join(DATA_DIR, 'projects_by_language.json')
GUIDELINE_PRESENCE_FILE = os.path.join(RESULTS_DIR, 'rq1', 'guideline_presence_by_project.json')

# Output files
SAMPLES_DIR = os.path.join(BASE_DIR, 'data', 'samples')
PR_SAMPLE_CSV = os.path.join(SAMPLES_DIR, 'pull_requests_sample.csv')
PR_SAMPLE_JSON = os.path.join(SAMPLES_DIR, 'random_prs_with_comments.json')
MD_FILES_JSON = os.path.join(SAMPLES_DIR, 'random_readme_contributing_files.json')
MD_URLS_JSON = os.path.join(SAMPLES_DIR, 'markdown_files_urls.json')
MD_URLS_CHECKED_JSON = os.path.join(SAMPLES_DIR, 'markdown_files_urls_checked.json')
MANUAL_VALIDATION_XLSX = os.path.join(RESULTS_DIR, 'Manual Validation.xlsx')

# Sampling parameters
NUM_PRS = 200
MAX_MD_FILES = 150
TARGET_FILES_PER_LANGUAGE = 50

# GitHub API settings
GITHUB_HEADERS = {
    "User-Agent": "GuidelineValidator/1.0",
    "Accept": "application/vnd.github.v3+json"
} 