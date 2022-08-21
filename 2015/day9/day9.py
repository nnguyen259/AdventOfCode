import itertools

with open("2015/day9/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()

places = set()
distances = dict()
results = list()

for travel in data:
    start, _, end, _, travel_distance = travel.split(" ")
    places.add(start)
    places.add(end)
    distances[(start, end)] = distances[(end, start)] = int(travel_distance)

for travel_road in itertools.permutations(places):
    total_distance = 0
    for i, place in enumerate(travel_road[:-1]):
        total_distance += distances[(place, travel_road[i + 1])]
    results.append(total_distance)

print(min(results))
print(max(results))
