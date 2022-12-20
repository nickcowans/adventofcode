#!/usr/local/bin/python3

with open("input.txt", "r") as f:
    paths = f.read().strip().split("\n")

## Paths
abyss = 0

# Build a set of blocked spaces
blocked = set()  # Start off with empty set
for path in paths:
    coords = [list(map(int, xy.split(","))) for xy in path.split(" -> ")] 
    for coord1, coord2 in zip(coords, coords[1:]):     # create pairs of coordinates by zipping in a clever way
        startX, endX = sorted([coord1[0], coord2[0]])  # Sort to make sure start with smallest value ...
        startY, endY = sorted([coord1[1], coord2[1]])  # ... regardless of which order they appear
        for x in range(startX, endX+1):                # This will loop across a rectangle where ...
            for y in range(startY, endY+1):            # ... one dimension has width of 1
                blocked.add((x, y))                    # add rock to blocked set (is a set so avoids issues with duplicates)
                abyss = max(abyss, y+1)                # the abyss is below (higher number) than lowest rock

rocks=list(blocked) # for diagram

## Sand
grain=0
keepGoing=True

while keepGoing:
    sand=(500,0)
    while True:
        if sand[1] > abyss: # abysmal! 
            print(grain)
            keepGoing = False
            break
        if (sand[0], sand[1]+1) not in blocked:
            sand=(sand[0], sand[1]+1)
            continue
        if (sand[0]-1, sand[1]+1) not in blocked:
            sand=(sand[0]-1, sand[1]+1)
            continue
        if (sand[0]+1, sand[1]+1) not in blocked:
            sand=(sand[0]+1, sand[1]+1)
            continue
        grain+=1
        blocked.add((sand[0],sand[1]))
        break

# Diagram
xmin,xmax=sorted([x for x,y in blocked])[::len(blocked)-1]
ymin,ymax=sorted([y for x,y in blocked])[::len(blocked)-1]

with open("top.html", "r") as f:
    print(f.read())

for y in range(0, ymax+1):
    print("<div><div class='block' style='width: 12px'>"+str(y)+"</div>")
    for x in range(xmin, xmax+1):
        if (x,y) in blocked and (x,y) in rocks:
            print("<div class='block rock'></div>")
        elif (x,y) in blocked:
            print("<div class='block sand'></div>")
        else:
            print("<div class='block air'></div>")
    print("</div>")

print("</body></html>")