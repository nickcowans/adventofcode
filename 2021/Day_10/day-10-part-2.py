import numpy as np

fileName = "input.txt"
#fileName = "example.txt"

file1 = open(fileName, 'r')
lines = file1.readlines()

open  = ('(', '[', '{', '<')
close = (')', ']', '}', '>')
points = [3, 57, 1197, 25137]
aPoints = [1, 2, 3, 4]

totalPoints=0
score = []
def autoComplete(line):
    #print(line)
    lineLen = len(line)-1
    score = 0
    while lineLen >= 0:
        #print(line[lineLen], score)
        score = score * 5 + aPoints[open.index(line[lineLen])]
        lineLen = lineLen - 1
    return(score)

for line in lines:
    carryOn = True
    c = 0
    line  = line.replace('\n', '')
    while c <= len(line) and carryOn == True:
        if c == len(line):
            score.append(autoComplete(line))
            carryOn = False
        elif line[c] in close:
            other = open[close.index(line[c])]
            if line[c-1] == other:
                line = line[0:c-1] + line[c+1:]
                c = c -2
            else:
                #print("Expected:", close[open.index(line[c-1])], "but found:", line[c])
                totalPoints = totalPoints + points[close.index(line[c])]
                carryOn = False
        c = c + 1

print(int(np.median(score)))