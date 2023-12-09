input = open("in.txt").read().strip().split('\n\n')# Read in the input

seeds=[int(seed) for seed in input[0].split("seeds: ")[1].split()]
instructions=input[1:]

def inOut(D, S, R, inVal):
    if((int(inVal) >= int(S)) & (int(inVal) < (int(S)+int(R)))):
        outVal=int(D)+int(inVal)-int(S)
        return outVal
    else:
        return False

finals=[]
for inVal in seeds:
    for instruction in instructions:
        mapName,mapCodes=instruction.split(':\n')
        mapCodesList=mapCodes.split('\n')
        newVal = False
        i = 0
        maxI = len(mapCodesList)
        while (newVal == False and i < maxI):
            D, S, R = mapCodesList[i].split() # Destination Start, Source Start, Range
            newVal = inOut(D, S, R, inVal)
            i+=1
        if newVal == False:
            newVal = inVal
        inVal=newVal
    finals.append(newVal)    

print("Part1:", min(finals))