import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

CUSTOMERS_FILE = RAW_DIR / "olist_customers_dataset.csv"

customers = pd.read_csv(CUSTOMERS_FILE)

print("=" * 60)
print("CUSTOMER DATA INVESTIGATION")
print("=" * 60)

print(f"\nTotal customer records: {len(customers):,}")

print(
    f"Unique customer IDs: "
    f"{customers['customer_id'].nunique():,}"
)

print(
    f"Unique customer unique IDs: "
    f"{customers['customer_unique_id'].nunique():,}"
)

print("\n1. Missing values:")
print(customers.isnull().sum().to_string())

print("\n2. Customer distribution by state:")
print(
    customers["customer_state"]
    .value_counts()
    .to_string()
)

print("\n3. Top 10 customer cities:")
print(
    customers["customer_city"]
    .value_counts()
    .head(10)
    .to_string()
)

print("\n4. Sample customer records:")
print(customers.head(10).to_string(index=False))

print("\nCustomer investigation completed.")