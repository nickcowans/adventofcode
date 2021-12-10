import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

file1 = open(fileName, 'r')
lines = file1.readlines()

lineLen = len(lines[0]) - 1
fileLen = len(lines)

data = []

for line in lines:
    for i in range(0, lineLen):
        data.append(int(line[i]))

# Figured out could surround matrix in 9's and skip edges - much less code below
matrix = [9]*(lineLen+2)
for line in lines:
    matrix.append(9)
    for i in range(0, lineLen):
        matrix.append(int(line[i]))
    matrix.append(9)
for i in range(0,lineLen+2):    
    matrix.append(9)

matrix=np.reshape(matrix, (fileLen+2, lineLen+2))

basins = []
numBasins = 0

for i in range(1, fileLen+1):
    for j in range(1, lineLen+1):
        if matrix[i,j] < matrix[i-1,j] and matrix[i,j] < matrix[i+1,j] and matrix[i,j] < matrix[i,j-1] and matrix[i,j] < matrix[i,j+1]:
            basins.append([i,j])
            numBasins = numBasins + 1

basins=np.reshape(basins, (numBasins, 2))

def checkAdjacent(check, inBasin):
    if matrix[check[0], check[1]] != 9 and check not in inBasin:
        inBasin.append(check)
    return(inBasin)

basinLens = []

for basin in basins:
    inBasin = []
    inBasin.append(list(basin))

    for condender in inBasin:
        inBasin = checkAdjacent(check = [condender[0]-1, condender[1]], inBasin=inBasin)
        inBasin = checkAdjacent(check = [condender[0]+1, condender[1]], inBasin=inBasin)
        inBasin = checkAdjacent(check = [condender[0], condender[1]-1], inBasin=inBasin)
        inBasin = checkAdjacent(check = [condender[0], condender[1]+1], inBasin=inBasin)
    
    basinLens.append(len(inBasin))

orderedBasinLen = sorted(basinLens)
print(np.product(orderedBasinLen[numBasins-3:numBasins]))