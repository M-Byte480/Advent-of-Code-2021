file1 = open("AdventOfCodeDay7.txt", "r")
Lines = file1.readlines()
Whales = Lines[0].split(",")
for i in range(len(Whales)):
    Whales[i] = int(Whales[i])

def sumatpoint (input, whale):
    if input > whale:
        return input-whale
    else:
        return whale-input

fuelpositions =[]
for position in range(1, int(max(Whales))+1):
    sum = 0
    for whale in range(len(Whales)):
        sum += sumatpoint(position, Whales[whale])
    fuelpositions.append(sum)

print(Whales)
print(int(min(fuelpositions)), " is the cheapeast fuel, in position: ", fuelpositions.index(min(fuelpositions)) + 1)





file1.close()
