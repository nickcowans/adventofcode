#!/usr/local/bin/python3
import re
from collections import deque
with open("example.txt", "r") as f:
    blueprints = f.read().strip().split("\n")

blueprintData = []

for blueprint in blueprints:
    blueprintNumber, oreCostOre, clayCostOre, obsidianCostOre, obsidianCostClay, geodeCostOre, geodeCostObsidian = (map(int, re.findall(r'[0-9]+',blueprint)))
    blueprintData.append([blueprintNumber, [[oreCostOre,0,0,0], [clayCostOre,0,0,0], [obsidianCostOre, obsidianCostClay,0,0], [geodeCostOre, 0,geodeCostObsidian,0]]])
    #blueprintData.append({"blueprintNumber": blueprintNumber, "oreCostOre": oreCostOre, "clayCostOre": clayCostOre, "obsidianCostOre": obsidianCostOre, "obsidianCostClay": obsidianCostClay, "geodeCostOre": geodeCostOre, "geodeCostObsidian": geodeCostObsidian})

def dfs(blueprint, time, robots, assets):
    maxGeode=0
    while time:
        newRobotOptions = [False,False,False,False]
        for i in range(len(blueprint[1])):
            planCost = [a >= b for a, b in zip(assets, blueprint[1][i])]
            if sum(planCost) == 4: 
                newRobotOptions[i] = True
        robotIndex = 0
        for robot in robots:
            if robot:
                assets[robotIndex] += robot
            robotIndex+=1
        if time <= 0:
            return max(maxGeode,assets[3])
        print(time, robots, assets, newRobotOptions)
        for i in range(len(newRobotOptions)):
            if newRobotOptions[i]:
                robots[i] +=1
                for j in range(len(assets)):
                     assets[j]-=blueprint[1][i][j]
                dfs(blueprint, time-1, robots, assets)
        time -=1

for blueprint in blueprintData:
    robots = [1,0,0,0] # oreRobot, clayRobot, obsidianRobot, geodeRobot
    assets = [0,0,0,0] # ore, clay, obsidian, geode
    print(dfs(blueprint,4, robots, assets))
    print(robots, assets)



