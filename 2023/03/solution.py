import re
input = open("in.txt").read().strip() # Read in the input

nRow = input.count('\n')+1
nCol = input.find('\n')

modifiedInput = ''
for lineNo, line in enumerate(input.split('\n')):
    if lineNo == 0:
        modifiedInput+='.'*nRow+'..\n.'+line+'.\n'
    elif lineNo == nRow-1:
        modifiedInput+='.'+line+'.\n'+'.'*nRow+'..'
    else:
        modifiedInput+='.'+line+'.\n'

numberList = []
thisNumLen = 0

part1=0

for lineNo, line in enumerate(modifiedInput.split('\n')):  # For each line
    for colNo, char in enumerate(line):
        if thisNumLen > 0:
            thisNumLen=thisNumLen-1
            continue
        if char.isdigit():
            thisNum = char
            thisNumLen = 1
            # 1 figure out whole number
            for i in range(colNo+1, nCol+1):
                if modifiedInput.split('\n')[lineNo][i].isdigit():
                    thisNum+=modifiedInput.split('\n')[lineNo][i]
                    thisNumLen+=1
                else:
                    break
            isValid = False
            for x in range(colNo-1,colNo+thisNumLen+1):
                if ((modifiedInput.split('\n')[lineNo-1][x].isdigit()==False) & (modifiedInput.split('\n')[lineNo-1][x]!='.')):
                    isValid = True
                    symbol = modifiedInput.split('\n')[lineNo-1][x]
                    break
                if ((modifiedInput.split('\n')[lineNo+1][x].isdigit()==False) & (modifiedInput.split('\n')[lineNo+1][x]!='.')):
                    isValid = True
                    symbol = modifiedInput.split('\n')[lineNo+1][x]
                    break
            if((modifiedInput.split('\n')[lineNo][colNo-1].isdigit()==False) & (modifiedInput.split('\n')[lineNo][colNo-1]!='.')):
                isValid = True
                symbol = modifiedInput.split('\n')[lineNo][colNo-1]
            if((modifiedInput.split('\n')[lineNo][colNo+thisNumLen].isdigit()==False) & (modifiedInput.split('\n')[lineNo][colNo+thisNumLen]!='.')):
                isValid = True
                symbol = modifiedInput.split('\n')[lineNo][colNo+thisNumLen]
            if isValid:
                part1+=int(thisNum)

print('Part1:',part1)

part2=0

for lineNo, line in enumerate(modifiedInput.split('\n')):  # For each line
    for colNo, char in enumerate(line):
        if(char=='*'):
            parts=[]
            thisDig=""
            firstDig=0
            for y in range(lineNo-1,lineNo+2):
                catch1=0
                for x in range(colNo-1,colNo+2):
                    if catch1>=x:
                        continue   # to avoid repeats
                    num=modifiedInput.split('\n')[y][x]
                    goLeft = True
                    firstDig = x
                    if(num.isdigit()):
                        while(goLeft):
                            if(modifiedInput.split('\n')[y][firstDig-1].isdigit()):
                                firstDig-=1
                            else:
                                goLeft=False
                        goRight = True
                        thisDig=modifiedInput.split('\n')[y][firstDig]
                        while(goRight):
                            if(modifiedInput.split('\n')[y][firstDig+1].isdigit()):
                                thisDig=thisDig+modifiedInput.split('\n')[y][firstDig+1]
                                firstDig+=1
                            else:
                                goRight=False
                                catch1=firstDig
                    if thisDig != "":
                        parts.append(thisDig)
                        thisDig=""
            if(len(parts) ==2):
               part2+=int(parts[0])*int(parts[1])

print('Part2:',part2)
