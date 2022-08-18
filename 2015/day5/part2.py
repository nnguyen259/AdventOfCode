with open("2015/day5/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()


result = 0

for phrase in data:
    pairs = dict()
    pair_condition = False
    letter_condition = False

    for i, char in enumerate(phrase[0:-1]):
        if 1 <= i <= (len(phrase) - 2) and not letter_condition:
            if phrase[i - 1] == phrase[i + 1]:
                letter_condition = True

        if not pair_condition:
            pair = f"{char}{phrase[i + 1]}"
            if pair not in pairs:
                pairs[pair] = i
            else:
                if pairs[pair] != i - 1:
                    pair_condition = True

        if pair_condition and letter_condition:
            result += 1
            break

print(result)
