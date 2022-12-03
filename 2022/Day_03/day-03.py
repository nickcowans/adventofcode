with open("input.txt", "r") as f:
    data = f.read()

rucksacks = data.split("\n")
alphabetmap = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
common1 = []
common2 = []

for i in range(len(rucksacks)-1):
    comp1, comp2 = rucksacks[i][:len(rucksacks[i])//2], rucksacks[i][len(rucksacks[i])//2:]
    common1.append(alphabetmap.get(''.join(set(comp1).intersection(comp2))))

i = 0
while i < len(rucksacks)-1:
    comp1, comp2, comp3 = rucksacks[i], rucksacks[i+1], rucksacks[i+2]
    at1 = ''.join(set(comp1).intersection(comp2))
    at2 = ''.join(set(at1).intersection(comp3))
    common2.append(alphabetmap.get(at2))
    i = i + 3


print(sum(common1)) # part 1
print(sum(common2)) # part 2