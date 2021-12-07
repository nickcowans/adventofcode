import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

with open(fileName, "r") as f:
    data = f.readlines()

crabPositions = list(map(int,data[0].split(",")))

minCrabPosition = min(crabPositions)
maxCrabPosition = max(crabPositions)

fuleUsedMatrix = []

for i in range(minCrabPosition, maxCrabPosition+1):
    fuelUsed = 0
    for crab in crabPositions:
        fuelUsed=fuelUsed+abs(crab-i)
    fuleUsedMatrix.append(fuelUsed)

print(min(fuleUsedMatrix))