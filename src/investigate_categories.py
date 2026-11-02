
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

products_file = RAW_DIR / "olist_products_dataset.csv"
translation_file = RAW_DIR / "product_category_name_translation.csv"

products = pd.read_csv(products_file)
translations = pd.read_csv(translation_file)

print("=" * 60)
print("PRODUCT CATEGORY INVESTIGATION")
print("=" * 60)

print(f"\nUnique categories in products: {products['product_category_name'].nunique()}")
print(f"Categories in translation file: {len(translations)}")

print("\nTranslation file columns:")
print(translations.columns.tolist())

print("\nFirst 10 category translations:")
print(translations.head(10).to_string(index=False))

# Find product categories that have no English translation
product_categories = set(
    products["product_category_name"].dropna().unique()
)

translated_categories = set(
    translations["product_category_name"].dropna().unique()
)

missing_translations = product_categories - translated_categories

print(f"\nCategories without English translations: {len(missing_translations)}")
print(sorted(missing_translations))

print("\nCategory investigation completed.")
