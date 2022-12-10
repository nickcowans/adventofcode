#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    data = f.read().strip()

instructions = data.split("\n")
x = 1
xHistory = [x]

for instruction in instructions:
    if instruction == "noop":
        xHistory.append(x)
    else:
        value = int(instruction.split()[1])
        xHistory.append(x)
        x += value
        xHistory.append(x)

def calculateSignalStrength(ns,array):
    """Calculate the sum of signal strengths for cycles in ns."""
    score=0
    for n in ns:
        score+=n*array[n-1]
    return score

print(calculateSignalStrength(list(range(20,221,40)),xHistory)) # Part 1

message="\n"
for cycle in range(len(xHistory)-1):
    row = cycle // 40
    message+="🟨" if(cycle-row*40 in [xHistory[cycle]-1,xHistory[cycle],xHistory[cycle]+1]) else "⬛"
    message+="\n" if(row != ((cycle+1) // 40)) else ""

print(message) # Part 2