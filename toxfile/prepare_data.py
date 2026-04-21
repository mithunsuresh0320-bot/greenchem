import pandas as pd

# Load dataset (your path is correct)
data = pd.read_csv(r"C:\Users\MITHUN\Desktop\greenchem\toxfile\tox21.csv")

# Drop rows with missing SMILES
data = data.dropna(subset=["smiles"])

# Remove non-numeric columns except smiles
tox_cols = data.drop(columns=["smiles"])

# Convert all to numeric
tox_cols = tox_cols.apply(pd.to_numeric, errors='coerce')

# Replace NaN with 0
tox_cols = tox_cols.fillna(0)

# Create label
data["green_score"] = (tox_cols.sum(axis=1) == 0).astype(int)

# Keep only needed columns
final_data = data[["smiles", "green_score"]]

# Save cleaned file
final_data.to_csv("cleaned_data.csv", index=False)

print("✅ Cleaned dataset saved!")