input = open("in.txt").read().strip()  # Read in the input

part1 = 0
part2 = 0

for line in input.split("\n"):  # For each line
    lineValsPart1 = []
    lineValsPart2 = []
    for i, char in enumerate(line):  # split by character (i is the character's 'space')
        if char.isdigit():  # if it is a digit add to list for the line
            lineValsPart1.append(char)
            lineValsPart2.append(char)
        for num, string in enumerate(
            [
                "zero",
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
        ):
            # for part 2, also go through and check if there are string representations of the numbers.
            # Zero included so char space aligns.
            if line[i:].startswith(string):
                lineValsPart2.append(str(num))
    # Pick first and last char to form an integet and add to running total
    part1 += int(lineValsPart1[0] + lineValsPart1[-1])
    part2 += int(lineValsPart2[0] + lineValsPart2[-1])

print("Part 1:", part1)
print("Part 2:", part2)
