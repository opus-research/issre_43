import json
import pandas as pd
from config.paths import GUIDELINE_PRESENCE_FILE, MANUAL_VALIDATION_XLSX

def update_validation_xlsx():
    """Update the manual validation Excel file with guideline presence data."""
    # Load guideline presence data
    with open(GUIDELINE_PRESENCE_FILE, 'r') as f:
        guideline_data = json.load(f)

    # Convert to DataFrame
    rows = []
    for project_data in guideline_data:
        for project, guidelines in project_data.items():
            row = {'Project': project}
            row.update(guidelines)
            rows.append(row)
    df = pd.DataFrame(rows)

    # Create a new DataFrame with the correct structure
    new_df = pd.DataFrame(columns=['Project'] + list(df.columns[1:]))

    # Add the guideline presence data
    for _, row in df.iterrows():
        new_df = pd.concat([new_df, pd.DataFrame([row])], ignore_index=True)

    # Save the new DataFrame to XLSX
    new_df.to_excel(MANUAL_VALIDATION_XLSX, index=False)
    print(f"Created new XLSX file at {MANUAL_VALIDATION_XLSX} with guideline presence data.")

if __name__ == '__main__':
    update_validation_xlsx() 