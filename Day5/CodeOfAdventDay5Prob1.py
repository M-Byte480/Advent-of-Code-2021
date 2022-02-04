file1 = open("AdventOfCodeDay5.txt", "r")
Lines = file1.readlines()
from pandas import *
Array = []
counter = 0
for i in range(len(Lines)):
    Array.append(Lines[i].replace("\n", "").split(" -> "))
    for x in range(2):
        Array[i][x] = Array[i][x].split(",")

MyArray2D = []
for x in range(1000):
    MyArray2D.append([])
    for y in range(1000):
        MyArray2D[x].append(0)

for line in range(len(Array)):

    FirstPoint = Array[line][0]
    SecondPoint = Array[line][1]
    x1 = int(Array[line][0][0])
    y1 = int(Array[line][0][1])
    x2 = int(Array[line][1][0])
    y2 = int(Array[line][1][1])

    if (x1 == x2) or (y1 == y2):
        if x1 == x2:

            if y1 > y2:
                High = y1
                Low = y2
            else:
                Low = y1
                High = y2

            for vertical in range(int(Low), int(High)+1):
                MyArray2D[vertical][x1] += 1

        elif y1 == y2:
            if x1 > x2:
                High = x1
                Low = x2
            else:
                Low = x1
                High = x2

            for horizontal in range(int(Low), int(High)+1):
                MyArray2D[y1][horizontal] += 1



for x in range(len(MyArray2D)):
    for y in range(len(MyArray2D[0])):
        if MyArray2D[x][y] > 1:
            counter += 1

print(counter)
print('\n'.join([''.join([str(cell) for cell in row]) for row in MyArray2D]))

file1.close()
