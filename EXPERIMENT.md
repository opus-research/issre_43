# Contribution Guidelines Analysis Experiment

This document describes the research experiment conducted to analyze contribution guidelines in open-source projects.

## Research Questions

1. **RQ1: What are the common contribution guidelines in open-source projects?**
   - Analyzes the presence and patterns of contribution guidelines across different programming languages
   - Identifies standardized guidelines and their adoption rates
   - Examines language-specific patterns in guideline implementation

2. **RQ2: How do contribution guidelines evolve over time?**
   - Tracks changes in guidelines across different project stages
   - Analyzes the evolution of guideline complexity and coverage
   - Identifies patterns in guideline adoption and modification

3. **RQ3: What is the relationship between contribution guidelines and project success?**
   - Correlates guideline presence with project metrics
   - Analyzes the impact of guidelines on project health
   - Examines the relationship between guideline quality and project success

## Project Structure

```
.
├── data/                      # All data files
│   ├── raw/                   # Original data files
│   │   ├── contributing.csv   # Initial dataset of projects
│   │   └── projects_by_language.json  # Project metadata
│   ├── dumps/                 # Centralized dump files
│   │   ├── gpt-4o-guidelines/ # Guidelines extracted by GPT-4
│   │   ├── gpt-4o-commits/    # Commit history analysis
│   │   └── gpt-4o-metrics/    # Project metrics analysis
│   ├── rq1/                   # RQ1-specific data
│   ├── rq2/                   # RQ2-specific data
│   └── rq3/                   # RQ3-specific data
├── scripts/                   # Analysis scripts
│   ├── rq1/                   # Scripts for RQ1
│   ├── rq2/                   # Scripts for RQ2
│   └── rq3/                   # Scripts for RQ3
└── prompts/                   # GPT prompts for analysis
```

## Research Process

### Data Collection and Processing Flow

1. **Initial Dataset Collection**
   - Start with `data/raw/projects_by_language.json` containing project metadata
   - Projects are categorized by programming language
   - This serves as the base dataset for analysis

2. **Documentation Collection**
   - For each project in the dataset:
     - Collect CONTRIBUTING.md files
     - Collect README.md files
   - Store raw documentation in `data/contributing_files/`

3. **Guideline Extraction**
   - Process each documentation file using GPT-4o
   - Extract structured guidelines from both CONTRIBUTING.md and README.md
   - Store extracted guidelines in `data/gpt-4o-guidelines/`
   - Each project's guidelines are stored in a JSON file named `{owner}-{repo}.json`

4. **Guideline Processing**
   - Text preprocessing:
     - Convert text to lowercase
     - Remove punctuation and special characters
     - Remove common English stopwords
     - Apply lemmatization to reduce words to their base form
   - Apply TF-IDF (Term Frequency-Inverse Document Frequency) algorithm:
     - Calculate term frequencies for each guideline
     - Compute inverse document frequency across all guidelines
     - Generate TF-IDF vectors for each guideline
     - Use these vectors to identify key terms and patterns
   - Prepare guidelines for clustering analysis:
     - Normalize vector representations
     - Remove duplicate guidelines based on semantic similarity
     - Standardize guideline formatting and structure

5. **Guideline Clustering**
   - Group similar guidelines using semantic analysis
   - Create clusters of related contribution guidelines
   - Store clustered guidelines for further analysis

6. **Guideline Summarization**
   - Use GPT-4 to analyze clustered guidelines
   - Create a standardized set of common guidelines
   - Document the mapping between original and standardized guidelines


## Prompts and Analysis Flow

### RQ1: Common Contribution Guidelines

1. **Guideline Collection Prompt** (`prompts/guideline_collection.txt`)
   - Purpose: Extract and structure guidelines from CONTRIBUTING.md and README.md files
   - Input: Raw documentation files
   - Output: Structured JSON with categorized guidelines
   - Order: First step in the analysis pipeline
   - Prompt:
   ```
   Read the following document, in triple quotes:

   """{doc}"""

   This document is part of the documentation for an open-source GitHub project. These documents often 
   contain instructions or rules (often called contribution guidelines) on how developers should 
   contribute to that specific open-source project.

   Summarize, in a JSON those contribution guidelines. Utilize the following template 
   {"guidelines": [{"title": "short title for the guideline, "description": "a description for that guideline"}}, ...]}.

   Regarding the information contained in each object in the JSON array: the title field should be a 
   short title describing the guideline, and the description should be a longer description of the
   guideline, and your reasoning for why it is considered a guideline.
   ```

2. **Guideline Clustering Prompt** (`prompts/openai_rq1.txt`)
   - Purpose: Group similar guidelines into standardized categories
   - Input: Extracted guidelines from step 1
   - Output: Clustered guidelines with standardized categories
   - Order: Second step, after guideline collection
   - Prompt:
   ```
   You will receive a JSON file containing clustered contribution guidelines for open source repositories. Each cluster groups guidelines that are similar in meaning or topic.

   Your task is to produce a refined, unified, and concise set of high-quality, general-purpose contribution guidelines. Follow these specific steps:

   ### Steps to Follow:

   1. **Normalize Casing and Remove Duplicates:**
      - Treat guidelines with varying casing as identical
      - Completely remove exact duplicates.

   2. **Merge Similar or Overlapping Sentences:**
      - Combine guidelines with clear semantic similarity
      - Examples:
        - "Be Respectful and Collaborative", "Be Respectful and Communicative" → "Code of Conduct"
        - "Automated Testing", "Automated Tests" → "Write Automated Tests"

   3. **Generalize or Rephrase Clearly:**
      - When merging terms, generalize or rephrase if necessary
      - Exclude overly broad single-word terms
      - Ensure no similar guidelines end up in "Miscellaneous"

   4. **Provide Explanations:**
      - Clearly explain each final guideline

   5. **Count and List Original Elements:**
      - List original elements merged into each guideline
      - Provide total count of original elements

   ### Output Structure:
   {
     "final_guidelines": [
       {"Guideline Name": "Clear and concise explanation..."},
       {"Another Guideline": "Another clear explanation..."}
     ],
     "cluster_mapping": {
       "Guideline Name": {
         "number_of_elements": 4,
         "elements": ["Original Element 1", "Original Element 2", ...]
       }
     }
   }
   ```

3. **Guideline Presence Analysis Prompt** (`prompts/openai_rq1_presence.txt`)
   - Purpose: Analyze the presence of standardized guidelines across projects
   - Input: Clustered guidelines
   - Output: Presence statistics and patterns
   - Order: Final step in RQ1 analysis
   - Prompt:
   ```
   You will receive:
   1. A list of standardized contribution guidelines, each with a short description.
   2. A dictionary of multiple projects. Each project contains a list of guidelines extracted from its CONTRIBUTING.md file.

   Your task:
   - For each project, go through the standardized list of guidelines.
   - For each guideline, check if it is present in the project's list of guidelines.
   - Use semantic understanding and synonyms where appropriate.
   - Return a JSON array where each item is an object with:
     - The project name (as a key)
     - A dictionary of standardized guideline names as keys, with values "yes" or "no"

   Only output the JSON array. Do not include explanations or additional text.
   ```

### RQ2: Guideline Adherence Analysis

1. **PR Adherence Analysis Prompt** (`prompts/openai_rq2.txt`)
   - Purpose: Evaluate PR compliance with contribution guidelines
   - Input: Pull request data and standardized guidelines
   - Output: Binary classification of guideline adherence
   - Order: First step in adherence analysis
   - Prompt:
   ```
   You are an assistant that checks multiple GitHub pull requests for compliance with contributing guidelines.

   You will receive:
   1. A list of contributing guidelines (each with a short description).
   2. A list of pull requests. Each pull request includes:
      - An ID or title
      - The pull request body
      - A string indicating the head branch which the pull request was created
      - A list of commit messages which composed the pull request
      - A list of comments from all users in the pull request

   Your task:
   - For each pull request, evaluate each guideline and determine if it is followed.
   - Use only the PR body, commit messages, head branch, and comments as context.
   - If you cannot confidently answer "yes", return "no".
   - Return a JSON array where each item represents a pull request, and includes:
     - The pull request ID
     - A dictionary mapping guideline titles to "yes" or "no"

   ### Output Format:
   [
     {
       "pull_request_id": "PR-101",
       "guideline_compliance": {
         "Add unit tests": "yes",
         "Write clear commit messages": "no",
         "Update documentation": "yes"
       }
     }
   ]
   ```

### RQ3: Project Success Correlation

1. **Metrics Collection Prompt**
   - Purpose: Extract relevant project success metrics
   - Input: Project metadata and activity data
   - Output: Structured project metrics
   - Order: First step in correlation analysis

2. **Correlation Analysis Prompt**
   - Purpose: Analyze relationship between guidelines and project success
   - Input: Project metrics and guideline presence data
   - Output: Correlation statistics and insights
   - Order: Final step in RQ3 analysis

