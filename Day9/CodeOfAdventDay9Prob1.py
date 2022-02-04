# Code of Advent, Day 9 - Problem 1

file1 = open("AdventOfCodeDay9.txt", "r")
lines = file1.readlines()

def Check_OfTopLine(list, char, temp):
    new = int(list[0][char])
    if char == 0:
        if list[1][char] < temp:
            new = 9
        if list[0][char + 1] < temp:
            new = 9
    elif char == len(list)-1:
        if list[1][char] < temp:
            new = 9
        if list[0][char - 1] < temp:
            new = 9
    else:
        if list[1][char] < temp:
            new = 9
        if list[0][char + 1] < temp:
            new = 9
        if list[0][char - 1] < temp:
            new = 9
    return str(new)

def Check_BottomLine(list, char, temp):
    new = int(list[len(list)-1][char])
    if char == 0:
        if list[len(list)-2][char] < temp:
            new = 9
        if list[len(list)-1][char + 1] < temp:
            new = 9
    elif char == len(list)-1:
        if list[len(list)-2][char] < temp:
            new = 9
        if list[len(list)-1][char - 1] < temp:
            new = 9
    else:
        if list[len(list)-2][char] < temp:
            new = 9
        if list[len(list)-1][char + 1] < temp:
            new = 9
        if list[len(list)-1][char - 1] < temp:
            new = 9
    return str(new)

def Check_LeftColumn(list, row, temp):
    new = int(list[row][0])
    if row == 0:
        if list[row][1] < temp:
            new = 9
        if list[row + 1][0] < temp:
            new = 9
    elif row == len(list)-1:
        if list[row][1] < temp:
            new = 9
        if list[row - 1][0] < temp:
            new = 9
    else:
        if int(list[row][1]) < temp:
            new = 9
        if int(list[row+1][0]) < temp:
            new = 9
        if int(list[row-1][0]) < temp:
            new = 9
    return str(new)

def Check_RightColumn(list, row, temp):
    new = int(list[row][len(row)-1])
    if row == 0:
        if list[row][len(row)-2] < temp:
            new = 9
        if list[row + 1][len(row)-1] < temp:
            new = 9
    elif row == len(row)-1:
        if list[row][len(row)-2] < temp:
            new = 9
        if list[row - 1][len(row)-1] < temp:
            new = 9
    else:
        if list[row][len(row)-2] < temp:
            new = 9
        if list[row+1][len(row)-1] < temp:
            new = 9
        if list[row-1][len(row)-1] < temp:
            new = 9
    return str(new)

temp = []
Map = []
for z in lines:
    temp.append(z.replace("\n",""))
    # Map.append(z.replace("\n","").replace("9"," "))
for i in range(len(temp)):
    for z in range(temp[0]):
        Map[i].append(int(temp[i][z]))
print(Map)
counter = 0
file1.close()

print('\n'.join([''.join([str(cell) for cell in row]) for row in Map]))

for x in range(9, 0, -1):
    for line in range(len(Map)):
        print("Line: ", line)
        for char in range(line):
            print("char: ", char)
            print("Actual thing: ", Map[line][char])
            character = int(Map[line][char])
            temp = 9


            if character != x:
                #We need to check the surrounding variables to see if it is the lowest
                if line == 0:
                    Map[line][char] = Check_OfTopLine(Map, char, temp)
                elif line == len(Map)-1:
                    Map[line][char] = Check_BottomLine(Map, char, temp)
                elif char == 0:
                    Map[line][char] = Check_LeftColumn(Map, line, temp)
                elif char == len(line) - 1:
                    Map[line][char] = Check_RightColumn(Map, line, temp)
                print("New char: ", Map[line][char])
                # if Map[line+1][char] < temp:
                #     char = 9
                # if Map[line-1][char] < temp:
                #     char = 9
                # if Map[line][char+1] < temp:
                #     char = 9
                # if Map[line][char-1] < temp:
                #     char = 9

                if Map[line+1][char] > temp and Map[line-1][char] > temp and Map[line][char+1] > temp and Map[line][char-1] > temp:
                    counter += 1
                print("Counter: ", counter)
                # if line == 0:
                #     if char == 0:
                #     elif char == len(line - 1):
                #
                # elif line == len(Map)-1:
                #     if char == 0:
                #     elif char == len(line - 1):
                #
                # if char == 0:
                # elif char == len(line-1):


# print(Map)
# We have a 100x100 map
print('\n'.join([''.join([str(cell) for cell in row]) for row in Map]))
# print(len(Map[0]))