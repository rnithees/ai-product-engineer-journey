#dictionary
playzones = {
    "Kuddy Baba": 4.7,
    "Fun Park": 4.2,
    "Kiddo Zone": 4.6,
    "Adventure Zone": 4.4,
    "Happy Land": 4.5,
    "Playville": 4.4,
    "Playtopia": 4.3,
    "Wonderland": 4.6
}

total = 0

for playzone, rating in playzones.items():
    print(f"{playzone} rating: {rating}")
    total += rating

print(f"playzones.items(): {playzones.items()}")

average = total / len(playzones)
print((f"\nAverage rating: {average}"))

best_playzone = max(playzones, key=playzones.get)
print(f"\nHighest rated playzone: {best_playzone} - {playzones[best_playzone]}")
print(f"\nmax(playzones.values()): {max(playzones.values())}")

min_playzone = min(playzones, key=playzones.get)
print(f"\nLowest rated playzone: {min_playzone} - {playzones[min_playzone]}")
print(f"\nmin(playzones.values()): {min(playzones.values())}")


# set
# get all the ratings from the playzones and store them in a list
ratings = list(playzones.values())
# get all the playzone names from the playzones and store them in a list
playzone_names = list(playzones.keys())
print(f"\nRatings: {ratings}")
print(f"\nPlayzone Names: {playzone_names}")

unique_ratings = set(ratings)
print(f"\nUnique Ratings: {unique_ratings}")

# functions

def average_rating(rating_list):
    total = sum(rating_list)
    average = total / len(rating_list)
    return average

avg_rating = average_rating(ratings)
print(f"\nAverage Rating: {avg_rating}")

# mini challenge1
# Combine what we learned:
    # Create a list of dictionaries for 5 playzones with name and rating.
    # Use a function to calculate:
        # Average rating
        # Highest rated playzone
        # List of playzones with rating > 4.0
    # Convert ratings to a set to see unique ratings.
# copilot:disable-start
new_playzones = {
    "PZ 1": 4.5,
    "PZ 2": 4.1,
    "PZ 3": 3.2,
    "PZ 4": 3.3,
    "PZ 5": 4.4,
}

def calculate_avg_rating(ratings):
    total = sum(ratings)
    avg = total / len(ratings)
    return avg

def get_highest_rated_pz(playzones):
    return max(playzones, key=playzones.get)

def get_pz_above_4(playzones):
    return [pz for pz, rating in playzones.items() if rating > 4]

print(f"\nNew Playzones: {new_playzones}")
new_ratings = list(new_playzones.values())
avg_new_rating = calculate_avg_rating(new_ratings)
print(f"\nAverage Rating of New Playzones: {avg_new_rating}")
highest_rated_pz = get_highest_rated_pz(new_playzones)
print(f"\nHighest Rated Playzone: {highest_rated_pz} - {new_playzones[highest_rated_pz]}")
playzones_above_4 = get_pz_above_4(new_playzones)
print(f"\nPlayzones with rating above 4: {playzones_above_4}")
# copilot:disable-end


# mini challenge2
# Add weighted ratings for each playzone:
    # Weight = number of visitors
    # Compute weighted average instead of simple average
# copilot:disable-start
new_playzones2 = {
    "PZ 1": {"rating": 4.5, "visitors": 20},
    "PZ 2": {"rating": 4.1, "visitors": 80},
    "PZ 3": {"rating": 3.2, "visitors": 50},
    "PZ 4": {"rating": 3.3, "visitors": 40},
    "PZ 5": {"rating": 4.4, "visitors": 100},
}
def calculate_weighted_avg(playzones):
    total_weighted_rating = sum(pz["rating"] * pz["visitors"] for pz in playzones.values())
    total_visitors = sum(pz["visitors"] for pz in playzones.values())
    weighted_avg = total_weighted_rating / total_visitors
    return weighted_avg

def get_highest_rating_visitors_pz(playzones):
    return max(playzones, key=lambda pz: playzones[pz]["visitors"])

def get_highest_avg_rating_pz(playzones):
    return max(playzones, key=lambda pz: playzones[pz]["rating"])

def get_highest_weighted_rating_pz(playzones):
    return max(playzones, key=lambda pz: playzones[pz]["rating"] * playzones[pz]["visitors"])

weighted_avg_rating = calculate_weighted_avg(new_playzones2)
print(f"\nWeighted Average Rating: {weighted_avg_rating:.2f}")
highest_rating_visitors_pz = get_highest_rating_visitors_pz(new_playzones2)
print(f"\nHighest Rating Visitors Playzone: {highest_rating_visitors_pz} - {new_playzones2[highest_rating_visitors_pz]['visitors']}")
highest_avg_rated_pz = get_highest_avg_rating_pz(new_playzones2)
print(f"\nHighest Avg Rated Playzone: {highest_avg_rated_pz} - {new_playzones2[highest_avg_rated_pz]['rating']}")
highest_weighted_rated_pz = get_highest_weighted_rating_pz(new_playzones2)
print(f"\nHighest Weighted Rated Playzone: {highest_weighted_rated_pz} - {new_playzones2[highest_weighted_rated_pz]['rating'] * new_playzones2[highest_weighted_rated_pz]['visitors']}")
# copilot:disable-end