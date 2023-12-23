lines = open("in.txt").read().strip().split("\n")

lineMax = len(lines)
colMax = len(lines[0])

# print(colMax, lineMax)

myMap = {}
for line in range(0, lineMax):
    for col in range(0, colMax):
        myMap[str(line) + "|" + str(col)] = lines[line][col]

rules = {
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
}

opposite = {"N": "S", "S": "N", "E": "W", "W": "E"}
coordsMap = {"N": [-1, 0], "S": [1, 0], "E": [0, 1], "W": [0, -1]}


def returnCoords(symbol):
    coordinates_str = list(myMap.keys())[list(myMap.values()).index(symbol)].split("|")
    return [int(coord) for coord in coordinates_str]


def returnNextPart(coords, dirIn):
    line, col = coords
    thisSym = myMap[str(line) + "|" + str(col)]
    if thisSym == "S":
        return [None, None, thisSym]
    dirOut = [item for item in rules[thisSym] if item != opposite[dirIn]][0]
    coordsOut = [x + y for x, y in zip(coords, coordsMap[dirOut])]
    # print(line, col, thisSym, dirOut, coordsOut)
    return coordsOut, dirOut, thisSym


start = returnCoords("S")
print("Start:", start)

coords = [21, 103]  # Manually add in
dir = "S"
sym = ""

i = 0

while sym != "S":
    # print(i, coords, dir, sym)
    coords, dir, sym = returnNextPart(coords, dir)
    i = i + 1

print("Part1:", int(i / 2))
