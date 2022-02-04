# Code of Advent, Day 3 - Problem 1

file1 = open("AdventOfCodeDay3.txt", "r")
lines = file1.readlines()
# Empty Gamma and Epsilon (binary) variables
Gamma = ""
Epsilon = ""

for k in range(len(lines[0].replace("\n", ""))):

    Counter1 = 0
    Counter0 = 0

    for i in range(len(lines)):
        # Remove \n at the end of the line
        var = str(lines[i]).replace("\n", "")
        number = var[k]
        number = int(number)

        # Count the number of 1's and 0's
        if number == 1:
            Counter1 = Counter1 + 1
        else:
            Counter0 = Counter0 + 1

    # According to the instructions:
    # If there are more 1's than 0's then add 1 to the binary string, otherwise add 0
    if Counter1 > Counter0:
        Gamma = Gamma + "1"
    else:
        Gamma = Gamma + "0"
    # And vice versa for Epsilon
    if Counter1 > Counter0:
        Epsilon = Epsilon + "0"
    else:
        Epsilon = Epsilon + "1"

# Convert the binary to decimal
Result1 = int(Gamma, 2)
Result2 = int(Epsilon, 2)

# Return their Products
print(Result1 * Result2)

file1.close()
