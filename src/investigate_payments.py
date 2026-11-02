import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

PAYMENTS_FILE = RAW_DIR / "olist_order_payments_dataset.csv"
ORDERS_FILE = RAW_DIR / "olist_orders_dataset.csv"

payments = pd.read_csv(PAYMENTS_FILE)
orders = pd.read_csv(ORDERS_FILE)

print("=" * 60)
print("ORDER PAYMENT INVESTIGATION")
print("=" * 60)

print(f"\nPayment records: {len(payments):,}")
print(f"Orders: {len(orders):,}")

print("\n1. Payment types:")
print(payments["payment_type"].value_counts().to_string())

print("\n2. Payment value summary:")
print(payments["payment_value"].describe().to_string())

print("\n3. Orders with multiple payment records:")

payment_counts = payments.groupby("order_id").size()

print(f"Unique orders in payments: {payment_counts.size:,}")
print(f"Orders with multiple payment records: {(payment_counts > 1).sum():,}")
print(f"Maximum payment records for one order: {payment_counts.max()}")

print("\n4. Payment value examples:")
print(
    payments[
        ["order_id", "payment_sequential", "payment_type", "payment_value"]
    ]
    .head(10)
    .to_string(index=False)
)

print("\n5. Orders without a payment record:")

payment_order_ids = set(payments["order_id"])
order_ids = set(orders["order_id"])

print(f"Orders without payment records: {len(order_ids - payment_order_ids):,}")

print("\nPayment investigation completed.")