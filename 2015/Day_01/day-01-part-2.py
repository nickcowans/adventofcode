fileName = "input.txt"

with open(fileName, "r") as f:
    data = f.read()

floor = position = 0
stop = False

for instruction in data:
    if stop == False:
        position = position + 1
        if instruction == "(":
            floor = floor + 1
        elif instruction == ")":
            floor = floor - 1
        if floor < 0:
            stop = True
        
print(position)