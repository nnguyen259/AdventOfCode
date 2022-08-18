import itertools
from math import prod

with open("2015/day2/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()

result = 0
for present in data:
    dimensions = list(map(int, present.split("x")))
    volume = prod(dimensions)
    smallest = min(map(sum, itertools.combinations(dimensions, 2)))
    result += volume + 2 * smallest

print(result)
