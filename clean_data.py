import pandas as pd

print("--- 1. Loading the Dataset ---")

df = pd.read_csv('SuperMarket Analysis.csv')

print(df.head(3))

print("\n--- 2. Checking Dataset Info ---")
print(f"Total Rows & Columns: {df.shape}")
print(df.info())

print("\n--- 3. Checking for Missing Values ---")
print(df.isnull().sum())

print("\n--- 4. Cleaning & Formatting ---")
df['Date'] = pd.to_datetime(df['Date'])

df.columns = df.columns.str.strip()

print("\n--- 5. Saving Cleaned Data ---")
df.to_csv('cleaned_supermarket_sales.csv', index=False)
print("Success! Cleaned data saved as 'cleaned_supermarket_sales.csv'.")