file1 = open("AdventOfCodeDay4.txt", "r")
lines = file1.readlines()

numbersPulled = "87,12,53,23,31,70,37,79,95,16,72,9,98,92,5,74,17,60,96,80,75,11,73,33,3,84,81,2,97,93,59,13,77,52," \
                "69,83,51,64,48,82,7,49,20,8,36,66,19,0,99,41,91,78,42,40,62,63,57,39,55,47,29,50,58,34,27,43,30,35," \
                "22,28,4,14,26,32,10,88,46,65,90,76,38,6,71,67,44,68,86,25,21,24,56,94,18,89,61,15,1,45,54," \
                "85".split(",")
numberNotUsed = numbersPulled.copy()

boards = []
placeHolder = -1
Winner = 0


def sum_of_rows(boardNo, rowNo):
    n = 0
    for Q in boardNo[rowNo]:
        n = n + int(Q)
    return n


def sum_of_columns(boardNo, columnNo):
    n = 0
    for K in range(len(boardNo[0])):
        n += int(boardNo[K][columnNo])
    return n


for board in range(int(len(lines)/6)):
    temp = []
    for row in range(5):
        temp.append(lines[board * 6 + row].split())
    boards.insert(board, temp)
winningNumber = 0

for i in numbersPulled:

    Pop = False
    if len(boards) == 1:
        Winner = boards[0]
        break
    numberNotUsed.remove(i)
    for BoardNum in range(len(boards)):
        for R in range(len(boards[BoardNum])):
            for element in range(len(boards[BoardNum][R])):
                if boards[BoardNum][R][element] == i:
                    boards[BoardNum][R][element] = -1

    check = 0
    var = len(boards)
    while check != var:
        for R in range(len(boards[check])):
            if sum_of_rows(boards[check], R) == -5:
                Pop = True
                boards.pop(check)
                check -= 1
                break
        var = len(boards)
        check += 1

    check = 0
    var = len(boards)

    while check != var:
        for C in range(5):
            if sum_of_columns(boards[check], C) == -5:
                Pop = True
                boards.pop(check)
                check -= 1
                break
        var = len(boards)
        check += 1

print(numberNotUsed)
print(Winner)

Test = False

for i in numberNotUsed:


    for Row in range(5):
        for Col in range(5):
            if Winner[Row][Col] == i:
                Winner[Row][Col] = (-1)

    for check in range(5):
        for R in range(5):
            if sum_of_rows(Winner, R) == -5:
                Test = True
                break


    for check in range(5):
        for C in range(5):
            if sum_of_columns(Winner, C) == -5:
                Test = True
                break
    if Test == True:
        winningNumber = i
        break
total = 0

for x in range(len(Winner)):
    for z in range(len(Winner[x])):
        if Winner[x][z] == -1:
            Winner[x][z] = 0

        total = int(Winner[x][z]) + total


print(total * int(winningNumber))

file1.close()