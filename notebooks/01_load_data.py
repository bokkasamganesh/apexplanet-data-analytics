
import pandas as pd
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Define dataset path
file_path = BASE_DIR / "data" / "Sample - Superstore.csv"

# Load dataset
df = pd.read_csv(file_path, encoding="latin1")

# Display first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Dataset shape
print("\nDATASET SHAPE:")
print(df.shape)

# Column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Dataset information
print("\nDATASET INFORMATION:")
df.info()
