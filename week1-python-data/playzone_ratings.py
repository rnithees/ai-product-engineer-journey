playzones = {
    "Kuddy Baba": 4.7,
    "Fun Park": 4.2,
    "Kiddo Zone": 4.3,
    "Adventure Zone": 4.4,
    "Playtopia": 4.6,
    "Wonderland": 4.6
}

total = 0

for playzone, rating in playzones.items():
    print(f"{playzone} rating: {rating}")
    total += rating

average = total / len(playzones)
print((f"\nAverage rating: {average}"))

best_playzone = max(playzones, key=playzones.get)
print(f"\nHighest rated playzone: {best_playzone} - {playzones[best_playzone]}")
print(f"\nmax(playzones.values()): {max(playzones.values())}")

min_playzone = min(playzones, key=playzones.get)
print(f"\nLowest rated playzone: {min_playzone} - {playzones[min_playzone]}")
print(f"\nmin(playzones.values()): {min(playzones.values())}")