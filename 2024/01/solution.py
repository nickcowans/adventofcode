input = open("in.txt").read().strip()  # Read in the input

list1 = []
list2 = []

for line in input.split("\n"):  # For each line
    a, b = line.split("   ")
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

i = 0
x = 0
while i < len(list1):
    x += abs(list1[i] - list2[i])
    i += 1

print("Part1: ", x)

list1 = []
list2 = []

for line in input.split("\n"):  # For each line
    a, b = line.split("   ")
    list1.append(int(a))
    list2.append(int(b))

counts = [list2.count(value) for value in list1]

i = 0
x = 0
while i < len(list1):
    x += list1[i] * counts[i]
    i += 1

print("Part2: ", x)
