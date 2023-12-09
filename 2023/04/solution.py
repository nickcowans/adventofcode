from collections import defaultdict

input = open("in.txt").read().strip()  # Read in the input

part1 = 0

for gameNo, line in enumerate(input.split("\n")):
    winSet, mySet = line.split(":")[1].split(" | ")
    thisGameScore = 0
    for chance in winSet.split():
        if chance in mySet.split():
            thisGameScore = int(max(0.5, thisGameScore) * 2)
    part1 += thisGameScore

print("Part1:", part1)

scratchcards = []

for gameNo, line in enumerate(input.split("\n")):
    scratchcards.append([gameNo + 1, line.split(":")[1].split(" | ")])

scratchcardCount = defaultdict(int)

for scratchcard in scratchcards:
    scratchcardCount[scratchcard[0]] += 1
    winSet, mySet = scratchcard[1]
    thisGameScore = 0
    for chance in winSet.split():
        if chance in mySet.split():
            thisGameScore += 1
    while thisGameScore > 0:
        thisGameScore -= 1
        scratchcardCount[scratchcard[0] + thisGameScore + 1] += scratchcardCount[
            scratchcard[0]
        ]

print("Part2:", sum(scratchcardCount.values()))
