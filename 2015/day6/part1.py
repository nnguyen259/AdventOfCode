with open("2015/day6/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in data:
    modes = ("toggle ", "turn on ", "turn off ")
    for mode in modes:
        if instruction.startswith(mode):
            break

    detail = instruction.split(mode)[1]
    startx, starty, endx, endy = (
        int(place)
        for coordinate in detail.split(" through ")
        for place in coordinate.split(",")
    )
    for i in range(startx, endx + 1):
        for j in range(starty, endy + 1):
            if mode == "toggle ":
                if grid[i][j] == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0
            elif mode == "turn on ":
                grid[i][j] = 1
            else:
                grid[i][j] = 0

result = sum(map(sum, grid))
print(result)
