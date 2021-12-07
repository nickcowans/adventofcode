import numpy as np

with open("input.txt", "r") as f:
    data = f.readlines()

fileSize = len(data) # 500

inputCoords = []

for i in range(0, fileSize):
    inputCoords.append(list(map(int,data[i].replace('\n', '').replace(' -> ', ',').split(","))))

inputCoords=np.reshape(inputCoords, (fileSize, 4)) 

gridSize = 1000
#gridSize = 10

fillInGrid = np.reshape([0] * gridSize * gridSize, (gridSize, gridSize))

for inputCoords in inputCoords:
    if inputCoords[0] == inputCoords[2]: # x's same
        for i in range(min(inputCoords[1], inputCoords[3]), max(inputCoords[1], inputCoords[3])+1):
            fillInGrid[inputCoords[0], i] = fillInGrid[inputCoords[0], i] + 1
    elif inputCoords[1] == inputCoords[3]: # y's same
        for i in range(min(inputCoords[0], inputCoords[2]), max(inputCoords[0], inputCoords[2])+1):
            fillInGrid[i, inputCoords[1]] = fillInGrid[i, inputCoords[1]] + 1  
         
print(np.ndarray.sum(1*fillInGrid >= 2))
