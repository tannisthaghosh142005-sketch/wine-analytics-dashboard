import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_wine_data.csv")

print("\n===== DATASET OVERVIEW =====")
print("Total Records:", len(df))
print("Average Price:", round(df['price'].mean(), 2))
print("Average Rating:", round(df['points'].mean(), 2))


print("\n===== TOP COUNTRIES BY PRODUCTION =====")
print(df['country'].value_counts().head(10))


print("\n===== MOST EXPENSIVE WINES =====")
top_expensive = df.sort_values(by="price", ascending=False).head(5)
print(top_expensive[['country', 'variety', 'price']])


print("\n===== BEST RATED WINES =====")
top_rated = df.sort_values(by="points", ascending=False).head(5)
print(top_rated[['country', 'variety', 'points']])


print("\n===== PRICE DISTRIBUTION =====")
print(df['price'].describe())


print("\n===== ANOMALY DETECTION =====")

# Simple anomaly detection: extremely expensive wines
threshold = df['price'].mean() + 3 * df['price'].std()
anomalies = df[df['price'] > threshold]

print("Number of price anomalies:", len(anomalies))
