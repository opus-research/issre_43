import pandas as pd
import numpy as np

def normalize(val):
    val = str(val).strip().upper()
    if val in ["YES", "TRUE"]:
        return True
    if val in ["NO", "FALSE"]:
        return False
    return val

# Read the CSV files
oracle = pd.read_csv('results/contributing_fixed.csv')
validation = pd.read_csv('results/guideline_presence.csv')

# Get the columns to compare (excluding Language and Contribution Guideline File)
columns_to_compare = oracle.columns[2:]

# Initialize counters
total_cells = 0
matching_cells = 0
mismatches = []

# Compare each row
for idx, row in oracle.iterrows():
    # Find matching row in validation
    val_row = validation[validation['Contribution Guideline File'] == row['Contribution Guideline File']]
    
    if len(val_row) > 0:
        for col in columns_to_compare:
            total_cells += 1
            oracle_val = normalize(row[col])
            validation_val = normalize(val_row[col].values[0])
            if oracle_val == validation_val:
                matching_cells += 1
            else:
                if len(mismatches) < 5:
                    mismatches.append((row['Contribution Guideline File'], col, row[col], val_row[col].values[0]))

# Calculate accuracy
accuracy = (matching_cells / total_cells) * 100 if total_cells > 0 else 0

print(f"Total cells compared: {total_cells}")
print(f"Matching cells: {matching_cells}")
print(f"Accuracy: {accuracy:.2f}%")

if mismatches:
    print("\nFirst 5 mismatches:")
    for m in mismatches:
        print(f"File: {m[0]}, Column: {m[1]}, Oracle: {m[2]}, Validation: {m[3]}")

# Calculate accuracy per column
print("\nAccuracy per column:")
for col in columns_to_compare:
    matches = 0
    total = 0
    for idx, row in oracle.iterrows():
        val_row = validation[validation['Contribution Guideline File'] == row['Contribution Guideline File']]
        if len(val_row) > 0:
            total += 1
            oracle_val = normalize(row[col])
            validation_val = normalize(val_row[col].values[0])
            if oracle_val == validation_val:
                matches += 1
    col_accuracy = (matches / total) * 100 if total > 0 else 0
    print(f"{col}: {col_accuracy:.2f}%") 