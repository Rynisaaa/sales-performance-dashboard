import pandas as pd
from pathlib import Path

source = Path("data/Sample - Superstore.csv")
target = Path("data/superstore_clean.csv")
df = pd.read_csv(source)
before = len(df)
df = df.drop_duplicates()
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
for col in ["Sales", "Profit", "Quantity", "Discount"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=["Order Date", "Order ID", "Region", "Category", "Sales", "Profit", "Quantity"])
df.to_csv(target, index=False)
print(f"Baris sebelum cleaning: {before:,}")
print(f"Baris setelah cleaning: {len(df):,}")
print(f"File tersimpan: {target}")
