#!/usr/local/bin/python3
import numpy as np
with open("input.txt", "r") as f:
    data = f.read().strip()

instructions = data.split("\n")
move = {"L": [-1,0], "R": [1,0], "U": [0,1], "D": [0,-1]}

needCorrecting = [[ 2, 0], [-2, 0], [ 0,-2], [ 0, 2], [ 1,-2], [-1, 2], [ 2, 1], [-2,-1], [-1,-2], [ 1, 2], [ 2,-1], [-2, 1], [-2,-2], [ 2, 2], [-2, 2], [ 2,-2]]
correction     = [[-1, 0], [ 1, 0], [ 0, 1], [ 0,-1], [-1, 1], [ 1,-1], [-1,-1], [ 1, 1], [ 1, 1], [-1,-1], [-1, 1], [ 1,-1], [ 1, 1], [-1,-1], [ 1,-1], [-1, 1]]

rope = np.array([[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]])

tail2History = [list(rope[1])]
tail9History = [list(rope[9])]

for instruction in instructions:
    direction, distance = instruction.split()
    for step in range(int(distance)):
        rope[0] = rope[0]+np.array(move.get(direction))
        for segment in range(len(rope)-1):
            tailDist = rope[segment+1]-rope[segment]
            if list(tailDist) in needCorrecting:
                rope[segment+1] = rope[segment+1]+np.array(correction[needCorrecting.index(list(tailDist))])
        tail2History.append(list(rope[1]))
        tail9History.append(list(rope[9]))

uniqueTail2History = [list(x) for x in set(tuple(x) for x in tail2History)]
print(len(uniqueTail2History))
uniqueTail9History = [list(x) for x in set(tuple(x) for x in tail9History)]
print(len(uniqueTail9History))