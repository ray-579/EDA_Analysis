import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


os.makedirs("plots", exist_ok=True)


df = pd.read_csv('A:/train.csv')


df["Sales"] = df["Sales"].astype(str).str.replace("..", "", regex=False)
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")


df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)


print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())


plt.figure()
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")
plt.savefig("plots/sales_distribution.png")


plt.figure()
sns.barplot(x="Category", y="Sales", data=df, estimator=sum)
plt.title("Total Sales by Category")
plt.savefig("plots/sales_by_category.png")


plt.figure(figsize=(10,5))
sns.barplot(x="Sub-Category", y="Sales", data=df, estimator=sum)
plt.xticks(rotation=45)
plt.title("Sales by Sub-Category")
plt.savefig("plots/sales_by_subcategory.png")


plt.figure()
sns.barplot(x="Region", y="Sales", data=df, estimator=sum)
plt.title("Sales by Region")
plt.savefig("plots/sales_by_region.png")


df["Year"] = df["Order Date"].dt.year

plt.figure()
sns.lineplot(x="Year", y="Sales", data=df, estimator=sum)
plt.title("Sales Trend Over Years")
plt.savefig("plots/sales_trend.png")


plt.figure()
sns.barplot(x="Segment", y="Sales", data=df, estimator=sum)
plt.title("Sales by Segment")
plt.savefig("plots/sales_by_segment.png")


top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xticks(rotation=45)
plt.savefig("plots/top_products.png")

print("\nEDA Completed. Check 'plots' folder.")