file1 = open("AdventOfCodeDay6.txt", "r")
lines = file1.readlines()


Fish = lines[0].split(",")
for i in range(len(Fish)):
    Fish[i] = int(Fish[i])
#Optimization:
fish = []

for z in range(1, 10):
    num = 0
    for i in range(len(Fish)):
        if Fish[i] == z:
            num += 1
    fish.append([z, num])
print(fish)

for days in range(256):

    newFish = 0
    length = 0
    """for z in range(len(fish) - 1):
        length += fish[z][1]
    print(length)"""

    for i in range(len(fish)):

        fish[i][0] = fish[i][0] - 1

    if fish[0][0] == -1:
        newFish = fish[0][1]
        fish[0][0] = 6
        temp = fish[0][1]
        fish.pop(0)

        fish[6][1] += temp

        fish[8][1] += newFish
    print(fish)
    fish.append([9,0])
    print("\n")

total = 0
for i in range(len(fish)):
    total = total + fish[i][1]

print(total)

file1.close()