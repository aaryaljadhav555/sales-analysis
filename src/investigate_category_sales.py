import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"
RAW_DIR = PROJECT_DIR / "data" / "raw"

PRODUCTS_FILE = (
    PROCESSED_DIR / "products_with_english_categories.csv"
)
ITEMS_FILE = RAW_DIR / "olist_order_items_dataset.csv"

products = pd.read_csv(PRODUCTS_FILE)
items = pd.read_csv(ITEMS_FILE)

print("=" * 60)
print("PRODUCT CATEGORY INVESTIGATION")
print("=" * 60)

print(f"\nTotal products: {len(products):,}")
print(f"Unique product IDs: {products['product_id'].nunique():,}")

print("\n1. Products by category (top 15):")

print(
    products["product_category_name_english"]
    .value_counts()
    .head(15)
    .to_string()
)

print("\n2. Joining products with order items...")

product_sales = items.merge(
    products[
        ["product_id", "product_category_name_english"]
    ],
    on="product_id",
    how="left",
    validate="many_to_one"
)

print(f"Order item records after joining: {len(product_sales):,}")

print("\n3. Top 15 categories by product sales:")

category_sales = (
    product_sales.groupby("product_category_name_english")
    .agg(
        total_sales=("price", "sum"),
        items_sold=("order_item_id", "count")
    )
    .sort_values("total_sales", ascending=False)
)

print(category_sales.head(15).round(2).to_string())

print("\n4. Product category investigation completed.")