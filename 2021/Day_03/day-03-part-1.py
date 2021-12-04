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
gamma = map(str,list(1*(np.sum(matrix, axis=0) > nrow/2)))
epsilon = list(1*(np.sum(matrix, axis=0) < nrow/2))

gammaD=int("".join(map(str,gamma)),2)
epsilonD=int("".join(map(str,epsilon)),2)

print("Gamma: ",  gammaD)
print("Epsilon: ", epsilonD)
print("Power: ", gammaD * epsilonD)