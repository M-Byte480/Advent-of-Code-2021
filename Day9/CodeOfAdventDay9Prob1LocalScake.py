# Code of Advent, Day 9 - Problem 1

file1 = open("AdventOfCodeDay9.txt", "r")
lines = file1.readlines()

def Check_OfTopLine(list, char, temp):
    comparison = int(list[0][char])
    if list[
    if char == 0:
        if list[1][char] >= comparison:
            if list[0][char + 1] >= comparison:
                comparison += 1
    elif char == len(list)-1:
        if list[1][char] >= comparison:
            if list[0][char - 1] >= comparison:
                comparison += 1
    else:
        if list[1][char] >= comparison:
            if list[0][char + 1] >= comparison:
                if list[0][char - 1] >= comparison:
                    comparison += 1
    return str(comparison)

def Check_BottomLine(list, char, temp):
    new = int(list[len(list)-1][char])
    if char == 0:
        if list[len(list)-2][char] < temp:
             if list[len(list)-1][char + 1] < temp:
                new = temp
    elif char == len(list)-1:
        if list[len(list)-2][char] < temp:
             if list[len(list)-1][char - 1] < temp:
                new = temp
    else:
        if list[len(list)-2][char] < temp:
            if list[len(list)-1][char + 1] < temp:
                if list[len(list)-1][char - 1] < temp:
                    new = temp
    return str(new)

def Check_LeftColumn(list, row, temp):
    new = int(list[row][0])
    if row == 0:
        if list[row][1] < temp:
            if list[row + 1][0] < temp:
                new = temp
    elif row == len(list)-1:
        if list[row][1] < temp:
            if list[row - 1][0] < temp:
                new = temp
    else:
        if int(list[row][1]) < temp:
            if int(list[row+1][0]) < temp:
                if int(list[row-1][0]) < temp:
                  new = temp
    return str(new)

def Check_RightColumn(list, row, temp):
    new = int(list[row][len(row)-1])
    if row == 0:
        if list[row][len(row)-2] < temp:
            if list[row + 1][len(row)-1] < temp:
                new = temp
    elif row == len(row)-1:
        if list[row][len(row)-2] < temp:
            if list[row - 1][len(row)-1] < temp:
                new = temp
    else:
        if list[row][len(row)-2] < temp:
            if list[row+1][len(row)-1] < temp:
                if list[row-1][len(row)-1] < temp:
                    new = temp
    return str(new)

temp = []
Map = []

for z in lines:
    temp.append(z.replace("\n",""))
    # Map.append(z.replace("\n","").replace("9"," "))

for i in range(len(temp)-1):
    Map.append([])
    for z in range(len(temp[0])-1):
        # print(temp[i][z])
        Map[i].append(int(temp[i][z]))
# print(Map)

counter = 0
file1.close()
print(Map)
print('\n'.join([''.join([str(cell) for cell in row]) for row in Map]))
x = 9
# while x != -1:
#     change = False
for line in range(len(Map)):
    for char in range(line):
        character = int(Map[line][char])

        # print('\n'.join([''.join([str(cell) for cell in row]) for row in Map]))
        # print('\n')
        if character != x:
            if line == 0:
                Value = int(Check_OfTopLine(Map, char, x))
                change = True

            elif line == len(Map)-1:
                Value = int(Check_BottomLine(Map, char, x))
                change = True

            elif char == 0:
                Value = int(Check_LeftColumn(Map, line, x))
                change = True

            elif char == len(Map[line]) - 1:
                Value = int(Check_RightColumn(Map, line, x))
                change = True

            # print("New char: ", Value)
            Map[line][char] = int(Value)
            # if change == False:
            #     x -= 1

                # if Map[line+1][char] > x and Map[line-1][char] > x and Map[line][char+1] > x and Map[line][char-1] > x:
                #     counter += 1
                # print("Counter: ", counter)


print(Map)
# We have a 100x100 map
print('\n'.join([''.join([str(cell) for cell in row]) for row in Map]))
# print(len(Map[0]))