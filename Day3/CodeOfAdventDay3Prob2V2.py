# Code of Advent, Day 3 - Problem 1

file1 = open("AdventOfCodeDay3.txt", "r")
lines = file1.readlines()
List1 = []
Result1 = 0
Result2 = 0

# Converting the data into a List
for i in lines:
    List1.append(i.replace("\n", ""))


List2 = List1.copy()

for digit in range(len(lines[0]) - 1):
    Counter1 = 0
    Counter0 = 0

    for element in List1:
        if element[digit] == "1":
            Counter1 += 1
        else:
            Counter0 += 1

    if Counter1 < Counter0:
        MostCommon = "0"
    else:
        MostCommon = "1"

    variable = 0
    while variable != len(List1):
        char = List1[variable][digit]
        if len(List1) == 1:
            break
        if char != MostCommon:
            del List1[variable]
            variable -= 1
        variable += 1

    if len(List1) == 1:
        break

    O2 = List1[0]

    # for j in range(len(O2)):
    #     Result1 = Result1 + 2 ** int(11 - j) * int(O2[int(j)])

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

    CO2 = List2[0]

Result1 = int(O2, 2)
Result2 = int(CO2, 2)


print(Result1 * Result2)
file1.close()
