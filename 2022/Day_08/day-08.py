#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    data = f.read()

grid = data.strip().split("\n")
nRow = len(grid)
nCol = len(grid[0])
list1 = []
for i in range(0,nRow):
    for j in range(0,nCol):
        list1.append(int(grid[i][j]))

fg = [list1[r*nCol:(r+1)*nCol] for r in range(0,nRow)] #finalGrid
fg2 = [list(sublist) for sublist in list(zip(*fg))]

count=0
for i in range(1,nRow-1):
    for j in range(1,nCol-1):
        h = fg[i][j] #height
        if (max(fg[i][:j])<h) or (max(fg[i][j+1:])<h) or (max(fg2[j][:i])<h) or (max(fg2[j][i+1:])<h):
            count +=1

print(count+(nRow*4)-4) # part1

def calScore(h, list):
    score=0
    for i in range(0,len(list)):
        if int(list[i]) < h:
            score +=1
        else:
            score +=1
            break
    return score

totScore = []
for i in range(1,nRow-1):
    for j in range(1,nCol-1):
        h = int(fg[i][j]) #height
        left = fg[i][:j]
        left.reverse()
        right = fg[i][j+1:]
        above = fg2[j][:i]
        above.reverse()
        below = fg2[j][i+1:]
        totScore.append(calScore(h,left)*calScore(h,right)*calScore(h,above)*calScore(h,below))

print(max(totScore)) # part2
