import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "olist_products_dataset.csv"

df = pd.read_csv(DATA_FILE)

print("=" * 60)
print("PRODUCT DATA INVESTIGATION")
print("=" * 60)

print(f"\nTotal products: {len(df):,}")

print("\n1. Missing values by column:")
print(df.isnull().sum().to_string())

print("\n2. Products with missing category:")

missing_category = df[df["product_category_name"].isnull()]

print(f"Number of products: {len(missing_category)}")
print(missing_category.head(10).to_string(index=False))

print("\n3. Products with missing weight:")

missing_weight = df[df["product_weight_g"].isnull()]

print(f"Number of products: {len(missing_weight)}")
print(missing_weight.to_string(index=False))

print("\n4. Products with missing dimensions:")

dimension_columns = [
    "product_length_cm",
    "product_height_cm",
    "product_width_cm",
]

missing_dimensions = df[df[dimension_columns].isnull().any(axis=1)]

print(f"Number of products: {len(missing_dimensions)}")
print(missing_dimensions.to_string(index=False))

print("\nProduct investigation completed.")