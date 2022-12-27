#!/usr/local/bin/python3
import re
from collections import deque
with open("example.txt", "r") as f:
    blueprints = f.read().strip().split("\n")

blueprintData = []

for blueprint in blueprints:
    blueprintNumber, oreCostOre, clayCostOre, obsidianCostOre, obsidianCostClay, geodeCostOre, geodeCostObsidian = (map(int, re.findall(r'[0-9]+',blueprint)))
    blueprintData.append([blueprintNumber, oreCostOre, clayCostOre, obsidianCostOre, obsidianCostClay, geodeCostOre, geodeCostObsidian])
    #blueprintData.append({"blueprintNumber": blueprintNumber, "oreCostOre": oreCostOre, "clayCostOre": clayCostOre, "obsidianCostOre": obsidianCostOre, "obsidianCostClay": obsidianCostClay, "geodeCostOre": geodeCostOre, "geodeCostObsidian": geodeCostObsidian})

asserts = [0,0,0,0] # ore, clay, obsidian, geode

for blueprint in blueprintData:
    print(blueprint)