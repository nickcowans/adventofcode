import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

with open(fileName, "r") as f:
    data = f.readlines()

fishes = list(map(int,data[0].split(",")))

days=80


for day in range(1, days+1):
    newFishes = []
    addNewFishes =[]
    for fish in fishes:
        if fish == 0:
            newFishes.append(6)
            addNewFishes.append(8)
        else:
            newFishes.append(fish-1)
    for fish in addNewFishes:
        newFishes.append(fish)
    fishes=newFishes
    
print(len(fishes))