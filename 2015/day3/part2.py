with open("2015/day3/input.txt", "r") as inputfile:
    data = inputfile.read()

sx = 0
sy = 0

rx = 0
ry = 0

result = set()
result.add((0, 0))
robo = False

for direction in data:
    if robo:
        x = rx
        y = ry
    else:
        x = sx
        y = sy

    if direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    elif direction == "^":
        y += 1
    else:
        y -= 1

    if robo:
        rx = x
        ry = y
    else:
        sx = x
        sy = y

    robo = not robo
    result.add((x, y))

print(len(result))
