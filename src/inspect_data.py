import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"

csv_files = sorted(DATA_DIR.glob("*.csv"))

print("\nSALES ANALYSIS - DATASET SUMMARY")
print("=" * 65)

if not csv_files:
    print("No CSV files found. Please check the data/raw folder.")
else:
    for file_path in csv_files:
        try:
            df = pd.read_csv(file_path)

            print(f"\nFile: {file_path.name}")
            print(f"Rows: {df.shape[0]:,}")
            print(f"Columns: {df.shape[1]}")
            print(f"Missing values: {df.isna().sum().sum():,}")

        except Exception as error:
            print(f"\nError reading {file_path.name}: {error}")

print("\nInspection completed.")