with open("input.txt", "r") as f:
    data = f.readlines()

fileSize = len(data)

maxcal = 0
thiscal = 0

for i in range(0, fileSize):
    if data[i] == "\n":
        if thiscal > maxcal:
            maxcal = thiscal
        thiscal = 0
    else:
        thiscal = thiscal + int(data[i].rstrip())

print(maxcal)