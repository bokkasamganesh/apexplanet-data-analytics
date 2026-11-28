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



# STEP 11: Detect outliers using IQR method

columns = ["Sales", "Profit", "Discount"]

for column in columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\nOutlier analysis for {column}:")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Number of Outliers:", len(outliers))



    # STEP 12: Inspect potential outliers

for column in columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\nOUTLIER DETAILS: {column}")
    print("Minimum value:", df[column].min())
    print("Maximum value:", df[column].max())
    print("First 5 outlier values:")
    print(outliers[column].head())



    # STEP 13: Handle potential outliers

# IQR method was used to identify potential outliers
# Sales, Profit, and Discount were inspected.
# These values may represent genuine business transactions.
# Therefore, no rows were removed or capped.

print("\nOutlier handling completed.")
print("No valid business transactions were removed.")
print("Final dataset shape:", df.shape)



# STEP 14: Save cleaned dataset

output_file = BASE_DIR / "data" / "cleaned_superstore.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("File location:", output_file)




# STEP 15: Statistical Summary

print("\n========== DATASET INFORMATION ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== CATEGORICAL SUMMARY ==========")
print(df.describe(include="category"))