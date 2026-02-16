import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned_wine_data.csv")

sns.set(style="whitegrid")

# ===== 1. Price Distribution =====
plt.figure(figsize=(10,5))
sns.histplot(df['price'], bins=50, kde=True)
plt.title("Wine Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.savefig("price_distribution.png")
plt.close()


# ===== 2. Top Countries =====
plt.figure(figsize=(10,5))
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top Wine Producing Countries")
plt.xlabel("Number of Wines")
plt.savefig("top_countries.png")
plt.close()


# ===== 3. Rating vs Price =====
plt.figure(figsize=(10,5))
sns.scatterplot(x=df['price'], y=df['points'], alpha=0.3)
plt.title("Price vs Rating Relationship")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.savefig("price_vs_rating.png")
plt.close()


print("All visualizations generated successfully!")
