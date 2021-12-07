import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

days=256

with open(fileName, "r") as f:
    data = f.readlines()

fishes = list(map(int,data[0].split(",")))

countMatrix = []

for fishDay in range(0,9):
    countMatrix.append(fishes.count(fishDay))

for day in range(1, days+1):
    newCountMatrix = []
    newCountMatrix.append(countMatrix[1])
    newCountMatrix.append(countMatrix[2])
    newCountMatrix.append(countMatrix[3])
    newCountMatrix.append(countMatrix[4])
    newCountMatrix.append(countMatrix[5])
    newCountMatrix.append(countMatrix[6])
    newCountMatrix.append(countMatrix[0]+countMatrix[7])
    newCountMatrix.append(countMatrix[8])
    newCountMatrix.append(countMatrix[0])
    countMatrix=newCountMatrix

print(sum(countMatrix))