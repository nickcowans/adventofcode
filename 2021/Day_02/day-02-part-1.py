file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
depth = 0
horizontalPosition=0

for line in Lines:
    command, distance = line.split()
    if command == "forward":
        horizontalPosition = horizontalPosition + int(distance)
    if command == "up":
        depth = depth - int(distance)
    if command == "down":
        depth = depth + int(distance)

print("Depth: " + str(depth) + "\nHorizontal Position: " + str(horizontalPosition) + "\nAnswer: " + str(depth * horizontalPosition))

