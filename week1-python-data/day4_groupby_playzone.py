import pandas as pd

data = {
    "playzone": ["PZ1", "PZ2", "PZ3", "PZ4", "PZ5"],
    "rating": [4.5, 4.1, 3.2, 3.3, 4.4],
    "visitors": [100, 150, 200, 250, 300],
    "category": ["Indoor", "Indoor", "Outdoor", "Outdoor", "Indoor"]
}

df = pd.DataFrame(data)

print("\nFull Data:")
print(df)

grouped = df.groupby("category")["rating"].mean()

print("\nAverage Rating by Category:")
print(grouped)

visitorsAvgByCat = df.groupby("category")["visitors"].mean()

print("\nAverage Visitors by Category:")
print(visitorsAvgByCat)

summary = df.groupby("category").agg({
    "rating": "mean",
    "visitors": "sum"
})

print("\nCategory Summary:")
print(summary)

aggregatedSummary = df.groupby("category").agg({
    "rating": ["mean", "max", "min"],
    "visitors": ["sum", "count"]
})
print("\nCategory Summary:")
print(aggregatedSummary)

print("\nCategory Sort Values:")
print(aggregatedSummary["rating", "mean"].sort_values(ascending=True))

df["weighted_rating"] = df["rating"] * df["visitors"]
print("\nFeature created DF:")
print(df)

high_rating = aggregatedSummary[aggregatedSummary["rating"]["mean"] > 4]
print("\nhigh_rating:")
print(high_rating)

summaryWithWeightedRatingAgg = df.groupby("category").agg({
    "rating": "mean",
    "visitors": "sum",
    "weighted_rating": "mean"
})
print("\nsummaryWithWeightedRatingAgg:")
print(summaryWithWeightedRatingAgg)

print("\n Sorted categories by weighted rating:")
print(summaryWithWeightedRatingAgg["weighted_rating"].sort_values(ascending=False))

category_summary = df.groupby("category").apply(
    lambda x: x["weighted_rating"].sum() / x["visitors"].sum()
)
print("\n Category summary:")
print(category_summary)

summaryWithWeightedRatingAgg["true_weighted_rating"] = df.groupby("category").apply(
    lambda x: x["weighted_rating"].sum() / x["visitors"].sum()
)

print("\nsummaryWithWeightedRatingAgg with true weighted rating:")
print(summaryWithWeightedRatingAgg)