fileName = "input.txt"

with open(fileName, "r") as f:
    data = f.read()

floor = 0

for instruction in data:
    if instruction == "(":
        floor = floor + 1
    elif instruction == ")":
        floor = floor - 1

print(floor)