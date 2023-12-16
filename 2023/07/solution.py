from collections import Counter

input = open("in.txt").read().strip().split("\n")  # Read in the input


def valueHand(hand):
    handValues = list(Counter(hand).values())

    rankings = {
        5: 6,  # Five of a kind
        4: 5,  # Four of a kind
        3: 4 if 2 in handValues else 3,  # Full house or Three of a kind
        2: 2 if handValues.count(2) == 2 else 1,  # Two pair or One pair
        1: 0,  # High card
    }

    if hand == "":
        return 0
    else:
        return rankings.get(max(handValues), 0)


games = []
for game in input:
    hand, bid = game.split()
    handTranslate = hand.translate(str.maketrans("TJQKA", "BCDEF"))
    games.append([valueHand(hand), handTranslate, hand, int(bid)])

sortedGames = sorted(games, key=lambda x: (x[0], x[1]))

value = 0
for i in range(0, len(sortedGames)):
    value += (i + 1) * sortedGames[i][3]

print("Part1:", value)

### PART 2

games2 = []
for game2 in input:
    hand, bid = game2.split()
    handTranslate1 = hand.translate(str.maketrans("TJQKA", "B1DEF"))
    handTranslate2 = hand.replace("J", "")

    newHandLen = len(handTranslate2)
    currentHandValue = valueHand(handTranslate2)
    # if 4 of kind (5) and length = 4 then now 5 of kind (6)
    if currentHandValue == 5 and newHandLen == 4:
        newHandValue = 6
    # full house only possible with 5
    # if 3 of kind (3) and length = 4 then now 4 of kind (5)
    elif currentHandValue == 3 and newHandLen == 4:
        newHandValue = 5
    # if 3 of kind (3) and length = 3 then now 5 of kind (6)
    elif currentHandValue == 3 and newHandLen == 3:
        newHandValue = 6
    # if 2 pair (2) and length = 4 then now full house (4)
    elif currentHandValue == 2 and newHandLen == 4:
        newHandValue = 4
    # if pair (1) and length 4 then now 3 of kind (3)
    elif currentHandValue == 1 and newHandLen == 4:
        newHandValue = 3
    # if pair (1) and length 3 then now 4 of kind (5)
    elif currentHandValue == 1 and newHandLen == 3:
        newHandValue = 5
    # if pair (1) and length 2 then now 5 of kind (6)
    elif currentHandValue == 1 and newHandLen == 2:
        newHandValue = 6
    # if highcard (0) and length 4 then now pair (1)
    elif currentHandValue == 0 and newHandLen == 4:
        newHandValue = 1
    # if highcard (0) and length 3 then now 3 of kind (3)
    elif currentHandValue == 0 and newHandLen == 3:
        newHandValue = 3
    # if highcard (0) and length 2 then now 4 of kind (5)
    elif currentHandValue == 0 and newHandLen == 2:
        newHandValue = 5
    # if highcard (0) and length 1 then now 5 of kind (6)
    elif currentHandValue == 0 and newHandLen == 1:
        newHandValue = 6
    elif newHandLen == 0:
        newHandValue = 6
    else:
        newHandValue = currentHandValue

    games2.append(
        [
            newHandValue,
            handTranslate1,
            handTranslate2,
            hand,
            int(bid),
        ]
    )

sortedGames2 = sorted(games2, key=lambda x: (x[0], x[1]))


value = 0
for i in range(0, len(sortedGames2)):
    value += (i + 1) * sortedGames2[i][4]

print("Part2:", value)
