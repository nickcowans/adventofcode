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
        currentValve, time = paths.popleft()
        for neighbour in valveTunnels[currentValve]:
            if neighbour in previouslyVisited:
                continue
            previouslyVisited.add(neighbour)
            if valvePressures[neighbour]:
                distanceMap[valve][neighbour] = time+1
            paths.append((neighbour, time+1))


valveIndex = {}

for index, element in enumerate(activeValves):
    valveIndex[element] = index

cache = {}

## Depth First (https://en.wikipedia.org//wiki/Depth-first_search)
# Highly inspired by https://github.com/hyper-neutrino/advent-of-code
# I started off trying to do this with deque (see day-16-part-1.py) but I 
# couldn't get it to optimise for input
def depthFirstSearch(time, currentValve, openValves):
    if (time, currentValve, openValves) in cache:
        return cache[(time, currentValve, openValves)]
        
    maxPressure = 0
    for neighbour in distanceMap[currentValve]:
        openValve = 1 << valveIndex[neighbour]
        if openValves & openValve: # this means this valve is already open, so continue
            continue
        remainingTime = time - (distanceMap[currentValve][neighbour] + 1)
        if remainingTime <= 0:
            continue
        maxPressure = max(maxPressure, depthFirstSearch(remainingTime, neighbour, openValves | openValve) + valvePressures[neighbour]*remainingTime)
        
    cache[(time, currentValve, openValves)] = maxPressure

    return maxPressure

print(depthFirstSearch(30, "AA", 0))

## Part 2
# I think if I were left alone in a room being fed and watered for a month with
# nothing else to do I would not have worked this out without hyper-neutrino's
# video - I have learnt a lot about bit manipulation!
# https://www.chubbydeveloper.com/bit-manipulation-python/

b = (1 << len(activeValves)) - 1
#print(bin(b))

totalMax = 0

for i in range((b+1) // 2):
    totalMax = max(totalMax, depthFirstSearch(26, "AA", i) + depthFirstSearch(26, "AA", b ^ i))

print(totalMax)