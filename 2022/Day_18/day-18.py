#!/usr/local/bin/python3
from collections import deque
with open("input.txt", "r") as f:
    cubes = f.read().strip().split("\n")

matrix=[]
for cube in cubes:
    matrix.append(list(map(int, cube.split(","))))

sides = set()

minX =  int(1E10); minY =  int(1E10); minZ =  int(1E10) 
maxX = -int(1E10); maxY = -int(1E10); maxZ = -int(1E10) 

for x,y,z in matrix:
    minX = min(minX, x); minY = min(minY, y); minZ = min(minZ, z)
    maxX = max(maxX, x); maxY = max(maxY, y); maxZ = max(maxZ, z)
    for sx,sy,sz in [(-0.5,0,0), (0,-0.5,0), (0,0,-0.5), (0.5,0,0), (0,0.5,0), (0,0,0.5)]:
        if (sx+x, sy+y, sz+z) in sides:
            sides.remove((sx+x, sy+y, sz+z))
        else:
            sides.add((sx+x, sy+y, sz+z))

# Part 1
print(len(sides))

externalSides = 0

paths = deque()
paths.append((minX-1, minY-1, minZ-1))
visited = set()
visited.add((minX-1, minY-1, minZ-1))

while paths:
    x,y,z = paths.popleft()
    for sx,sy,sz in [(-1,0,0), (0,-1,0), (0,0,-1), (1,0,0), (0,1,0), (0,0,1)]:
        newX, newY, newZ = x+sx, y+sy, z+sz
        if [newX, newY, newZ] in matrix:
            externalSides+=1
            continue
        if (newX, newY, newZ) in visited or newX < (minX -1) or newX > (maxX +1) or newY < (minY -1) or newY > (maxY +1) or newZ < (minZ -1) or newZ > (maxZ +1):
            continue
        visited.add((newX, newY, newZ))
        paths.append((newX, newY, newZ))
        
# Part 2
print(externalSides)