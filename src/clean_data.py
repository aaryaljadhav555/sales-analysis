import pandas as pd
from pathlib import Path

# Define project and dataset folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

# Find all CSV files
csv_files = sorted(RAW_DIR.glob("*.csv"))

print("=" * 65)
print("SALES ANALYSIS - DATA QUALITY CHECK")
print("=" * 65)

if not csv_files:
    print("No CSV files found. Check the data/raw folder.")
else:
    for file_path in csv_files:
        print(f"\nDataset: {file_path.name}")

        try:
            df = pd.read_csv(file_path)

            # Basic information
            print(f"Rows: {len(df):,}")
            print(f"Columns: {len(df.columns)}")

            # Count missing values
            missing = df.isnull().sum()
            total_missing = int(missing.sum())

            print(f"Total missing values: {total_missing:,}")

            if total_missing > 0:
                print("Columns with missing values:")
                print(missing[missing > 0].to_string())
            else:
                print("No missing values found.")

            # Count completely duplicated rows
            duplicates = int(df.duplicated().sum())
            print(f"Duplicate rows: {duplicates:,}")

        except Exception as error:
            print(f"Error reading dataset: {error}")

print("\nData quality check completed.")