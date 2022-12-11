#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    data = f.read().strip()

monkeyData = data.split("\n\n")

items1=[]
items2=[]
operations=[]
tests=[]
trues=[]
falses=[]

for monkey in range(len(monkeyData)):
    items1.append(list(map(int,monkeyData[monkey].split("\n")[1].split(": ")[1].split(", "))))
    items2.append(list(map(int,monkeyData[monkey].split("\n")[1].split(": ")[1].split(", "))))
    operations.append(monkeyData[monkey].split("\n")[2].split("= old ")[1].split())
    tests.append(monkeyData[monkey].split("\n")[3].split("divisible by ")[1])
    trues.append(monkeyData[monkey].split("\n")[4].split("throw to monkey ")[1])
    falses.append(monkeyData[monkey].split("\n")[5].split("throw to monkey ")[1])

inspectsItems1=[0 for _ in range(len(monkeyData))]
inspectsItems2=[0 for _ in range(len(monkeyData))]

commonMultiplier = 1
for test in tests:
    commonMultiplier *= int(test)

def runPart(part=1, noRounds=20, items=items1, inspectsItems=inspectsItems1):
    for _ in range(noRounds):
        for monkey in range(len(monkeyData)):
            for item in items[monkey]:
                inspectsItems[monkey]+=1
                mult = item if operations[monkey][1]=="old" else int(operations[monkey][1])
                new = item+mult if operations[monkey][0]=="+" else item*mult
                new = new // 3 if part==1 else new % commonMultiplier # only remainder of common multipler matters
                newMonkey = int(trues[monkey]) if new % int(tests[monkey]) == 0 else int(falses[monkey])
                items[newMonkey].append(new)
            items[monkey]=[]
    return sorted(inspectsItems,reverse=True)[0]*sorted(inspectsItems,reverse=True)[1]

print(runPart(part=1, noRounds=20, items=items1, inspectsItems=inspectsItems1))
print(runPart(part=2, noRounds=10000, items=items2, inspectsItems=inspectsItems2))