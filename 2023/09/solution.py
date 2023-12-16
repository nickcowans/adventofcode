from collections import deque


def historiesFunction(part):
    counter = 0

    for history in histories:
        if part == "Part1:":
            readings = [int(value) for value in history.split()]
        else:
            readings = [int(value) for value in history.split()][::-1]
        diagram = deque([readings])
        while any(value != 0 for value in readings):
            readingDiffs = []
            for i in range(0, len(readings) - 1):
                readingDiffs.append(readings[i + 1] - readings[i])
            readings = readingDiffs
            diagram.appendleft(readings)
        for j in range(1, len(diagram)):
            len1 = len(diagram[j - 1]) - 1
            len2 = len(diagram[j]) - 1
            diagram[j].append(diagram[j][len2] + diagram[j - 1][len1])
        counter += diagram[j][len2 + 1]

    print(part, counter)


histories = open("in.txt").read().strip().split("\n")

historiesFunction("Part1:")
historiesFunction("Part2:")
