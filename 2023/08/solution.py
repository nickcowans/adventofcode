from collections import defaultdict
from math import lcm

fileName = "in.txt"

directionInstructions = (
    open(fileName).read().strip().split("\n\n")[0]
)  # Read in the input
mapInstructions = open(fileName).read().strip().split("\n\n")[1].split("\n")

instructions = {}
startingLocations = []
for mapInstruction in mapInstructions:
    if mapInstruction.split()[0][2] == "A":
        startingLocations.append(mapInstruction.split()[0])
    instructions[mapInstruction.split()[0]] = {
        "L": mapInstruction.split()[2].strip("(,"),
        "R": mapInstruction.split()[3].strip(")"),
    }

currentLocation = "AAA"
currentInstruction = 0
maxInstruction = len(directionInstructions)
stepNo = 0
while not currentLocation == "ZZZ":
    currentLocation = instructions[currentLocation][
        directionInstructions[currentInstruction]
    ]
    currentInstruction += 1
    if currentInstruction >= maxInstruction:
        currentInstruction = 0
    stepNo += 1

print("Part1:", stepNo)

noStarting = len(startingLocations)
currentInstruction = 0
maxInstruction = len(directionInstructions)
stepNo = 0
cycleNos = defaultdict(int)

while len(cycleNos) < noStarting:
    for i in range(0, len(startingLocations)):
        startingLocations[i] = instructions[startingLocations[i]][
            directionInstructions[currentInstruction]
        ]
        if startingLocations[i][2] == "Z" and cycleNos[i] == 0:
            cycleNos[i] = stepNo + 1

    currentInstruction += 1
    if currentInstruction >= maxInstruction:
        currentInstruction = 0
    stepNo += 1

print("Part2:", lcm(*list(cycleNos.values())))
