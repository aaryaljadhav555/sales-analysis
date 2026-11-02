
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "raw" / "olist_orders_dataset.csv"

df = pd.read_csv(DATA_FILE)

print("=" * 60)
print("ORDER STATUS INVESTIGATION")
print("=" * 60)

# Count orders by status
print("\n1. Orders by status:")
print(df["order_status"].value_counts().to_string())

# Check missing values in each column
print("\n2. Missing values by column:")
print(df.isnull().sum().to_string())

# Investigate missing dates by order status
date_columns = [
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
]

print("\n3. Missing dates by order status:")

for column in date_columns:
    print(f"\n{column}:")
    result = (
        df.groupby("order_status")[column]
        .apply(lambda values: values.isnull().sum())
    )
    print(result.to_string())

# Show a few orders with missing delivery dates
print("\n4. Sample orders with missing delivery dates:")

missing_delivery = df[
    df["order_delivered_customer_date"].isnull()
]

print(
    missing_delivery[
        ["order_id", "order_status", "order_purchase_timestamp",
         "order_delivered_customer_date"]
    ].head(10).to_string(index=False)
)

print("\nInvestigation completed.")

print("\n" + "=" * 60)
print("DELIVERED ORDERS WITH MISSING DELIVERY DATES")
print("=" * 60)

delivered_missing_dates = df[
    (df["order_status"] == "delivered")
    & (df["order_delivered_customer_date"].isnull())
]

columns_to_show = [
    "order_id",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

print(f"Number of affected orders: {len(delivered_missing_dates)}")

print(
    delivered_missing_dates[columns_to_show]
    .to_string(index=False)
)
