import pandas as pd
df = pd.read_csv("raw_data.csv")
df = df.drop_duplicates()
df["amount"] = df["amount"].fillna(df["amount"].mean())
df["date_of_birth"] = pd.to_datetime(df["date_of_birth"], errors='coerce')
df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors='coerce')
df["customer_age"] = 2026 - df["date_of_birth"].dt.year
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning completed successfully!")
