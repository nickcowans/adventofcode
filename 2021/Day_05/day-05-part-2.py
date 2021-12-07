import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

with open(fileName, "r") as f:
    data = f.readlines()

fileSize = len(data) # 500

inputCoords = []

for i in range(0, fileSize):
    inputCoords.append(list(map(int,data[i].replace('\n', '').replace(' -> ', ',').split(","))))

inputCoords=np.reshape(inputCoords, (fileSize, 4)) 

gridSize = 1000

fillInGrid = np.reshape([0] * gridSize * gridSize, (gridSize, gridSize))

for inputCoord in inputCoords:
    if inputCoord[0] == inputCoord[2]: # x's same
        for i in range(min(inputCoord[1], inputCoord[3]), max(inputCoord[1], inputCoord[3])+1):
            fillInGrid[inputCoord[0], i] = fillInGrid[inputCoord[0], i] + 1
    elif inputCoord[1] == inputCoord[3]: # y's same
        for i in range(min(inputCoord[0], inputCoord[2]), max(inputCoord[0], inputCoord[2])+1):
            fillInGrid[i, inputCoord[1]] = fillInGrid[i, inputCoord[1]] + 1  
    else: # diag at 45 deg
        fromX = min(inputCoord[0], inputCoord[2])
        toX = max(inputCoord[0], inputCoord[2])
        if fromX == inputCoord[0]:
            fromY = inputCoord[1]    
            toY = inputCoord[3]
        else:
            fromY = inputCoord[3]
            toY = inputCoord[1]
        if fromY > toY:
            mult = -1
        else:
            mult = 1
        #print(inputCoord, fromX, fromY, toX, toY)
        c = 0
        for i in range(fromX, toX+1):
            fillInGrid[i, fromY+c*mult] = fillInGrid[i, fromY+c*mult] + 1  
            c=c+1

#print(fillInGrid)
print(np.ndarray.sum(1*fillInGrid >= 2))
