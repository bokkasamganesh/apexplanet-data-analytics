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


# STEP 7: Check duplicate records

print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# STEP 8: Remove duplicate records

before_count = len(df)

df = df.drop_duplicates()

after_count = len(df)

removed_count = before_count - after_count

print("\nDUPLICATE REMOVAL SUMMARY:")
print("Before removing duplicates:", before_count)
print("After removing duplicates:", after_count)
print("Total duplicates removed:", removed_count)



# STEP 9: Fix date data types

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nUPDATED DATA TYPES:")
print(df.dtypes)


# STEP 10: Convert categorical columns

categorical_columns = [
    "Ship Mode",
    "Segment",
    "Country",
    "Region",
    "Category",
    "Sub-Category"
]

for column in categorical_columns:
    df[column] = df[column].astype("category")

print("\nFINAL DATA TYPES:")
print(df.dtypes)

print("\nUPDATED MEMORY USAGE:")
print(df.memory_usage(deep=True).sum())