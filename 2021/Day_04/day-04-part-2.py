import numpy as np

with open("input.txt", "r") as f:
    data = f.readlines()

fileSize = len(data)
numCards = int((fileSize - 1)/6)

# First line is the winning numbers
winningNumbers = data[0].split(",")

# Create empty list to mark off when correct 
markingList = [0] * numCards * 5 * 5
cardsWon=0
winningCards = [0] * numCards

for winningNumber in winningNumbers:

    if cardsWon <= numCards:
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

        while startRow <= int((fileSize-2)/6)*5 and cardsWon <= numCards:
            cardMatrix = markingMatrix[startRow:startRow+5][0:5]
            rowScore = np.sum(cardMatrix, axis=1)
            colScore = np.sum(cardMatrix, axis=0)
            if max(rowScore) == 5 or max(colScore) == 5:
                if startRow not in winningCards:
                    winningCards[cardsWon] = startRow
                    cardsWon = cardsWon + 1
                    winningMarkingMatrix = cardMatrix
                    theWinningNumber = winningNumber
            startRow = startRow+5

print(winningCards)
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

# Sort of lost the plot at this point... but this works (not sure why it is 98 and no 100?)
winningCard = np.reshape(niceList, (numCards * 5, 5))[winningCards[98]:winningCards[98]+5]

print(int(theWinningNumber)*(sum(sum(winningCard*(1-winningMarkingMatrix)))))