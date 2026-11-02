import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

ORDERS_FILE = RAW_DIR / "olist_orders_dataset.csv"

orders = pd.read_csv(ORDERS_FILE)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )

print("=" * 60)
print("DELIVERY DATA INVESTIGATION")
print("=" * 60)

print("\n1. Missing delivery dates by order status:")

print(
    orders.groupby("order_status")[
        [
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]
    ]
    .agg(lambda column: column.isna().sum())
    .to_string()
)

delivered = orders[orders["order_status"] == "delivered"].copy()

print("\n2. Delivered orders:")
print(f"Total delivered orders: {len(delivered):,}")

print(
    "Missing customer delivery dates: "
    f"{delivered['order_delivered_customer_date'].isna().sum():,}"
)

print("\n3. Delivery duration:")

valid_deliveries = delivered.dropna(
    subset=[
        "order_purchase_timestamp",
        "order_delivered_customer_date"
    ]
).copy()

valid_deliveries["delivery_days"] = (
    valid_deliveries["order_delivered_customer_date"]
    - valid_deliveries["order_purchase_timestamp"]
).dt.total_seconds() / 86400

print(
    "Average delivery time: "
    f"{valid_deliveries['delivery_days'].mean():.2f} days"
)

print(
    "Median delivery time: "
    f"{valid_deliveries['delivery_days'].median():.2f} days"
)

print("\n4. Estimated versus actual delivery:")

valid_estimates = valid_deliveries.dropna(
    subset=["order_estimated_delivery_date"]
)

valid_estimates["delivery_difference_days"] = (
    valid_estimates["order_delivered_customer_date"]
    - valid_estimates["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

print(
    "Orders delivered after estimated date: "
    f"{(valid_estimates['delivery_difference_days'] > 0).sum():,}"
)

print(
    "Orders delivered on or before estimated date: "
    f"{(valid_estimates['delivery_difference_days'] <= 0).sum():,}"
)

on_time_count = (
    valid_estimates["delivery_difference_days"] <= 0
).sum()

total_estimated_deliveries = len(valid_estimates)

on_time_percentage = (
    on_time_count / total_estimated_deliveries
) * 100

print("\n5. On-time delivery performance:")
print(f"Valid deliveries evaluated: {total_estimated_deliveries:,}")
print(f"On-time delivery percentage: {on_time_percentage:.2f}%")

print("\nDelivery investigation completed.")