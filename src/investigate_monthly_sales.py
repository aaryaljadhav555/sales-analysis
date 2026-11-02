import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

ORDERS_FILE = RAW_DIR / "olist_orders_dataset.csv"
ITEMS_FILE = RAW_DIR / "olist_order_items_dataset.csv"

orders = pd.read_csv(ORDERS_FILE)
items = pd.read_csv(ITEMS_FILE)

print("=" * 60)
print("MONTHLY SALES INVESTIGATION")
print("=" * 60)

# Convert purchase timestamps into datetime values
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

# Join order items with their order purchase dates
sales_data = items.merge(
    orders[
        ["order_id", "order_purchase_timestamp", "order_status"]
    ],
    on="order_id",
    how="left",
    validate="many_to_one"
)

print(f"\nOrder item records after joining: {len(sales_data):,}")

print("\n1. Order status distribution:")
print(orders["order_status"].value_counts().to_string())

# Create a monthly period from the purchase timestamp
sales_data["month"] = (
    sales_data["order_purchase_timestamp"].dt.to_period("M")
)

# Calculate preliminary monthly product sales
monthly_sales = (
    sales_data.groupby("month")
    .agg(
        total_sales=("price", "sum"),
        items_sold=("order_item_id", "count"),
        unique_orders=("order_id", "nunique")
    )
    .sort_index()
)

print("\n2. Monthly sales (first 10 months):")
print(monthly_sales.head(10).round(2).to_string())

print("\n3. Monthly sales (last 10 months):")
print(monthly_sales.tail(10).round(2).to_string())

print("\n4. Total product sales across all months:")
print(f"{sales_data['price'].sum():,.2f} BRL")

print("\nMonthly sales investigation completed.")