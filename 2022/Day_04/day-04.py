#!/usr/local/bin/python3
with open("input.txt", "r") as f:
    data = f.read()

pairs = data.split("\n")

count1 = 0
count2 = 0

for i in range(len(pairs)-1):
    e1,e2 = pairs[i].split(",")[0],pairs[i].split(",")[1]
    e1s,e1e = int(e1.split("-")[0]),int(e1.split("-")[1])
    e2s,e2e = int(e2.split("-")[0]),int(e2.split("-")[1])
    e1r = set(list(range(e1s,e1e+1)))
    e2r = set(list(range(e2s,e2e+1)))
    over = set(list(e1r & e2r))
    if (e1r == over) or (e2r == over):
        count1+=1
    if over != set():
        count2+=1  

print(count1) # Part 1
print(count2) # Part 2
