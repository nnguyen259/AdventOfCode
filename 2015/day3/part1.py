with open("2015/day3/input.txt", "r") as inputfile:
    data = inputfile.read()

x = 0
y = 0

result = set()
result.add((0, 0))

for direction in data:
    if direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    elif direction == "^":
        y += 1
    else:
        y -= 1

    result.add((x, y))

print(len(result))
