import numpy as np

ratings = np.array([4.5, 4.1, 3.2, 3.3, 4.4, ])

print("Ratings:", ratings)
print("Average:", np.mean(ratings))
print("Highest:", np.max(ratings))
print("Lowest:", np.min(ratings))

scaled = ratings * 10

print("Scaled Ratings:", scaled)

visitors = np.array([100, 150, 200, 250, 300])

weighted = ratings * visitors
weighted_avg = np.sum(weighted) / np.sum(visitors)
print("Ratings:", ratings)
print("Visitors:", visitors)
print("Weighted Rating:", weighted)
print("Weighted Average:", weighted_avg)

print("Difference from average:", ratings - np.mean(ratings))

print("Standard Deviation:", np.std(ratings))
ratings2 = np.array([1.0, 5.0, 2.0, 5.0, 6.7])
print("Ratings2 average:", np.mean(ratings2))
print("Standard Deviation:", np.std(np.array(ratings2)))

normalized = (ratings - np.mean(ratings)) / np.std(ratings)
print("Normalized Ratings:", normalized)