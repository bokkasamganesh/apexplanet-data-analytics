import pandas as pd
from pathlib import Path

# STEP 1: Load the dataset
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

# STEP 2: Display first 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# STEP 3: Display dataset shape
print("\nDATASET SHAPE:")
print(df.shape)

# STEP 4: Display column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# STEP 5: Display dataset information
print("\nDATASET INFORMATION:")
df.info()

# STEP 6: Check missing values
print("\nMISSING VALUES BY COLUMN:")
print(df.isnull().sum())

print("\nTOTAL MISSING VALUES:")
print(df.isnull().sum().sum())