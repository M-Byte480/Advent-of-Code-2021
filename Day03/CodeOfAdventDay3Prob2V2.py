# Code of Advent, Day 3 - Problem 1

file1 = open("AdventOfCodeDay3.txt", "r")
lines = file1.readlines()
List1 = []
Result1 = 0
Result2 = 0

# Converting the data into a List
for i in lines:
    List1.append(i.replace("\n", ""))

# Make a copy of List1, as we will be alternating the list and we will need the original for the second part of my program
List2 = List1.copy()

# We will iterate through the digits, and we check each digit in its corresponding column. IE: check the every digit in the first place, then second, etc.
for digit in range(len(lines[0]) - 1):
    # Counting the number 1's and 0's
    Counter1 = 0
    Counter0 = 0

    # Count 1's and 0's in the digit (column)
    for element in List1:
        if element[digit] == "1":
            Counter1 += 1
        else:
            Counter0 += 1

    # Check which is dominant
    if Counter1 < Counter0:
        MostCommon = "0"
    else:
        MostCommon = "1"


    variable = 0
    while variable != len(List1):
        char = List1[variable][digit]
        if len(List1) == 1: # This line makes sure if we are left with a single element to stop
            break
        if char != MostCommon:  # If the dominant character doesn't appear in the 'digit' place, discard those elements
            del List1[variable]
            variable -= 1
        variable += 1 # Now move to the next element to check


    O2 = List1[0] # If we are left with a single element, it must be the first one in the list

# Now we iterate through the copied list, and this time we will keep track of the non-dominant digits
for digit in range(len(lines[0]) - 1):
    Counter1 = 0
    Counter0 = 0

    for element in List2:
        if element[digit] == "1":
            Counter1 += 1
        else:
            Counter0 += 1

    if Counter1 < Counter0:
        LeastCommon = "1"
    else:
        LeastCommon = "0"
    # Begin discarding the elements where the non-dominant digit doesn't appear
    variable = 0
    while variable != len(List2):
        if len(List2) == 1:
            break
        if List2[variable][digit] != LeastCommon:
            del List2[variable]
            variable -= 1
        variable += 1


    if len(List2) == 1:
        break

    CO2 = List2[0] #We assign the final value to CO2

# Converting the Binary values of O2 and CO2
Result1 = int(O2, 2)
Result2 = int(CO2, 2)

# Returning their Product
print(Result1 * Result2)
file1.close()

