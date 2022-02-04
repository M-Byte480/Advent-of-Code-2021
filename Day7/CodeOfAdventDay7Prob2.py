file1 = open("AdventOfCodeDay7.txt", "r")
Lines = file1.readlines()
Whales = Lines[0].split(",")
#import sys
#sys.setrecursionlimit(1500)
for i in range(len(Whales)):
    Whales[i] = int(Whales[i])

def recursion(n):
    increment = 0
    for i in range(1, n+1):
        increment += i
    return increment

def sumatpoint (input, whale):
    #
    if input > whale:
        difference = input-whale
    else:
        difference = whale-input

    return recursion(difference)


fuelpositions =[]
for position in range(1, int(max(Whales))+1):
    sum = 0
    for whale in range(len(Whales)):
        sum += sumatpoint(position, Whales[whale])
    fuelpositions.append(sum)

print(Whales)
print(int(min(fuelpositions)), " is the cheapeast fuel, in position: ", fuelpositions.index(min(fuelpositions)) + 1)





file1.close()
