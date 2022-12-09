import numpy as np
with open("example.txt", "r") as f:
    data = f.read().strip()

instructions = data.split("\n")

move = {"L": [-1,0], "R": [1,0], "U": [0,1], "D": [0,-1]}

needCorrecting = [[ 2, 0], [-2, 0], [ 0,-2], [ 0, 2], [ 1,-2], [-1, 2], [ 2, 1], [-2,-1], [-1,-2], [ 1, 2], [ 2,-1], [-2, 1]]
correction     = [[-1, 0], [ 1, 0], [ 0, 1], [ 0,-1], [-1, 1], [ 1,-1], [-1,-1], [ 1, 1], [ 1, 1], [-1,-1], [-1, 1], [ 1,-1]]

head = np.array([0,0])
tail = np.array([0,0])

headHistory = [list(head)]
tailHistory = [list(tail)]

for instruction in instructions:
    direction, distance = instruction.split()
    for step in range(int(distance)):
        head = head+np.array(move.get(direction))
        headHistory.append(list(head))
        tailDist = tail-head
        #print("::", head,tail,tailDist,list(tailDist) in needCorrecting)
        if list(tailDist) in needCorrecting:
            tail = tail+np.array(correction[needCorrecting.index(list(tailDist))])
            tailHistory.append(list(tail))
            #print(":MOVED:", head,tail,tailDist,list(tailDist) in needCorrecting)


uniqueTailHistory = [list(x) for x in set(tuple(x) for x in tailHistory)]
print(len(uniqueTailHistory), ": ", tailHistory)