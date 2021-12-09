import numpy as np

fileName = "input.txt"

with open(fileName, "r") as f:
    data = f.readlines()

fileSize = len(data) # 1000

print(fileSize)

presentList = []

for i in range(0, fileSize):
    presentList.append(list(map(int,data[i].replace('\n', '').split("x"))))

presentMatrix=np.reshape(presentList, (fileSize, 3)) 

ribbon = 0
for present in presentMatrix:
    sortedDims = (np.sort(present, axis=-1, kind='quicksort', order=None))
    ribbon = ribbon + 2*sortedDims[0]+ 2*sortedDims[1] + (sortedDims[0]*sortedDims[1]*sortedDims[2])

print(ribbon)