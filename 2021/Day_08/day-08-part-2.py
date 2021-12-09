import numpy as np

fileName = "input.txt"
#fileName = "example.txt"
fullString = 'abcdefg'

totalSum = 0

with open(fileName, "r") as f:
    data = f.readlines()

for line in data:
    thisRowIn = line.split("|")[0].replace('\n', '').split(" ")
    thisRowOut = line.split("|")[1].replace('\n', '').split(" ")
    #print(thisRowIn, thisRowOut)
    fiveSeg = sixSeg = ""
    for i in range(0,10):
        if len(thisRowIn[i]) == 2:
            dig1=thisRowIn[i]
        elif len(thisRowIn[i]) == 3:
            dig7=thisRowIn[i]
        elif len(thisRowIn[i]) == 4:
            dig4=thisRowIn[i]
        elif len(thisRowIn[i]) == 7:
            dig8=thisRowIn[i]
        elif len(thisRowIn[i]) == 5:
            fiveSeg = fiveSeg+thisRowIn[i]
        elif len(thisRowIn[i]) == 6:
            sixSeg = sixSeg+thisRowIn[i]

    segA = ''.join(set(dig7).difference(dig1))
    segB = segD = ''.join(set(dig4).difference(dig7))
    segC = segF = ''.join(set(dig4).intersection(dig7))
    segSoFar = segA + segB + segC
    segE = segG = ''.join(set(fullString).difference(segSoFar))

    BEContender = CDEContender = ""
    for i in range(0, 7):
        if fiveSeg.count(fullString[i]) == 1:
            BEContender = BEContender + fullString[i]
        if sixSeg.count(fullString[i]) == 2:
            CDEContender = CDEContender + fullString[i]
        
    segB = ''.join(set(segB).intersection(BEContender))
    segE = ''.join(set(segE).intersection(BEContender))
    CDEContender = ''.join(set(CDEContender).difference(segE))
    segC = ''.join(set(segC).intersection(CDEContender))
    segD = ''.join(set(segD).intersection(CDEContender))
    segSoFar = segA + segB + segC + segD + segE
    segF = ''.join(set(segF).difference(segSoFar))
    segG = ''.join(set(segG).difference(segSoFar))

    #print(segA, segB, segC, segD, segE, segF, segG)
 
    print0 = segA + segB + segC        + segE + segF + segG
    print1 =               segC               + segF
    print2 = segA        + segC + segD + segE        + segG
    print3 = segA        + segC + segD        + segF + segG
    print4 =        segB + segC + segD        + segF
    print5 = segA + segB        + segD        + segF + segG
    print6 = segA + segB        + segD + segE + segF + segG
    print7 = segA        + segC               + segF
    print8 = segA + segB + segC + segD + segE + segF + segG
    print9 = segA + segB + segC + segD        + segF + segG

    finalOut = ""
    for i in range(1,5):
        if set(thisRowOut[i]) == set(print0):
            finalOut = finalOut + "0"
        if set(thisRowOut[i]) == set(print1):
            finalOut = finalOut + "1"
        if set(thisRowOut[i]) == set(print2):
            finalOut = finalOut + "2"
        if set(thisRowOut[i]) == set(print3):
            finalOut = finalOut + "3"
        if set(thisRowOut[i]) == set(print4):
            finalOut = finalOut + "4"
        if set(thisRowOut[i]) == set(print5):
            finalOut = finalOut + "5"
        if set(thisRowOut[i]) == set(print6):
            finalOut = finalOut + "6"
        if set(thisRowOut[i]) == set(print7):
            finalOut = finalOut + "7"
        if set(thisRowOut[i]) == set(print8):
            finalOut = finalOut + "8"
        if set(thisRowOut[i]) == set(print9):
            finalOut = finalOut + "9"

    totalSum = totalSum + int(finalOut)

print(totalSum)