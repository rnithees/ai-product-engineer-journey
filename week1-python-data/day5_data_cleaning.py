import pandas as pd

data = {
    "playzone": ["PZ1", "PZ2", "PZ3", "PZ4", "PZ5"],
    "rating": [4.5, None, 3.2, 3.3, 4.4],
    "visitors": [100, 150, None, 250, 300],
    "category": ["Indoor", "indoor", "Outdoor", None, "Indoor"]
}

df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nMissing Count:")
print(df.isnull().sum())

df["rating"] = df["rating"].fillna(df["rating"].mean())
df["visitors"] = df["visitors"].fillna(0)
df["category"] = df["category"].fillna("Unknown")

print("\nCleaned Data:")
print(df)

print("\nDuplicate Rows:")
print(df.duplicated())

print("\nData Types:")
print(df.dtypes)

df["visitors"] = df["visitors"].astype(int)

print("\nAfter Type Conversion:")
print(df.dtypes)

dirty = pd.Series(["100", "200", "unknown"])

clean = pd.to_numeric(dirty, errors="coerce")

print("\nSafe Numeric Conversion:")
print(clean)

print("\nUnique Categories:")
print(df["category"].unique())

df["category"] = df["category"].str.strip().str.lower()

print("\nClean Categories:")
print(df["category"].unique())