file1 = open('input.txt', 'r')
Lines = file1.readlines()

aim=0
depth = 0
horizontalPosition=0

for line in Lines:
    command, distance = line.split()
    if command == "forward":
        horizontalPosition = horizontalPosition + int(distance)
        depth = depth + (aim * int(distance))
    if command == "up":
        aim = aim - int(distance)
    if command == "down":
        aim = aim + int(distance)

print("Depth: " + str(depth) + "\nHorizontal Position: " + str(horizontalPosition) + "\nAnswer: " + str(depth * horizontalPosition))

