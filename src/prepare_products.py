
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = PROJECT_DIR / "data" / "raw" / "olist_products_dataset.csv"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "products_cleaned.csv"

print("=" * 60)
print("PREPARING PRODUCT DATA")
print("=" * 60)

# Read original product data
df = pd.read_csv(RAW_FILE)

print(f"Original product rows: {len(df):,}")

# Replace missing categories with Unknown
df["product_category_name"] = (
    df["product_category_name"].fillna("Unknown")
)

# Preserve missing measurements and descriptive fields
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Save processed data separately
df.to_csv(OUTPUT_FILE, index=False)

print(f"Processed product rows: {len(df):,}")
print(
    "Missing categories filled with Unknown: "
    f"{df['product_category_name'].eq('Unknown').sum():,}"
)
print(
    "Remaining missing values: "
    f"{df.isnull().sum().sum():,}"
)

print(f"\nSaved to: {OUTPUT_FILE}")
print("Original dataset remains unchanged.")
print("\nProduct preparation completed.")
