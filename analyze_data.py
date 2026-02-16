import pandas as pd

# Load dataset
df = pd.read_csv("data/winemag-data_first150k.csv")

print("Dataset Loaded Successfully\n")

# Basic info
print("Shape of dataset:", df.shape)
print("\nColumns:\n", df.columns)

# Missing values
print("\nMissing values:\n", df.isnull().sum())

# Top countries
print("\nTop Wine Producing Countries:")
print(df['country'].value_counts().head(10))
