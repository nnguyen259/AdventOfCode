with open("2015/day7/input.txt", "r") as inputfile:
    data = inputfile.read().splitlines()

result = dict()
operations = dict()

for operation in data:
    before, after = operation.split(" -> ")
    if before.isnumeric():
        before = int(before)
        result[after] = before

    operations[after] = before


def resolve(variable: str) -> int:
    if variable in result:
        return result[variable]

    if isinstance(operations[variable], int):
        result[variable] = operations[variable]
        return result[variable]

    operation: str = operations[variable]
    if operation.startswith("NOT "):
        operand = operation[4:]
        value = ~resolve(operand)
    elif "LSHIFT" in operation:
        left_operand, right_operand = operation.split(" LSHIFT ")
        value = resolve(left_operand) << int(right_operand)
    elif "RSHIFT" in operation:
        left_operand, right_operand = operation.split(" RSHIFT ")
        value = resolve(left_operand) >> int(right_operand)
    elif "AND" in operation:
        left_operand, right_operand = operation.split(" AND ")
        if left_operand.isnumeric():
            left_operand = int(left_operand)
        else:
            left_operand = resolve(left_operand)

        if right_operand.isnumeric():
            right_operand = int(right_operand)
        else:
            right_operand = resolve(right_operand)

        value = left_operand & right_operand
    elif "OR" in operation:
        left_operand, right_operand = operation.split(" OR ")
        if left_operand.isnumeric():
            left_operand = int(left_operand)
        else:
            left_operand = resolve(left_operand)

        if right_operand.isnumeric():
            right_operand = int(right_operand)
        else:
            right_operand = resolve(right_operand)

        value = left_operand | right_operand
    else:
        value = resolve(operation)

    result[variable] = value
    return value


value_a = resolve("a")
print(f"Part 1: {value_a}")

result = dict()
result["b"] = value_a
print(f"Part 2: {resolve('a')}")
