import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_supermarket_sales.csv')

print("=== SUPERMARKET SALES ANALYSIS ===")

total_revenue = df['Sales'].sum()
print(f"1. Total Revenue across all branches: ${total_revenue:,.2f}")

revenue_by_product = df.groupby('Product line')['Sales'].sum().reset_index()
print("\n2. Revenue by Product Line:")
print(revenue_by_product.sort_values(by='Sales', ascending=False))

rating_by_branch = df.groupby('Branch')['Rating'].mean().reset_index()
print("\n3. Average Rating by Branch:")
print(rating_by_branch)

payment_counts = df['Payment'].value_counts()
print("\n4. Most Popular Payment Methods:")
print(payment_counts)

print("\nGenerating and saving charts...")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 5))
sns.barplot(data=revenue_by_product, x='Sales', y='Product line', palette='Blues_r')
plt.title('Total Revenue by Product Line')
plt.xlabel('Total Revenue ($)')
plt.ylabel('Product Line')
plt.tight_layout()
plt.savefig('revenue_by_product.png')
plt.close()

plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='Payment', palette='Set2')
plt.title('Usage Count of Payment Methods')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('payment_methods.png')
plt.close()

print("Success! Charts saved as 'revenue_by_product.png' and 'payment_methods.png'.")