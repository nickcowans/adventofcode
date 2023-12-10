from collections import deque

input = open("test.txt").read().strip().split("\n\n")  # Read in the input

seeds = [int(seed) for seed in input[0].split("seeds: ")[1].split()]
instructions = input[1:]
print("~~~~~~~~")
print(instructions)
print("~~~~~~~~")
step1 = instructions[0].split("\n")[1:]
print(step1)

part2SeedSets = deque(seeds)
print(part2SeedSets, type(part2SeedSets))
part2Seeds = []
while part2SeedSets:
    n = part2SeedSets.popleft()
    part2Seeds.append([n, n + part2SeedSets.popleft() - 1])

seedsOfInterest = []
for i in range(len(part2Seeds)):
    i1, i2 = part2Seeds[i]
    seedsOfInterest.append(i1)
    seedsOfInterest.append(i2)
    for j in range(len(step1)):
        s1 = int(step1[j].split()[1])
        s2 = int(step1[j].split()[2]) + s1 - 1
        print(i1, i2, s1, s2)
        if (i1 >= s1) & (i1 <= s2) & (i2 >= s1) & (i2 <= s2):
            continue
        if (i1 >= s1) & (i1 <= s2) & (i2 > s2):
            seedsOfInterest.append(s2)
        if (i2 >= s1) & (i2 <= s2) & (i2 < s2):
            seedsOfInterest.append(s1)

finals = []
for inVal in seeds:
    print("Seed:", inVal)
    for instruction in instructions:
        mapName, mapCodes = instruction.split(":\n")
        mapCodesList = mapCodes.split("\n")
        print("Map:", mapCodesList)
        newVal = False
        i = 0
        maxI = len(mapCodesList)
        while newVal == False and i < maxI:
            D, S, R = map(
                int, mapCodesList[i].split()
            )  # Destination Start, Source Start, Range
            newVal = D + inVal - S if S <= inVal < S + R else False
            i += 1
        if newVal == False:
            newVal = inVal
        inVal = newVal
        print("Final:", inVal)
    finals.append(newVal)

print("Part1:", min(finals))

print("+++++", seedsOfInterest)

finals = []
for inVal in seedsOfInterest:
    print("Seed:", inVal)
    for instruction in instructions:
        mapName, mapCodes = instruction.split(":\n")
        mapCodesList = mapCodes.split("\n")
        print("Map:", mapCodesList)
        newVal = False
        i = 0
        maxI = len(mapCodesList)
        while newVal == False and i < maxI:
            D, S, R = map(
                int, mapCodesList[i].split()
            )  # Destination Start, Source Start, Range
            newVal = D + inVal - S if S <= inVal < S + R else False
            i += 1
        if newVal == False:
            newVal = inVal
        inVal = newVal
        print("Final:", inVal)
    finals.append(newVal)

print("Part2:", min(finals))
