import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

with open(fileName, "r") as f:
    data = f.readlines()

uniqueDig = 0

for line in data[0]:
    thisRow = line.split("|")[1].replace('\n', '').split(" ")
    thisRow = thisRow[1:len(thisRow)] # lazy way to drop first empty string
    for digit in thisRow:
        if len(digit) in (2,3,4,7):
            uniqueDig = uniqueDig + 1

print(uniqueDig)