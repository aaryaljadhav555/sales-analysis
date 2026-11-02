import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

INPUT_FILE = RAW_DIR / "product_category_name_translation.csv"
OUTPUT_FILE = PROCESSED_DIR / "category_translation_cleaned.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load original category translations
categories = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("CATEGORY TRANSLATION PREPARATION")
print("=" * 50)

print(f"\nOriginal category records: {len(categories):,}")
print(f"Duplicate rows: {categories.duplicated().sum():,}")
print(f"Missing values: {categories.isnull().sum().sum():,}")
print(
    "Unique Portuguese categories:",
    categories["product_category_name"].nunique()
)
print(
    "Unique English categories:",
    categories["product_category_name_english"].nunique()
)

# Remove exact duplicate rows only
categories = categories.drop_duplicates()

# Save processed data
categories.to_csv(OUTPUT_FILE, index=False)

print(f"\nProcessed category records: {len(categories):,}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nCategory translation preparation completed.")