import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# ===== CONFIGURATION =====
OUTPUT_DIR = "orders_data"
OUTPUT_FILE = "orders_aggregate.csv"           # change to .parquet if preferred
NUM_ROWS = 20_000_000                # ~1 GB as CSV
START_DATE = datetime(2000, 1, 1)
END_DATE = datetime(2024, 12, 31)

# ===== CREATE OUTPUT FOLDER =====
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===== HELPER FUNCTIONS =====
def random_dates(n, start, end):
    delta = end - start
    return [start + timedelta(days=np.random.randint(0, delta.days)) for _ in range(n)]

# ===== MAIN DATA GENERATION =====
def generate_orders(num_rows):
    print(f"Generating {num_rows:,} rows...")

    # --- Column data ---
    order_ids = np.arange(1, num_rows + 1)
    customer_ids = np.random.randint(1, 1_000_000, size=num_rows)
    #amounts = np.round(np.random.uniform(50, 5000, size=num_rows), 2)
    price = np.round(np.random.uniform(100, 200, size=num_rows), 2)
    order_dates = random_dates(num_rows, START_DATE, END_DATE)
    product_ids = np.random.randint(1, 99, size=num_rows)
    quantities = np.random.randint(1, 4, size=num_rows)
    statuses = np.random.choice(
        ["PLACED", "SHIPPED", "DELIVERED", "RETURNED", "CANCELLED"],
        size=num_rows,
        p=[0.35, 0.25, 0.25, 0.10, 0.05],
    )

    # --- State column ---
    states = np.random.choice(
        [
            "Andhra Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
            "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
            "Odisha", "Punjab", "Rajasthan", "Tamil Nadu", "Telangana",
            "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ],
        size=num_rows,
        p=None  # equal probability; you can bias this if you want
    )

    # --- Combine into DataFrame ---
    df = pd.DataFrame({
        "order_id": order_ids,
        "customer_id": customer_ids,
        "product_id" : product_ids,
        "price": price,
        "order_date": order_dates,
        "order_status": statuses,
        "state": states,
        "quantity" : quantities
    })

    return df

# ===== MAIN =====
if __name__ == "__main__":
    df = generate_orders(NUM_ROWS)
    print(df.head())

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    print(f"\nWriting data to: {output_path}")

    # Write as CSV
    df.to_csv(output_path, index=False, header=True)

    # Or, optionally as Parquet (smaller, faster for Spark)
    # df.to_parquet(output_path.replace(".csv", ".parquet"), index=False)

    print("Data generation complete!")
