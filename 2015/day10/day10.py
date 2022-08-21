data = "1321131112"


def process(number: str):
    count = 1
    num = number[0]
    result = ""
    for char in number[1:]:
        if char == num:
            count += 1
        else:
            result += f"{count}{num}"
            count = 1
            num = char
    result += f"{count}{num}"
    return result


for _ in range(40):
    data = process(data)
print(len(data))

for _ in range(10):
    data = process(data)
print(len(data))
