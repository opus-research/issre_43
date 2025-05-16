#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def run_rq1():
    """Run RQ1: Common Contribution Guidelines analysis"""
    print("\n🔍 Running RQ1: Common Contribution Guidelines")
    from scripts.rq1.guideline_collection import main as collect_guidelines
    from scripts.rq1.guideline_summarization import main as summarize_guidelines
    from scripts.rq1.process_guidelines import main as process_guidelines
    from scripts.rq1.rq1 import (
        cluster_guidelines,
        guideline_presence_by_project,
        compile_data_by_project,
        plot_grouped
    )

    print("📝 Step 1: Collecting guidelines from project documentation...")
    collect_guidelines()
    
    print("📊 Step 2: Summarizing collected guidelines...")
    summarize_guidelines()
    
    print("🔄 Step 3: Processing guidelines...")
    process_guidelines()
    
    print("🔍 Step 4: Clustering guidelines...")
    cluster_guidelines()
    
    print("📈 Step 5: Analyzing guideline presence by project...")
    guideline_presence_by_project()
    
    print("📊 Step 6: Compiling data by project...")
    compile_data_by_project()
    
    print("📊 Step 7: Generating plots...")
    plot_grouped()

def run_rq2():
    """Run RQ2: Guideline Evolution analysis"""
    print("\n🔍 Running RQ2: Guideline Evolution")
    
    print("📝 Step 1: Running RQ2 analysis...")
    from scripts.rq2.rq2 import main as run_rq2_analysis
    run_rq2_analysis()
    
    print("🔄 Step 2: Running RQ2 fixer...")
    from scripts.rq2.rq2_fixer import main as run_rq2_fixer
    run_rq2_fixer()
    
    print("📊 Step 3: Generating RQ2 results...")
    from scripts.rq2.rq2_results import main as run_rq2_results
    run_rq2_results()

def run_rq3():
    """Run RQ3: Project Success Correlation analysis"""
    print("\n🔍 Running RQ3: Project Success Correlation")
    
    print("📊 Running RQ3 analysis...")
    from scripts.rq3.rq3 import main as run_rq3_analysis
    run_rq3_analysis()

def main():
    """
    Main function to run all research questions in sequence.
    """
    print("🚀 Starting Research Analysis Pipeline")
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable is not set")
        print("Please set it in your .env file or environment")
        sys.exit(1)

    # Run each research question
    run_rq1()
    run_rq2()
    run_rq3()
    
    print("\n✅ Research Analysis Pipeline completed successfully!")

if __name__ == "__main__":
    main() 