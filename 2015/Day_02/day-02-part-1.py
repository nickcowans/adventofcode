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

wrappingPaper = 0
for present in presentMatrix:
    lw = present[0]*present[1]
    wh = present[1]*present[2]
    hl = present[2]*present[0]
    wrappingPaperThisPresent = 2*lw + 2*wh + 2*hl + min((lw,wh,hl))
    wrappingPaper = wrappingPaper + wrappingPaperThisPresent

print(wrappingPaper)