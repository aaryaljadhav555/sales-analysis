import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = PROJECT_DIR / "data" / "raw" / "olist_geolocation_dataset.csv"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "geolocation_cleaned.csv"

print("=" * 60)
print("PREPARING GEOLOCATION DATA")
print("=" * 60)

# Read the original dataset
df = pd.read_csv(RAW_FILE)

print(f"Original rows: {len(df):,}")

# Remove only rows identical across all columns
cleaned_df = df.drop_duplicates().copy()

print(f"Rows after removing exact duplicates: {len(cleaned_df):,}")
print(f"Exact duplicate rows removed: {len(df) - len(cleaned_df):,}")

# Create the output directory if necessary
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Save the cleaned dataset separately
cleaned_df.to_csv(OUTPUT_FILE, index=False)

print(f"\nCleaned dataset saved to: {OUTPUT_FILE}")
print("Original dataset remains unchanged.")
print("\nGeolocation preparation completed.")