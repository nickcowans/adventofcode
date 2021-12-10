import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

file1 = open(fileName, 'r')
lines = file1.readlines()

lineLen = len(lines[0]) -1
fileLen = len(lines)

data = []

for line in lines:
    for i in range(0, lineLen):
        data.append(int(line[i]))

matrix=np.reshape(data, (fileLen, lineLen))

#print(matrix)
risk = 0

for i in range(0, fileLen):
    for j in range(0, lineLen):
        if i==0: # first row
            if j==0: # first col
                if matrix[i,j] < matrix[i+1,j] and matrix[i,j] < matrix[i,j+1]:
                    risk = risk + matrix[i,j] + 1
            elif j==lineLen-1: # last col
                if matrix[i,j] < matrix[i+1,j] and matrix[i,j] < matrix[i,j-1]:
                    risk = risk + matrix[i,j] + 1
            else:
                if matrix[i,j] < matrix[i,j-1] and matrix[i,j] < matrix[i+1,j] and matrix[i,j] < matrix[i,j+1]:
                    risk = risk + matrix[i,j] + 1
        elif i==fileLen-1: # last row
            if j==0: # first col
                if matrix[i,j] < matrix[i-1,j] and matrix[i,j] < matrix[i,j+1]:
                    risk = risk + matrix[i,j] + 1
            elif j==lineLen-1: # last col
                if matrix[i,j] < matrix[i-1,j] and matrix[i,j] < matrix[i,j-1]:
                    risk = risk + matrix[i,j] + 1
            else:
                if matrix[i,j] < matrix[i-1,j] and matrix[i,j] < matrix[i,j+1] and matrix[i,j] < matrix[i,j-1]:
                    risk = risk + matrix[i,j] + 1
        else:
            if j==0: # first col
                if matrix[i,j] < matrix[i+1,j] and matrix[i,j] < matrix[i-1,j] and matrix[i,j] < matrix[i,j+1]:
                    risk = risk + matrix[i,j] + 1
            elif j==lineLen-1: # last col
                if matrix[i,j] < matrix[i-1,j] and matrix[i,j] < matrix[i+1,j] and matrix[i,j] < matrix[i,j-1]:
                    risk = risk + matrix[i,j] + 1
            else:
                if matrix[i,j] < matrix[i-1,j] and matrix[i,j] < matrix[i+1,j] and matrix[i,j] < matrix[i,j-1] and matrix[i,j] < matrix[i,j+1]:
                    risk = risk + matrix[i,j] + 1

print(risk)

