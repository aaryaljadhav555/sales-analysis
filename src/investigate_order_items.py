import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

ITEMS_FILE = RAW_DIR / "olist_order_items_dataset.csv"

items = pd.read_csv(ITEMS_FILE)

print("=" * 60)
print("ORDER ITEMS INVESTIGATION")
print("=" * 60)

print(f"\nTotal order item records: {len(items):,}")
print(f"Unique orders: {items['order_id'].nunique():,}")
print(f"Unique products: {items['product_id'].nunique():,}")
print(f"Unique sellers: {items['seller_id'].nunique():,}")

print("\n1. Missing values:")
print(items.isnull().sum().to_string())

print("\n2. Price summary:")
print(items["price"].describe().to_string())

print("\n3. Freight value summary:")
print(items["freight_value"].describe().to_string())

print("\n4. Total sales and freight:")

print(f"Total product sales: {items['price'].sum():,.2f}")
print(f"Total freight charges: {items['freight_value'].sum():,.2f}")
print(
    f"Total sales including freight: "
    f"{items['price'].sum() + items['freight_value'].sum():,.2f}"
)

print("\n5. Number of items per order:")

items_per_order = items.groupby("order_id").size()

print(f"Average items per order: {items_per_order.mean():.2f}")
print(f"Maximum items in one order: {items_per_order.max()}")

print("\n6. Sample records:")
print(items.head(10).to_string(index=False))

print("\nOrder items investigation completed.")