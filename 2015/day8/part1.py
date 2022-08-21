with open("2015/day8/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()

result = 0
for line in data:
    result += 2
    pos = 0
    for i, character in enumerate(line):
        if i < pos:
            continue
        if character == "\\":
            if line[i + 1] == "x":
                pos += 3
                result += 3
            else:
                pos += 1
                result += 1
        pos += 1


print(result)
