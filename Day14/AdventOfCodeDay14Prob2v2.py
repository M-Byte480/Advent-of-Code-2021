from collections import Counter

file1 = open("AdventOfCodeDay14.txt", "r")
lines = file1.readlines()
file1.close()

for temp in range(len(lines)):
    lines[temp] = lines[temp].replace("\n","")
input = lines.pop(0)
lines.pop(0)
for temp in range(len(lines)):
    lines[temp] = lines[temp].split(" -> ")

Totalcombinations = Counter()
letter = Counter(input)

for combo in range(len(input)-1):
    Totalcombinations[str(input[combo]+input[combo+1])]+= 1

combination = Totalcombinations.copy()

for step in range(40):
    for Num, Value in enumerate(combination):
        newValues = Counter()
        for z in lines:
            if Value == z[0]:
                newValues.update({z[0][0]+z[1]})
                newValues.update({z[1]+z[0][1]})

        Totalcombinations.update(newValues)
    combination = newValues.copy()

print(len(Totalcombinations))
for Num, Value in enumerate(Totalcombinations):
    for z in range(len(lines)):
        if Value == lines[z][0]:
            letter.update({lines[z][1]:Totalcombinations.get(Value)})
    # letter.update({lines[z][1] for z in range(len(lines)) if Value == lines[z][0]})

print(Totalcombinations)
print(letter)