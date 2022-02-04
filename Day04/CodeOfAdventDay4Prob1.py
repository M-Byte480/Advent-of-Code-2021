file1 = open("AdventOfCodeDay4.txt", "r")
lines = file1.readlines()

numbersPulled = "87,12,53,23,31,70,37,79,95,16,72,9,98,92,5,74,17,60,96,80,75,11,73,33,3,84,81,2,97,93,59,13,77,52,69,83,51,64,48,82,7,49,20,8,36,66,19,0,99,41,91,78,42,40,62,63,57,39,55,47,29,50,58,34,27,43,30,35,22,28,4,14,26,32,10,88,46,65,90,76,38,6,71,67,44,68,86,25,21,24,56,94,18,89,61,15,1,45,54,85".split(",")

rows, columns = (5,5)
boards = []
placeHolder = -1
Winner = 0

def _SumOfRows(board, row):
    n = 0
    for Q in board[row]:
        n = n + int(Q)
    return n

def _SumOfColumns(board, column):
    n = 0
    for K in range(len(board[0])):
        n += int(board[K][column])
    return n

for board in range(int(len(lines)/6)):
    temp = []
    for row in range(5):
        temp.append(lines[board * 6 + row].split())
    boards.insert(board, temp)
winningNumber = 0
# boards [Board] [Row] [Column]
# Note to Milan tomorrow, use the placeholder to replace the numbers pulled, then check after each number, if a board's sum of the row == -5 or the sum of the board's column == -5
# Then you can check the sum of the whole thing +5 or something
# xoxo
# Sleepy Milan
for i in numbersPulled:
#    print("Number Pulled is: " , i)
    for BoardNum in range(len(boards)):
#        print("Board Number is: " , BoardNum)
        for R in range(len(boards[BoardNum])):
#            print("Row Number is: " , R)
            for element in range(len(boards[BoardNum][R])):
                    if boards[BoardNum][R][element] == i:
                        boards[BoardNum][R][element] = (-1)

    for check in range(len(boards)):
        for R in range(len(boards[check])):
            if _SumOfRows(boards[check], R) == -5:
                print("Winning Board is, Board No. ", check)
                Winner = boards[check]
                break
        if Winner in boards:
            break

    for check in range(len(boards)):
        if Winner in boards:
            break
        for C in range(5):
            if _SumOfColumns(boards[check], C) == -5:
                Winner = boards[check]
                print("Winning Board is, Board No. ", check)
                break

    if Winner in boards:
        winningNumber = int(i)
        break

print(Winner)

total = 0
for x in range(len(Winner)):
    for z in range(len(Winner[x])):
        if Winner[x][z] == -1:
            Winner[x][z] = 0

        total = int(Winner[x][z]) + total


print(Winner)
print(winningNumber)
print(total)
print(total * winningNumber)
file1.close()