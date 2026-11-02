import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

INPUT_FILE = RAW_DIR / "olist_order_items_dataset.csv"
OUTPUT_FILE = PROCESSED_DIR / "order_items_cleaned.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load original order items
items = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("ORDER ITEMS DATA PREPARATION")
print("=" * 50)

print(f"\nOriginal item records: {len(items):,}")
print(f"Duplicate rows: {items.duplicated().sum():,}")
print(f"Missing values: {items.isnull().sum().sum():,}")

# Check important identifiers
print(f"Unique orders: {items['order_id'].nunique():,}")
print(f"Unique products: {items['product_id'].nunique():,}")
print(f"Unique sellers: {items['seller_id'].nunique():,}")

# Check sales values
print(f"\nTotal product sales: R$ {items['price'].sum():,.2f}")
print(f"Total freight charges: R$ {items['freight_value'].sum():,.2f}")

# Remove exact duplicate rows, if any
items = items.drop_duplicates()

# Save the processed dataset
items.to_csv(OUTPUT_FILE, index=False)

print(f"\nProcessed item records: {len(items):,}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nOrder items preparation completed.")