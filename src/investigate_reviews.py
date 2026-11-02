import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

REVIEWS_FILE = RAW_DIR / "olist_order_reviews_dataset.csv"

reviews = pd.read_csv(REVIEWS_FILE)

print("=" * 60)
print("ORDER REVIEWS INVESTIGATION")
print("=" * 60)

print(f"\nTotal review records: {len(reviews):,}")

print(
    f"Unique review IDs: "
    f"{reviews['review_id'].nunique():,}"
)

print(
    f"Unique orders with reviews: "
    f"{reviews['order_id'].nunique():,}"
)

print("\n1. Missing values:")
print(reviews.isnull().sum().to_string())

print("\n2. Review score distribution:")
print(
    reviews["review_score"]
    .value_counts()
    .sort_index()
    .to_string()
)

print("\n3. Average review score:")
print(f"{reviews['review_score'].mean():.2f} / 5")

print("\n4. Review comment title availability:")
print(
    f"Non-missing titles: "
    f"{reviews['review_comment_title'].notna().sum():,}"
)

print(
    f"Missing titles: "
    f"{reviews['review_comment_title'].isna().sum():,}"
)

print("\n5. Review message availability:")
print(
    f"Non-missing messages: "
    f"{reviews['review_comment_message'].notna().sum():,}"
)

print(
    f"Missing messages: "
    f"{reviews['review_comment_message'].isna().sum():,}"
)

print("\n6. Sample review records:")
print(reviews.head(10).to_string(index=False))

print("\nReview investigation completed.")