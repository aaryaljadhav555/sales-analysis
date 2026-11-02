import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"

# Load the geolocation dataset
file_path = DATA_DIR / "olist_geolocation_dataset.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("GEOLOCATION DUPLICATE INVESTIGATION")
print("=" * 60)

print(f"Total rows: {len(df):,}")

# Check exact duplicate rows across all columns
exact_duplicates = df.duplicated().sum()
print(f"Exact duplicate rows: {exact_duplicates:,}")

# Check repeated ZIP code prefixes
repeated_zip_rows = df.duplicated(
    subset=["geolocation_zip_code_prefix"]
).sum()

print(f"Rows with a previously seen ZIP prefix: {repeated_zip_rows:,}")

# Display examples of exact duplicates
print("\nExamples of exact duplicate rows:")

duplicate_examples = df[df.duplicated(keep=False)]

if duplicate_examples.empty:
    print("No exact duplicate rows found.")
else:
    print(duplicate_examples.head(10).to_string(index=False))

print("\nInvestigation completed.")
print("\n" + "=" * 60)
print("UNIQUE ZIP CODE ANALYSIS")
print("=" * 60)

unique_zip_codes = df["geolocation_zip_code_prefix"].nunique()

print(f"Total rows: {len(df):,}")
print(f"Unique ZIP prefixes: {unique_zip_codes:,}")
print(
    f"Average rows per ZIP prefix: "
    f"{len(df) / unique_zip_codes:.2f}"
)

print("\nTop 10 ZIP prefixes by number of records:")

zip_counts = (
    df["geolocation_zip_code_prefix"]
    .value_counts()
    .head(10)
)

print(zip_counts.to_string())