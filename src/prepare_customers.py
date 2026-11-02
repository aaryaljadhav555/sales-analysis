import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

INPUT_FILE = RAW_DIR / "olist_customers_dataset.csv"
OUTPUT_FILE = PROCESSED_DIR / "customers_cleaned.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load original customer data
customers = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("CUSTOMER DATA PREPARATION")
print("=" * 50)

print(f"\nOriginal customer records: {len(customers):,}")
print(f"Duplicate rows: {customers.duplicated().sum():,}")
print(f"Missing values: {customers.isnull().sum().sum():,}")

# Check unique customer identifiers
print(
    "Unique customer IDs:",
    customers["customer_id"].nunique()
)

print(
    "Unique customer identities:",
    customers["customer_unique_id"].nunique()
)

# Save the processed copy without modifying the original
customers.to_csv(OUTPUT_FILE, index=False)

print(f"\nProcessed customer records: {len(customers):,}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nCustomer preparation completed.")