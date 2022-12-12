from collections import deque
grid = [list(x) for x in open("input.txt").read().strip().splitlines()]

startPositions=[]
for rowNum, rowCols in enumerate(grid):
    for colNum, letter in enumerate(rowCols):
        if letter == "a":
            startPositions.append((rowNum, colNum))
        if letter == "E":
            endRow = rowNum
            endCol = colNum
            grid[rowNum][colNum] = "z"

stepCounter = []

for startRow, startCol in startPositions:

    validPaths = deque() # need to pop from left
    validPaths.append((0, startRow, startCol)) # step No, row, col
    visitedCoords = [(startRow, startCol)] # keep track of where i've been

    while validPaths: # For each validPath
        step, thisRow, thisCol = validPaths.popleft()
        for testRow, testCol in [(thisRow, thisCol-1), (thisRow, thisCol+1), (thisRow-1, thisCol), (thisRow+1, thisCol)]:
            if (testRow, testCol) in visitedCoords:
                continue # been there, got t-shirt, do nothing
            if testRow < 0 or testRow >= len(grid) or testCol < 0 or testCol >= (len(grid[0])):
                continue # space doesn't exist, do nothing
            if ord(grid[testRow][testCol]) - ord(grid[thisRow][thisCol]) > 1: # has to be 0 or 1 or negative any number
                continue # step too far, do nothing
            if (testRow, testCol) == (endRow, endCol):
                stepCounter.append(step + 1) # FOUND IT! Part 2
                exit
            validPaths.append((step + 1, testRow, testCol))
            visitedCoords.append((testRow, testCol))
    

print(min(stepCounter)) # part 2