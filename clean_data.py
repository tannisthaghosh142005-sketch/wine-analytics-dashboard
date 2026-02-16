import pandas as pd

# Load dataset
df = pd.read_csv("data/winemag-data_first150k.csv")

print("Original Shape:", df.shape)

# Remove useless column
df.drop(columns=["Unnamed: 0"], inplace=True)

# Handle missing values
df['price'].fillna(df['price'].median(), inplace=True)
df['country'].fillna("Unknown", inplace=True)
df['province'].fillna("Unknown", inplace=True)

# Drop columns with too many missing values
df.drop(columns=["designation", "region_2"], inplace=True)

# Remove remaining rows with missing critical data
df.dropna(inplace=True)

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_wine_data.csv", index=False)

print("Clean dataset saved successfully!")
