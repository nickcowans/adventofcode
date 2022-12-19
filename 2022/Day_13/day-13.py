#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    pairs = f.read().strip().split("\n\n")

verbose=False # for understanding / debugging

def determineOrder(a, b, verbose=verbose):
    if type(a)==int and type(b)==int:
        print("Both int -- RETURN (a-b):", a-b) if verbose else ""
        print("CONTINUE: a and b equal") if verbose and (a-b == 0) else ""
        return a-b # negative (right order) if first integer smaller
    elif type(a)==int and type(b)==list:
        print("Only b is list") if verbose else ""
        return determineOrder([a], b) # Make a list and run through function
    elif type(a)==list and type(b)==int:
        print("Only a is list") if verbose else ""
        return determineOrder(a, [b]) # Make n list and run through function
    
    print("Both lists") if verbose else ""
    itemInList =0
    for a1,b1 in zip(a,b): # both lists - zip together...
        itemInList +=1
        print("Item",itemInList, "A:", a1, "B:", b1) if verbose else ""
        _ = determineOrder(a1,b1)
        if _: # and if running through function produces non zero ...
            return _ # return it
            
    print("All pairs in list were equal: RETURN (len(a) - len(b)):",a,b, len(a)-len(b)) if verbose else ""
    print("CONTINUE: a and b same length") if verbose and (len(a)-len(b) == 0) else ""
    return len(a)-len(b) # if running through list results in only zeros (the same), then return diff in length

# Part 1
index=1
rightOrder=0
for pair in pairs:
    pair1,pair2 = (eval(_) for _ in pair.split("\n"))
    print("! Index:", index, "Pair1:", pair1, "Pair2:", pair2) if verbose else ""
    if determineOrder(pair1, pair2) < 0 :
        rightOrder+=index
    index+=1

print(rightOrder)

# Part 2
allPairs = []
for pair in pairs:
    pair1,pair2 = (eval(_) for _ in pair.split("\n"))
    allPairs.append(pair1)
    allPairs.append(pair2)

allPairs.append([[2]])
allPairs.append([[6]])

currentPair = 0
maxPair = 0

while currentPair < len(allPairs)-1:
    a,b = allPairs[currentPair],allPairs[currentPair+1]
    maxPair = max(maxPair, currentPair)
    if(determineOrder(a,b)) > 0:
        allPairs[currentPair] = b
        allPairs[currentPair+1] = a
        currentPair = max(0, currentPair-1)
    else:
        currentPair = maxPair+1

print((allPairs.index([[2]])+1)*(allPairs.index([[6]])+1))
