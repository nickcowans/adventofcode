#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    data = f.read()

mesLen = len(data)

def elfFunction(m):
    n=m-1
    for i in range(n, (mesLen-1)):
        test = data[(i-n):(i+1)]
        lets = []
        for j in range(m):
            lets.append(test[j])
        letSet = set(lets)
        if (len(letSet)==m):
            print(i+1, letSet)
            break

elfFunction(4) # part1
elfFunction(14) # part2