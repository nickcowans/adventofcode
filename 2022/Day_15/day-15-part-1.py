#!/usr/local/bin/python3
import re
from collections import deque
with open("input.txt", "r") as f:
    details = f.read().strip().split("\n")

Y = 2000000
sensors=set()
beacons=set()
noBeacon=set()

for detail in details:
    data = re.sub("[a-zA-Z =]","",detail)
    sx,sy=map(int,data.split(":")[0].split(","))
    bx,by=map(int,data.split(":")[1].split(","))
    manhattanDistance = abs(sx-bx)+abs(sy-by) 
    sensors.add((sx,sy,manhattanDistance))
    beacons.add((bx,by))
    xDist = manhattanDistance-abs(sy-Y)
    if xDist >0:
        for i in range(xDist+1):
            noBeacon.add((sx-i,Y)) 
            noBeacon.add((sx+i,Y))

print(len(noBeacon-beacons))