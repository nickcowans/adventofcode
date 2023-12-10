input = open("in.txt").read().strip().split("\n")  # Read in the input
pairs = list(
    zip(input[0].split(":")[1].strip().split(), input[1].split(":")[1].strip().split())
)

winVals = []
for pair in pairs:
    wins = 0
    for i in range(0, int(pair[0])):
        traveled = i * (int(pair[0]) - i)
        if traveled > int(pair[1]):
            wins += 1
    winVals.append(wins)

part1 = 1
for value in winVals:
    part1 *= value

print("Part1:", part1)

pairs2 = [
    ["".join(sublist)]
    for sublist in (
        input[0].split(":")[1].strip().split(),
        input[1].split(":")[1].strip().split(),
    )
]

pairs3 = [pairs2[0][0], pairs2[1][0]]
winVals = []
notWins = 0
cont = True
i = 0
while cont:
    traveled = i * (int(pairs3[0]) - i)
    if traveled > int(pairs3[1]):
        cont = False
    else:
        notWins += 1
    # print(i, traveled > int(pairs3[1]))
    i = i + 1

cont = True
i = int(pairs3[0])
while cont:
    traveled = i * (int(pairs3[0]) - i)
    if traveled > int(pairs3[1]):
        cont = False
    else:
        notWins += 1
    # print(i, traveled > int(pairs3[1]))
    i = i - 1

print("Part2:", int(pairs3[0]) - (notWins - 1))
