#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    data = f.read().strip()

instructions = data.split("\n")

cycle = 0
x = 1
xHistory = [x]

for instruction in instructions:
    if instruction == "noop":
        cycle += 1
        xHistory.append(x)
    else:
        value = int(instruction.split()[1])
        cycle += 1
        xHistory.append(x)
        cycle += 1
        x += value
        xHistory.append(x)

def calScore(ns,array):
    score=0
    for n in ns:
        score+=n*array[n-1]
    return score

print(calScore(list(range(20,221,40)),xHistory),"\n") # Part 1

message=""
for cycle in range(len(xHistory)-1):
    row = cycle // 40
    if(cycle-row*40 in [xHistory[cycle]-1,xHistory[cycle],xHistory[cycle]+1]):
        message+="#"
    else:
        message+=" " # nicer than .
    if(row != ((cycle+1) // 40)):
        message+="\n"

print(message) # part2