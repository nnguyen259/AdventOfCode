with open("2015/day5/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()


result = 0
vowels = ["a", "i", "u", "e", "o"]
banned = ["ab", "cd", "pq", "xy"]

for phrase in data:
    vowel_count = 0
    consecutive = False
    consecutive_count = 1
    for i, char in enumerate(phrase):
        if char in vowels:
            vowel_count += 1
        if i > 0:
            if f"{phrase[i-1]}{char}" in banned:
                consecutive = False
                break
            if char == phrase[i - 1] and not consecutive:
                consecutive_count += 1
                if consecutive_count == 2:
                    consecutive = True
            else:
                consecutive_count = 1
    if vowel_count >= 3 and consecutive:
        result += 1

print(result)
