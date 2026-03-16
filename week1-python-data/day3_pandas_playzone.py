import pandas as pd

data = {
    "playzone": ["PZ1", "PZ2", "PZ3", "PZ4", "PZ5"],
    "rating": [4.5, 4.1, 3.2, 3.3, 4.4],
    "visitors": [100, 150, 200, 250, 300]
}

df = pd.DataFrame(data)

print(df)

print(df["rating"])

print("Average:", df["rating"].mean())

print("Max:", df["rating"].max())
print("Min:", df["rating"].min())

print("Standard Deviation:", df["rating"].std())
print("Normalized Ratings:\n",(df["rating"] - df["rating"].mean()) / df["rating"].std())

print("Weighted Rating:", (df["rating"] * df["visitors"]).sum() / df["visitors"].sum())

print("Difference from average:\n", df["rating"] - df["rating"].mean())

print("Top ratings only:\n", df["rating"] > 4.0)
print("Top ratings:\n", df[df["rating"] > 4.0])
print("Top rating playzone:", df.loc[df["rating"].idxmax(), "playzone"])

sorted_df = df.sort_values(by="rating", ascending=False)

print(sorted_df)

print(df.describe())

df["weighted_score"] = df["rating"] * df["visitors"]
df["rating_category"] = df["rating"].apply(lambda x: "High" if x > 4 else "Normal")
print(df)