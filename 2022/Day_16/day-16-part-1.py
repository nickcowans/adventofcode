#!/usr/local/bin/python3
import re
from collections import deque

with open("input.txt", "r") as f:
    values = f.read().strip().split("\n")

valueNames = re.compile(r"[A-Z][A-Z]")
pressures = re.compile(r"\d+")

valveTunnels={}
valvePressures={}

for valve in values:
    valveTunnels[valueNames.findall(valve)[0]] =valueNames.findall(valve)[1:]
    valvePressures[valueNames.findall(valve)[0]]=int(pressures.findall(valve)[0])

paths=deque()
#time, pressure, current valve, open valves, history
paths.append([0, 0, "AA", set(), ""])
pressures=[]

count=0
while paths:
    count+=1
    # if count % 100000 == 0 and len(pressures) > 0:
    #     print(count, paths[0][0], len(paths), max(pressures))
    # elif count % 100000 == 0:
    #     print(count, paths[0][0], len(paths), 0)
    #print("NEW LOOP:",paths[0])
    #print(paths)
    min, pressure, currentValve, openValves, history = paths.popleft()
    min+=1
    if min==30 or len(openValves) == sum([_ != 0  for _ in valvePressures.values()]):
        #print("ALL OVER", min, openValves)
        pressures.append(pressure)
        print(count, paths[0][0], len(paths), max(pressures))
        continue
    if valvePressures[currentValve] != 0 and currentValve not in openValves:
        paths.append([min,pressure+valvePressures[currentValve]*(30-min),currentValve,openValves.union(set([currentValve])),currentValve])
        #print("OPENING VALVE", currentValve)
        #print(paths)
    for valveOption in valveTunnels[currentValve]:
        if valveOption != history:
            paths.append([min,pressure,valveOption,openValves,currentValve])
            #print("APPENDING VALVE", valveOption)
            #print(paths)      


print(max(pressures))