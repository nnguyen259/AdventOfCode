import itertools
from math import prod

with open("2015/day2/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()

result = 0
for present in data:
    dimensions = map(int, present.split("x"))
    sizes = [2 * prod(x) for x in itertools.combinations(dimensions, 2)]
    result += sum(sizes) + min(sizes) // 2

print(result)
