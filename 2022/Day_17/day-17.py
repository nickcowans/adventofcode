#!/usr/local/bin/python3
with open("rocks.txt", "r") as f:
    rocks = f.read().strip().split("\n\n")
with open("input.txt", "r") as f:
    gusts = f.read().strip()

rocksMatrix = []
for rock in rocks:
    rows = rock.split("\n")
    thisMatrix=[]
    for row in range(len(rows)):
        for column in range(len(rows[row])):
            thisMatrix.append(((len(rows)-row-1),column)) if rows[row][column] == "#" else 0
    thisMatrix.sort()
    rocksMatrix.append(thisMatrix)

solid = set(((0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7)))
rock0=set(); rock1=set(); rock2=set(); rock3=set(); rock4=set()

def printSolid(matrix):
    maxX=0
    maxY=0
    out=""
    for coord in matrix:
        maxX=max(maxX,coord[1])
        maxY=max(maxY,coord[0])
    for Y in range(maxY,-1,-1):
        for X in range(maxX+2):
            if X == 0 or X==8 or Y==0: out+="⬛"
            elif (Y,X) in rock0: out+="🟦" 
            elif (Y,X) in rock1: out+="🟩" 
            elif (Y,X) in rock2: out+="🟪" 
            elif (Y,X) in rock3: out+="🟥" 
            elif (Y,X) in rock4: out+="🟨" 
            else: out+="⬜"
        out+="\n"
    print(out)

def moveMatrix(matrix, distance, direction):
    newmatrix = []
    for item in matrix:
        if direction == "y":
            newmatrix.append((item[0]+distance, item[1]))
        if direction == "x":
            newmatrix.append((item[0], item[1]+distance))
    return newmatrix

rockId=0
rockNumber=0
gustNumber=0

while rockNumber < 2022:
    if rockId == len(rocksMatrix):
            rockId=0
    rockNumber+=1
    floor=max(solid)[0]
    rockPosition = moveMatrix(moveMatrix(rocksMatrix[rockId], floor+4,"y"), 3,"x")
    keepGoing = True
    while keepGoing == True:
        if gustNumber == len(gusts):
            gustNumber=0
        # MOVE LEFT or RIGHT
        testRockPosition = moveMatrix(rockPosition, -1, "x") if gusts[gustNumber] == "<" else moveMatrix(rockPosition, 1, "x")
        gustNumber +=1
        testOK=True
        for coord in testRockPosition:
            if coord[1] == 0 or coord[1] == 8 or (coord) in solid:
                testOK=False
                break
        if testOK==True: rockPosition = testRockPosition 
        # MOVE Down
        testRockPosition = moveMatrix(rockPosition, -1, "y")
        for coord in testRockPosition:
            if (coord) in solid:
                keepGoing=False
        if keepGoing==False:
            for coord in rockPosition:
                solid.add((coord))
                if rockId == 0: rock0.add((coord))
                elif rockId == 1: rock1.add((coord))
                elif rockId == 2: rock2.add((coord))
                elif rockId == 3: rock3.add((coord))
                elif rockId == 4: rock4.add((coord))
        else:
            rockPosition = testRockPosition
    rockId +=1
    # print(rockNumber,max(solid)[0]) # for part 2

printSolid(solid)
print(max(solid)[0])

# Part 2
# I did this part in Excel by looking for a repeating pattern (by eye - am sure
# I coudld have done it programatically, then summing the first 178 deltas, 
# 581395348 x the next 1720 deltas then then first 1262 of the pattern again 
# for the last part: 285 + (581395348 x 2704) + 1990 = 1572093023267