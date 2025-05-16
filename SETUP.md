# Project Setup and Running Instructions

This document provides instructions for setting up and running the contribution guidelines analysis project.

## Prerequisites

- Python 3.11 or higher
- OpenAI API key (for GPT-4o access)
- Git
- GitHub REST API access token

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd guidelines
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the environment variables template and set up your configuration:
```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your credentials
# OPENAI_API_KEY=your-api-key-here
# OPENAI_MODEL=gpt-4o  # Using GPT-4o as specified in the paper
# GITHUB_TOKEN=your-github-token-here
```

## Running the Analysis

The project provides a main script that orchestrates all analysis steps. To run the complete analysis:

```bash
python main.py
```

This will execute all research questions in sequence:

1. RQ1: Prevalent Contribution Guidelines
   - Collects and processes guidelines using GPT-4o
   - Performs clustering and analysis
   - Generates visualizations

2. RQ2: PR Adherence to Guidelines
   - Processes PRs and analyzes adherence using GPT-4o
   - Generates results and statistics

3. RQ3: PR Acceptance Analysis
   - Analyzes PR acceptance patterns using statistical methods
   - Performs correlation analysis between guidelines and PR acceptance
   - Generates statistical results and insights

## Output Files

The analysis results will be stored in the following locations:

- Documentation files: `data/raw/`
- Extracted guidelines: `data/dumps/gpt-4o-guidelines/`
- PR data: `data/dumps/gpt-4o-commits/`
- Project metrics: `data/dumps/gpt-4o-metrics/`
- RQ1 results: `data/rq1/`
- RQ2 results: `data/rq2/`
- RQ3 results: `data/rq3/`

## Troubleshooting

### Common Issues

1. **OpenAI API Key Not Found**
   - Ensure the API key is properly set in your environment
   - Check if the key is valid and has sufficient credits

2. **GitHub API Rate Limits**
   - Ensure your GitHub token has appropriate permissions
   - Consider using a higher rate limit token for large datasets

3. **Missing Dependencies**
   - Verify all requirements are installed: `pip list`
   - Reinstall requirements if needed: `pip install -r requirements.txt`

4. **File Not Found Errors**
   - Ensure you're running scripts from the project root directory
   - Check if all required data files are present in the correct locations

### Getting Help

If you encounter any issues not covered here:
1. Check the error message for specific details
2. Review the relevant script's documentation
3. Open an issue in the project repository
