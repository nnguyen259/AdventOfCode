with open("2015/day8/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()

len_code = 0
len_encode = 0
for line in data:
    len_code += len(line)
    len_encode += len(line) + 2
    for char in line:
        if char in ['"', "\\"]:
            len_encode += 1


print(len_encode - len_code)
