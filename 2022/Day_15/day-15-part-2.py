#!/usr/local/bin/python3
import re
from collections import deque
with open("input.txt", "r") as f:
    details = f.read().strip().split("\n")

lims = 4000000
coords = []

for detail in details:
    data = re.sub("[a-zA-Z =]","",detail)
    sx,sy=map(int,data.split(":")[0].split(","))
    bx,by=map(int,data.split(":")[1].split(","))
    coords.append([sx,sy,bx,by])

for Y in range(lims+1):
    sensors=set()
    beacons=set()
    noBeaconX=[]

    for coord in coords:
        sx,sy,bx,by = coord
        manhattanDistance = abs(sx-bx)+abs(sy-by) 
        sensors.add((sx,sy,manhattanDistance))
        beacons.add((bx,by))
        xDist = manhattanDistance-abs(sy-Y)
        if xDist >0:
            noBeaconX.append((sx-xDist,sx+xDist))
        noBeaconX.sort()

    noBeaconXCondensed=[]
    for xlo, xhi in noBeaconX:
        if noBeaconXCondensed == []:
            noBeaconXCondensed.append([xlo, xhi])
            continue
        if noBeaconXCondensed[-1][1] + 1 < xlo:
            noBeaconXCondensed.append([xlo, xhi])
            continue
        noBeaconXCondensed[-1][1] = max(xhi, noBeaconXCondensed[-1][1])

    if noBeaconXCondensed[0][0] < 0: noBeaconXCondensed[0][0] = 0
    if noBeaconXCondensed[-1][0] < lims: noBeaconXCondensed[-1][1] = lims
    if noBeaconXCondensed != [[0, lims]]:
        print((noBeaconXCondensed[0][1]+1)*4000000+Y)
