import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load Data
data = pd.read_csv("sales_data.csv", parse_dates=["Date"])

# 2️⃣ Data Cleaning
data.dropna(inplace=True)
data["Revenue"] = data["Units_Sold"] * data["Price"]

# 3️⃣ Feature Extraction
data["Month"] = data["Date"].dt.to_period("M")

# 4️⃣ Insights with Pandas
monthly_revenue = data.groupby("Month")["Revenue"].sum()
top_products = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)

# 5️⃣ NumPy Example – Revenue Stats
revenue_array = np.array(data["Revenue"])
print("Average Revenue per Sale:", np.mean(revenue_array))
print("Revenue Std Deviation:", np.std(revenue_array))

# 6️⃣ Visualization
plt.figure(figsize=(10, 6))
sns.lineplot(x=monthly_revenue.index.astype(str), y=monthly_revenue.values)
plt.title("📈 Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.show()

# 7️⃣ Category Comparison
plt.figure(figsize=(8, 5))
sns.barplot(x="Category", y="Revenue", data=data, estimator=sum, ci=None)
plt.title("💰 Revenue by Category")
plt.show()
