import numpy as np

file1 = open('input.txt', 'r')
Lines = file1.readlines()

data = []

for line in Lines:
    for i in range(0, 12):
        data.append(int(line[i]))

ncol=12
nrow=int(len(data)/ncol)
matrix=np.reshape(data, (nrow, ncol))

def calculateIndex(type, matrix=matrix):
    for i in range(0, 12):
        nrow = len(matrix)
        if nrow > 1:
            if type == 'oxygen':
                if np.sum(matrix, axis=0)[i] == nrow/2:
                    index = 1
                else:
                    index = 1*(np.sum(matrix, axis=0) >= nrow/2)[i]
            else:
                if np.sum(matrix, axis=0)[i] == nrow/2:
                    index = 0
                else:
                    index = 1*(np.sum(matrix, axis=0) <= nrow/2)[i]

            contenders=[]

            for p in matrix:
                if p[i] == index:
                    contenders.append(p)
        
            matrix = contenders

    return(matrix)

print(calculateIndex(type='oxygen'))
print(calculateIndex(type='co2'))

# Couldn't get this converted to a string... 
#[array([0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1])]
#[array([1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0])]

oxygenD=int('010110110011',2)
co2D=int('110001101010',2)
print(oxygenD)
print(co2D)
print(oxygenD*co2D)