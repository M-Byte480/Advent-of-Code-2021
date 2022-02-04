# Code of Advent, Day 8 - Problem 1

file1 = open("AdventOfCodeDay8.txt", "r")
lines = file1.readlines()
# Data[Line][Side][Display]
Data = lines.copy()
for i in range(len(lines)):
    Data[i] = Data[i].replace("\n", "")
    Data[i] = Data[i].split(" | ")
    Data[i][1] = Data[i][1].split(" ")
    Data[i][0] = Data[i][0].split(" ")

count = 0
for Element in range(len(Data)):
    for Display in range(4):
        Compare = len(Data[Element][1][Display])
        if Compare == 2 or Compare == 3 or Compare == 4 or Compare == 7:
            count += 1

print(count)
file1.close()
