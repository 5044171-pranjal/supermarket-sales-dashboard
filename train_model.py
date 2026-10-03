import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('cleaned_supermarket_sales.csv')

print("=== MACHINE LEARNING: SALES PREDICTION ===")

X = df[['Unit price', 'Quantity', 'cogs']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Evaluation Results:")
print(f"- Mean Squared Error (MSE): {mse:.4f}")
print(f"- R-squared Score: {r2:.4f} (Close to 1.0 means high accuracy!)")

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', lw=2)
plt.title('Actual Sales vs Predicted Sales (Linear Regression)')
plt.xlabel('Actual Sales ($)')
plt.ylabel('Predicted Sales ($)')
plt.tight_layout()
plt.savefig('model_results.png')
plt.close()

print("\nSuccess! Model trained and evaluation chart saved as 'model_results.png'.")