import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

INPUT_FILE = RAW_DIR / "olist_sellers_dataset.csv"
OUTPUT_FILE = PROCESSED_DIR / "sellers_cleaned.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load original seller data
sellers = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("SELLER DATA PREPARATION")
print("=" * 50)

print(f"\nOriginal seller records: {len(sellers):,}")
print(f"Duplicate rows: {sellers.duplicated().sum():,}")
print(f"Missing values: {sellers.isnull().sum().sum():,}")
print(f"Unique seller IDs: {sellers['seller_id'].nunique():,}")

# Remove exact duplicate rows, if any
sellers = sellers.drop_duplicates()

# Save the processed copy
sellers.to_csv(OUTPUT_FILE, index=False)

print(f"\nProcessed seller records: {len(sellers):,}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nSeller preparation completed.")