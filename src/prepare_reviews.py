import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

INPUT_FILE = RAW_DIR / "olist_order_reviews_dataset.csv"
OUTPUT_FILE = PROCESSED_DIR / "reviews_cleaned.csv"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load original reviews
reviews = pd.read_csv(INPUT_FILE)

print("=" * 50)
print("REVIEW DATA PREPARATION")
print("=" * 50)

print(f"\nOriginal review records: {len(reviews):,}")
print(f"Duplicate rows: {reviews.duplicated().sum():,}")

print("\nMissing values by column:")
print(reviews.isnull().sum().to_string())

print("\nReview score distribution:")
print(reviews["review_score"].value_counts().sort_index().to_string())

print(
    f"\nAverage review score: "
    f"{reviews['review_score'].mean():.2f} / 5"
)

print(f"Unique review IDs: {reviews['review_id'].nunique():,}")
print(f"Unique orders reviewed: {reviews['order_id'].nunique():,}")

# Remove exact duplicate rows only
reviews = reviews.drop_duplicates()

# Save processed data
reviews.to_csv(OUTPUT_FILE, index=False)

print(f"\nProcessed review records: {len(reviews):,}")
print(f"Saved to: {OUTPUT_FILE}")
print("\nReview preparation completed.")
