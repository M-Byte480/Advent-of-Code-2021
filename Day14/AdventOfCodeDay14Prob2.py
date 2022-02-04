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

combinations = Counter()
letter = Counter(input)

for combo in range(len(input)-1):
    combinations[str(input[combo]+input[combo+1])]+= 1
print(lines)

for step in range(40):
    updatedCombinations = Counter()
    for count, value in enumerate(combinations):
        letter.update({lines[z][1] for z in range(len(lines)) if value == lines[z][0]})
        for element in lines:
            if value == element[0]:
                    updatedCombinations.update({str(value[0]+element[1])})

                    updatedCombinations.update({str(element[1]+value[1])})
                    print(str(value[0]+element[1])+ ","+ str(element[1]+value[1]), end=" ")
                    break
    combinations = Counter()
    combinations.update(updatedCombinations)

print(letter)
