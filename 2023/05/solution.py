input = open("in.txt").read().strip().split("\n\n")  # Read in the input

seeds = [int(seed) for seed in input[0].split("seeds: ")[1].split()]
instructions = input[1:]

finals = []
for inVal in seeds:
    for instruction in instructions:
        mapName, mapCodes = instruction.split(":\n")
        mapCodesList = mapCodes.split("\n")
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
    finals.append(newVal)

print("Part1:", min(finals))
