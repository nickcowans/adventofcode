input = open("in.txt").read().strip() # Read in the input

cubes = {"red": 12, "green": 13, "blue": 14}

possibleGames=0
overallPower=0

for game, line in enumerate(input.split('\n')):  # For each line
    include=1
    gameCubes = {"red": 0, "green": 0, "blue": 0}
    for gameSet in line.split(': ')[1].split('; '):
        for setCubes in gameSet.split(', '):
            num, color = setCubes.split()
            if int(num) > cubes[color]:
                include=0
            gameCubes[color] = max(int(num), gameCubes[color])
    if(include==1):
        possibleGames+=int(game+1)
    overallPower+=gameCubes['red']*gameCubes['green']*gameCubes['blue']

print("Part 1:", possibleGames)
print("Part 2:", overallPower)