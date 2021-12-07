import numpy as np

with open("input.txt", "r") as f:
    data = f.readlines()

fileSize = len(data)
numCards = int((fileSize - 1)/6)

# First line is the winning numbers
winningNumbers = data[0].split(",")

# Create empty list to mark off when correct 
markingList = [0] * numCards * 5 * 5
won = False

for winningNumber in winningNumbers:

    if won == False:
        cardStart = 2
        numIndex = 0

        while cardStart < fileSize - 1:
            for cardLine in range(cardStart, cardStart+5):
                for cardNum in data[cardLine].split():
                    if int(cardNum) == int(winningNumber):
                        markingList[numIndex] = 1
                    numIndex = numIndex + 1

            cardStart = cardStart + 6
        
        # Check if won
        markingMatrix=np.reshape(markingList, (numCards * 5, 5)) 
        startRow=0

        while startRow < int((fileSize-2)/6)*5 and won == False:
            cardMatrix = markingMatrix[startRow:startRow+5][0:5]
            rowScore = np.sum(cardMatrix, axis=1)
            colScore = np.sum(cardMatrix, axis=0)
            if max(rowScore) == 5 or max(colScore) == 5:
                won = True
                winningRow = startRow
                winningMarkingMatrix = cardMatrix
                theWinningNumber = winningNumber
            startRow = startRow+5

# make a nice list of the cards
niceList = [0] * numCards * 5 * 5
cardStart = 2
numIndex = 0

while cardStart < fileSize - 1:
    for cardLine in range(cardStart, cardStart+5):
        for cardNum in data[cardLine].split():
            niceList[numIndex] = int(cardNum)
            numIndex = numIndex + 1
 
    cardStart = cardStart + 6

winningCard = np.reshape(niceList, (numCards * 5, 5))[winningRow:winningRow+5]

print(int(theWinningNumber)*(sum(sum(winningCard*(1-winningMarkingMatrix)))))