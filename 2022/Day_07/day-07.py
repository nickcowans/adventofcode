#!/usr/local/bin/python3
from collections import defaultdict
with open("input.txt", "r") as f:
    data = f.read()

instructions = data.strip().split("\n")
sizes = defaultdict(int)
folder = []

for i in instructions:
    command = i.split(" ")
    if(command[1] == 'cd'):
        if(command[2] == ".."):
            [folder.pop()]
        else:
            folder.append(command[2])
    elif (command[0] != 'dir') and (command[1] != 'ls'):
        for j in range(0,len(folder)):
            sizes[str(folder[0:(j+1)])] += int(command[0])

count = 0
for k,v in sizes.items():
    if (v <= 100000):
        count += v
print(count) # part 1

count = 1e9
for k,v in sizes.items():
    if (v>= sizes["['/']"]-(70000000 - 30000000)):
        count = min(count, v)
print(count) # part 2