with open("input.txt", "r") as f:
    data = f.readlines()

fileSize = len(data)

maxcal = [0,0,0]
thiscal = 0

for i in range(0, fileSize):
    if data[i] == "\n":
        if thiscal > maxcal[0]:
            maxcal[0] = thiscal
        elif thiscal > maxcal[1]:
            maxcal[1] = thiscal
        elif thiscal > maxcal[2]:
            maxcal[2] = thiscal
        maxcal.sort()
        thiscal = 0
    else:
        thiscal = thiscal + int(data[i].rstrip())

print(maxcal)
print(sum(maxcal))