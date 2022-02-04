import copy

file1 = open("AdventOfCodeDay9.txt", "r")
lines = file1.readlines()


Map = []
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n","").split()
    Map.append([])
    for x in range(len(lines[i][0])):
        Map[i].append(int(lines[i][0][x]))

file1.close()
MapOG = copy.deepcopy(Map)

CoordinateY = []
CoordinateX = []
print(Map)

# The algorithm we will use is to see if there is an 8 surrounded by 9s. If so add low point count++, increment everything by 1, which is logical equavelent of cutting down layers.
# Here we define the passed parameter:
def CheckLargest(line, element):
    counter = 0
    LastLine = (len(Map)-1)
    LastElement = (len(Map[0])-1)

    if line == 0: # First Line
        if element == 0:
            #Here we only check 2 points
            if (Map[0][1] == 9): # One to the right
                if (Map[1][0]==9): # One directly below, if there are 2 eights, I might be fucked
                    Map[0][0] = 9
                    counter += 1

        elif element == LastElement:
            if (Map[0][LastElement-1] == 9): # One to the left
                if (Map[1][LastElement]==9): # One directly below, if there are 2 eights, I might be fucked
                    Map[0][LastElement] = 9
                    counter += 1
        else:
            if (Map[0][element-1] == 9): # One to the left
                if (Map[1][element]==9): # One directly below, if there are 2 eights, I might be fucked
                    if (Map[0][element+1]) == 9: # Right -->
                        Map[0][element] = 9
                        counter += 1

    elif line == LastLine: # Last Line
        if element == 0:
            # Here we only check 2 points
            if (Map[LastLine][1] == 9):  # One to the right
                if (Map[LastLine - 1][0] == 9):  # One directly above, if there are 2 eights, I might be fucked
                    Map[LastLine][0] = 9
                    counter += 1

        elif element == LastElement:
            if (Map[LastLine][LastElement - 1] == 9):  # One to the left
                if (Map[LastLine - 1][LastElement] == 9):  # One directly above, if there are 2 eights, I might be fucked
                    Map[LastLine][LastElement] = 9
                    counter += 1
        else:
            if (Map[LastLine][element-1] == 9): # One to the left
                if (Map[LastLine-1][element]==9): # One above below, if there are 2 eights, I might be fucked
                    if (Map[LastLine][element+1]) == 9: # Right -->
                        Map[LastLine][element] = 9
                        counter += 1

    else: # In Between
        if (element == 0): # First element
            if (Map[line-1][0] == 9): # One to the left
                if (Map[line+1][0]==9): # One directly below, if there are 2 eights, I might be fucked
                    if (Map[line][1]) == 9: # Right -->
                        Map[line][element] = 9
                        counter += 1

        elif (element == LastElement): # Last Element
            if (Map[line][LastElement-1] == 9): # One to the left
                if (Map[line+1][LastElement]==9): # One directly below, if there are 2 eights, I might be fucked
                    if (Map[line-1][LastElement]) == 9: # Right -->
                        Map[line][LastElement] = 9
                        counter += 1

        else: # In between
            if (Map[line][element - 1]) == 9:  # One to the left
                if (Map[line][element + 1]) == 9:  # One directly below, if there are 2 eights, I might be fucked
                    if (Map[line + 1][element]) == 9:  # Right -->
                        if (Map[line-1][element]) == 9: # One above
                            Map[line][element] = 9
                            counter += 1
    if counter == 1:
        CoordinateY.append(line)
        CoordinateX.append(element)
    return counter

Counter = 0
Sum = 0
Total = 9 * (len(Map)) * (len(Map[0]))
Loop = -1
# for Q in range(9):
while Sum != Total:
    Loop += 1
    Sum = 0
    for y in range(len(Map)):
        for x in range(len(Map[0])):
            if Map[y][x] == 8:
                Counter += CheckLargest(y, x)
            if Map[y][x] != 9:
                Map[y][x] = Map[y][x] + 1

    # print("Loop: ", Loop ," and Count: ", Counter)
    # print('\n'.join([''.join([str(cell) for cell in row]) for row in Map]))
    Sum = sum(map(sum, Map))
# print(Sum)
# print(Counter)
# print(CoordinateX)
# print(CoordinateY)
Value = 0
print(len(CoordinateX))
print(len(CoordinateY))
# print(MapOG)
# print('\n'.join([''.join([str(cell) for cell in row]) for row in Map]))
# print('\n'.join([''.join([str(cell) for cell in row]) for row in MapOG]))
for x in range(len(CoordinateX)):
    # print(CoordinateX[x], " ", CoordinateY[x])
    # print(x)
    Value = Value + (1 + MapOG[CoordinateY[x]][CoordinateX[x]])
print(Value)