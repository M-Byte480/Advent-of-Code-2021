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
for x in range(10):
    MyArray2D.append([])
    for y in range(10):
        MyArray2D[x].append(0)

def line(ArrayName, LineNumber):
    return None

for line in range(len(Array)):

    FirstPoint = Array[line][0]
    x1, y1 = FirstPoint[0], FirstPoint[1]
    SecondPoint = Array[line][1]
    x2, y2 = SecondPoint[0], SecondPoint[1]
    print(x1, ",", x2 ,"-", y1,",",y2)

    if x1 == x2:
        if y1 > y2:
            Right = y1
            Left = y2
        else:
            Left = y1
            Right = y2

        for y_axis in range(Left, Right):
            MyArray2D[int(x1)][y_axis] += 1

"""    elif y2 == y1:
        if x1 > x2:
            High = x1
            Low = x2
        else:
            Low = x2
            High = x1

        for horizontal in range(Low, High):
            MyArray2D[horizontal][int(y1)] += 1"""



for x in range(10):
    for y in range(10):
        if MyArray2D[x][y] > 1:
            counter += 1

print(counter)
print('\n'.join([''.join([str(cell) for cell in row]) for row in MyArray2D]))

file1.close()
