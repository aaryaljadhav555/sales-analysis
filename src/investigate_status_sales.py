import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

ORDERS_FILE = RAW_DIR / "olist_orders_dataset.csv"
ITEMS_FILE = RAW_DIR / "olist_order_items_dataset.csv"

orders = pd.read_csv(ORDERS_FILE)
items = pd.read_csv(ITEMS_FILE)

print("=" * 60)
print("SALES BY ORDER STATUS")
print("=" * 60)

sales_data = items.merge(
    orders[["order_id", "order_status"]],
    on="order_id",
    how="left",
    validate="many_to_one"
)

status_summary = (
    sales_data.groupby("order_status")
    .agg(
        order_count=("order_id", "nunique"),
        item_count=("order_item_id", "count"),
        product_sales=("price", "sum"),
        freight_charges=("freight_value", "sum")
    )
    .sort_values("product_sales", ascending=False)
)

print("\n1. Sales and items by order status:")
print(status_summary.round(2).to_string())

print("\n2. Total product sales across all statuses:")
print(f"{sales_data['price'].sum():,.2f} BRL")

print("\n3. Total freight across all statuses:")
print(f"{sales_data['freight_value'].sum():,.2f} BRL")

print("\n4. Order item records without a matching order:")
print(f"{sales_data['order_status'].isna().sum():,}")

print("\nStatus sales investigation completed.")
