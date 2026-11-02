
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

PRODUCTS_FILE = PROCESSED_DIR / "products_cleaned.csv"
TRANSLATION_FILE = RAW_DIR / "product_category_name_translation.csv"
OUTPUT_FILE = PROCESSED_DIR / "products_with_english_categories.csv"

print("=" * 60)
print("PREPARING ENGLISH PRODUCT CATEGORIES")
print("=" * 60)

# Load the processed products and original translation table
products = pd.read_csv(PRODUCTS_FILE)
translations = pd.read_csv(TRANSLATION_FILE)

# Add English category names without removing original categories
df = products.merge(
    translations,
    on="product_category_name",
    how="left"
)

# Supply readable labels for the two untranslated categories
custom_translations = {
    "pc_gamer": "PC Gamer",
    "portateis_cozinha_e_preparadores_de_alimentos":
        "Portable Kitchen and Food Preparers",
}

df["product_category_name_english"] = (
    df["product_category_name_english"]
    .fillna(df["product_category_name"].map(custom_translations))
    .fillna("Unknown")
)

# Save the result separately
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print(f"Product rows: {len(df):,}")
print(
    "Missing English category labels: "
    f"{df['product_category_name_english'].isnull().sum()}"
)

print("\nExample category mappings:")
print(
    df[
        ["product_category_name", "product_category_name_english"]
    ]
    .drop_duplicates()
    .head(15)
    .to_string(index=False)
)

print(f"\nSaved to: {OUTPUT_FILE}")
print("Original datasets remain unchanged.")
print("\nCategory preparation completed.")
