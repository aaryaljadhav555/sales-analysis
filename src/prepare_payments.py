import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

INPUT_FILE = RAW_DIR / "olist_order_payments_dataset.csv"
OUTPUT_FILE = PROCESSED_DIR / "payments_cleaned.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load original payment data
payments = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("PAYMENT DATA PREPARATION")
print("=" * 50)

print(f"\nOriginal payment records: {len(payments):,}")
print(f"Duplicate rows: {payments.duplicated().sum():,}")
print(f"Missing values: {payments.isnull().sum().sum():,}")

print(f"Unique orders: {payments['order_id'].nunique():,}")

print("\nPayment methods:")
print(payments["payment_type"].value_counts().to_string())

print(
    "\nTotal recorded payment value: "
    f"R$ {payments['payment_value'].sum():,.2f}"
)

# Remove exact duplicate rows only
payments = payments.drop_duplicates()

# Save processed data
payments.to_csv(OUTPUT_FILE, index=False)

print(f"\nProcessed payment records: {len(payments):,}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nPayment preparation completed.")