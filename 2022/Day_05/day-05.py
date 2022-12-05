#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    data = f.read()

cratesData,moves = data.split("\n\n")[0],data.split("\n\n")[1]

noStacks = cratesData.count("\n")
noInstructions = moves.count("\n")

cratesRows = cratesData.split("\n")
noCrates = int((len(cratesRows[0])+1)/4)

def crateMoves(part=1):
    crateNo = 1
    allStacks = []

    for i in range(noCrates):
        crateNo = crateNo + i
        thisStack = []
        for j in range(noStacks):
            if(cratesRows[j][(4*i)+1] != " "):
                thisStack.append(cratesRows[j][(4*i)+1])
        allStacks.append(thisStack)

    movesList=moves.split(("\n"))

    for i in range(noInstructions):
        command = [int(movesList[i].split(" ")[1]),int(movesList[i].split(" ")[3]),int(movesList[i].split(" ")[5])]
        inprog = allStacks[command[1]-1][0:(command[0])] # what to move
        if(part==1):
            inprog.reverse() # reverse it (part 1 only)
        curLeng = len(allStacks[command[1]-1])
        toleave = allStacks[command[1]-1][(command[0]):curLeng] # what to leave
        allStacks[command[1]-1] = toleave 
        allStacks[command[2]-1] = inprog + allStacks[command[2]-1]

    answer=""

    for k in range(len(allStacks)):
        answer+=str(allStacks[k][0])

    return answer

print(crateMoves(1))
print(crateMoves(2))