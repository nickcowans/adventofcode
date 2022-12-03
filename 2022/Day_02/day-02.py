with open("input.txt", "r") as f:
    data = f.read()

games = data.split("\n")
scores1 = []
scores2 = []

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
def calcScore1(opponent, self):
    if (opponent == "A" and self == "Y") or (opponent == "B" and self == "Z") or (opponent == "C" and self == "X"):
        score1 = 6 # WIN
    elif (opponent == "A" and self == "X") or (opponent == "B" and self == "Y") or (opponent == "C" and self == "Z"):
        score1 = 3 # DRAW
    else:
        score1 = 0 # LOSE
    shapes = {"X": 1, "Y": 2, "Z": 3}
    score2 = shapes.get(self)
    return score1 + score2

# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def calcScore2(opponent, outcome):
    if (opponent == "B" and outcome == "X") or (opponent == "A" and outcome == "Y") or (opponent == "C" and outcome == "Z"):
        score2 = 1 # ROCK
    elif (opponent == "C" and outcome == "X") or (opponent == "B" and outcome == "Y") or (opponent == "A" and outcome == "Z"):
        score2 = 2 # PAPER
    else:
        score2 = 3 # SCISSORS
    outcomes = {"X": 0, "Y": 3, "Z": 6}
    score1 = outcomes.get(outcome)
    return score1 + score2

for i in range(0, len(games)-1):
    gameComp = games[i].split(" ")
    scores1.append(calcScore1(gameComp[0], gameComp[1]))
    scores2.append(calcScore2(gameComp[0], gameComp[1]))

print(sum(scores1)) # Part 1
print(sum(scores2)) # Part 2