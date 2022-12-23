#!/usr/local/bin/python3
import re
from collections import deque

with open("input.txt", "r") as f:
    valvesData = f.read().strip().split("\n")

valueNames = re.compile(r"[A-Z][A-Z]")
pressures = re.compile(r"\d+")

valveTunnels={}
valvePressures={}

for valve in valvesData:
    valveTunnels[valueNames.findall(valve)[0]] =valueNames.findall(valve)[1:]
    valvePressures[valueNames.findall(valve)[0]]=int(pressures.findall(valve)[0])

valves = list(valveTunnels.keys())

distanceMap = {}
activeValves = []

for valve in valves:
    if not valvePressures[valve] and valve != "AA": # We only want to find path between active valves (and AA which is where we start)
        continue
    if valve != "AA":
        activeValves.append(valve)

    distanceMap[valve] = {}
    previouslyVisited = set([valve])

    paths = deque([(valve, 0)])
    while paths:
        curentValve, time = paths.popleft()
        for neighbour in valveTunnels[curentValve]:
            if neighbour in previouslyVisited:
                continue
            previouslyVisited.add(neighbour)
            if valvePressures[neighbour]:
                distanceMap[valve][neighbour] = time+1
            paths.append((neighbour, time+1))

paths2=deque()
#time, pressure, current valve, open valves
paths2.append([0, 0, "AA", set()])
pressures=[]

while paths2:
    min, pressure, currentValve, openValves = paths2.popleft()
    if min==30 or len(openValves) == len(activeValves):
        pressures.append(pressure)
        continue
    for valveOption in list(distanceMap[currentValve].keys()) :
        if valveOption not in openValves:
            newMin=min+distanceMap[currentValve][valveOption]+1  # add 1 min for opening after getting there
            newPressure = pressure+(valvePressures[valveOption])*(30-newMin)
            newOpenValves = openValves.union(set([valveOption]))
            if newMin <= 30: # only append if can do in 30 min
                paths2.append([newMin,newPressure,valveOption,newOpenValves])

print(max(pressures))