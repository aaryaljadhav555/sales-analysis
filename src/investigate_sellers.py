import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

SELLERS_FILE = RAW_DIR / "olist_sellers_dataset.csv"

sellers = pd.read_csv(SELLERS_FILE)

print("=" * 60)
print("SELLER DATA INVESTIGATION")
print("=" * 60)

print(f"\nTotal seller records: {len(sellers):,}")

print(
    f"Unique seller IDs: "
    f"{sellers['seller_id'].nunique():,}"
)

print("\n1. Missing values:")
print(sellers.isnull().sum().to_string())

print("\n2. Seller distribution by state:")
print(
    sellers["seller_state"]
    .value_counts()
    .to_string()
)

print("\n3. Top 10 seller cities:")
print(
    sellers["seller_city"]
    .value_counts()
    .head(10)
    .to_string()
)

print("\n4. Sample seller records:")
print(sellers.head(10).to_string(index=False))

print("\nSeller investigation completed.")