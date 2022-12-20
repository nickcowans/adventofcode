#!/usr/local/bin/python3
import re
from collections import deque
with open("input.txt", "r") as f:
    details = f.read().strip().split("\n")

sensors=set()
beacons=set()

for detail in details:
    data = re.sub("[a-zA-Z =]","",detail)
    sx,sy=map(int,data.split(":")[0].split(","))
    bx,by=map(int,data.split(":")[1].split(","))
    sensors.add((sx,sy))
    beacons.add((bx,by))

noBecon = set()

for sensor in sensors:
    print(sensor)
    carryOn = True
    examineList = deque()
    examinedList = set()
    examineList.append((sensor[0],sensor[1]))
    while examineList:
        print(len(examineList))
        examX,examY = examineList.popleft()
        examinedList.add((examX,examY))    
        if (examX,examY) in beacons:
            #print(examX,examY)
            carryOn = False
        else:
            noBecon.add((examX,examY))
        if carryOn:
            if (examX+1,examY) not in examinedList and (examX+1,examY) not in examineList:
                examineList.append((examX+1,examY)) 
            if (examX-1,examY) not in examinedList and (examX-1,examY) not in examineList:
                examineList.append((examX-1,examY)) 
            if (examX,examY+1) not in examinedList and (examX,examY+1) not in examineList:
                examineList.append((examX,examY+1)) 
            if (examX,examY-1) not in examinedList and (examX,examY-1) not in examineList:
                examineList.append((examX,examY-1)) 

numberOfNoBeacon=0
for space in (sorted(noBecon)):
    numberOfNoBeacon+=1 if space[1] == 2000000 else 0

print(numberOfNoBeacon)