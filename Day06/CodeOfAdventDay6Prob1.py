file1 = open("AdventOfCodeDay6.txt", "r")
lines = file1.readlines()


Fish = lines[0].split(",")
for i in range(len(Fish)):
    Fish[i] = int(Fish[i])

for days in range(80):
    length = len(Fish)
    for i in range(length):
        Fish[i] = Fish[i] - 1
        if Fish[i] == -1:
            Fish[i] = 6
            Fish.append(8)

total = len(Fish)
print(total)

file1.close()