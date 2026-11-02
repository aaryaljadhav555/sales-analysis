import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

ORDERS_FILE = RAW_DIR / "olist_orders_dataset.csv"
OUTPUT_FILE = PROCESSED_DIR / "orders_cleaned.csv"

# Create the processed directory if needed
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load the original orders dataset
orders = pd.read_csv(ORDERS_FILE)

print("Original orders:", len(orders))

# Convert date columns to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )

# Check for duplicate rows
duplicate_count = orders.duplicated().sum()

print("Duplicate rows found:", duplicate_count)

# Remove exact duplicate rows only
orders = orders.drop_duplicates()

# Check missing values after date conversion
print("\nMissing values:")
print(orders.isnull().sum().to_string())

# Save the cleaned dataset
orders.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned orders:", len(orders))
print("Saved to:", OUTPUT_FILE)
print("\nOrders preparation completed.")