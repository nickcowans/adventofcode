import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

file1 = open(fileName, 'r')
lines = file1.readlines()

matrix = []

for line in lines:
    for i in range(0,10):
        matrix.append(int(line[i]))

matrix = np.reshape(matrix, (10,10))
print(matrix)

def addZeros(matrix):
    outputMat = [0]*12
    for line in matrix:
        outputMat.append(0)
        for i in range(0, 10):
            outputMat.append(int(line[i]))
        outputMat.append(0)
    for i in range(0,12):    
        outputMat.append(0)
    return(np.reshape(outputMat, (12, 12)))

def removeZeros(matrix):
    return(matrix[1:11,1:11])

totFlashes = 0

for it in range(0, 100): #change to 100
    print("Iteration:", it+1)
    matrix = addZeros(matrix + 1)
    keepGoing = True

    while keepGoing == True:
        flashes = matrix >= 10
        thisFlashes = sum(sum(flashes))
        totFlashes = totFlashes + thisFlashes
        if thisFlashes > 0:
            for i in range(1,11):
                for j in range(1,11):
                    if flashes[i,j] == True:
                        if matrix[i-1,j-1] >0 and matrix[i-1,j-1] <= 10:
                            matrix[i-1,j-1] = matrix[i-1,j-1] + 1
                        if matrix[i-1,j] >0 and matrix[i-1,j] <=10:
                            matrix[i-1,j] = matrix[i-1,j] + 1
                        if matrix[i-1,j+1] > 0 and matrix[i-1,j+1] <= 10:
                            matrix[i-1,j+1] = matrix[i-1,j+1] + 1
                        if matrix[i,j-1] > 0 and matrix[i,j-1] <= 10:
                            matrix[i,j-1] = matrix[i,j-1] + 1
                        if matrix[i,j+1] > 0 and matrix[i,j+1] <= 10:
                            matrix[i,j+1] = matrix[i,j+1] + 1
                        if matrix[i+1,j-1] > 0 and matrix[i+1,j-1] <= 10:
                            matrix[i+1,j-1] = matrix[i+1,j-1] + 1
                        if matrix[i+1,j] > 0 and matrix[i+1,j] <= 10:
                            matrix[i+1,j] = matrix[i+1,j] + 1
                        if matrix[i+1,j+1] > 0 and matrix[i+1,j+1] <= 10:
                            matrix[i+1,j+1] = matrix[i+1,j+1] + 1
                        matrix[i,j] = 0
        else:
            keepGoing = False
    
    matrix = removeZeros(matrix)    
    print(matrix)   

print("Total flashes: ", totFlashes)
