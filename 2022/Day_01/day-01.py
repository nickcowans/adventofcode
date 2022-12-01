with open("input.txt", "r") as f:
    data = f.read()

elves = data.split("\n\n")
cals = []

for i in range(0, len(elves)-1):
    cals.append(sum([int(j) for j in elves[i].split("\n")]))

cals.sort(reverse=True)
print(cals[0]) # Part 1
print(sum(cals[0:3])) # Part 2