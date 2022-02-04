import numpy as np

file1 = open("AdventOfCodeDay11.txt", "r")
lines = file1.readlines()

Grid = []
for p in lines:
    Grid.append(p.replace("\n",""))
for p in range(len(Grid)):
    Grid[p] = list(Grid[p])
    temp = map(int, Grid[p])
    Grid[p] = list(temp)

file1.close()
Grid = np.array(Grid)
counter = 0

def Circle(Row, Column): # Element ref: imagine an old phone number 1 - 9 in a 3x3 grind

    LastRow = (len(Grid))-1
    LastColumn = (len(Grid[0]))-1
    global counter

    if Row == 0:
        if Column == 0: # 6 8 9 # Q
            if Grid[Row + 1][Column] == 9:  # 8
                Grid[Row + 1][Column]= -100
                counter += 1
                Circle(Row+1, Column)
            else:
                Grid[Row + 1][Column] += 1

            if Grid[Row + 1][Column + 1] == 9:  # 9
                Grid[Row + 1][Column+1] = -100
                counter += 1
                Circle(Row+1, Column+1)
            else:
                Grid[Row + 1][Column + 1] += 1

            if Grid[Row][Column + 1] == 9:  # 6
                Grid[Row][Column + 1] = -100
                counter += 1
                Circle(Row, Column + 1)
            else:
                Grid[Row][Column + 1] += 1

        elif Column == LastColumn: ## F
            if Grid[Row][Column - 1] == 9: # 4
                Grid[Row][Column - 1] = -100
                counter += 1
                Circle(Row, Column-1)
            else:
                Grid[Row][Column - 1] += 1

            if Grid[Row + 1][Column - 1] == 9:  # 7
                Grid[Row + 1][Column-1] = -100
                counter += 1
                Circle(Row+1, Column-1)
            else:
                Grid[Row + 1][Column - 1] += 1

            if Grid[Row + 1][Column] == 9:  # 8
                Grid[Row + 1][Column]= -100
                counter += 1
                Circle(Row+1, Column)
            else:
                Grid[Row + 1][Column] += 1
        else: ## ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
            if Grid[Row][Column + 1] == 9: # 6
                Grid[Row][Column + 1] = -100
                counter += 1
                Circle(Row, Column+1)
            else:
                Grid[Row][Column + 1] += 1

            if Grid[Row][Column - 1] == 9: # 4
                Grid[Row][Column - 1] = -100
                counter += 1
                Circle(Row, Column-1)
            else:
                Grid[Row][Column - 1] += 1

            if Grid[Row + 1][Column - 1] == 9:  # 7
                Grid[Row + 1][Column-1] = -100
                counter += 1
                Circle(Row+1, Column-1)
            else:
                Grid[Row + 1][Column - 1] += 1

            if Grid[Row + 1][Column] == 9:  # 8
                Grid[Row + 1][Column]= -100
                counter += 1
                Circle(Row+1, Column)
            else:
                Grid[Row + 1][Column] += 1

            if Grid[Row + 1][Column + 1] == 9:  # 9
                Grid[Row + 1][Column+1] = -100
                counter += 1
                Circle(Row+1, Column+1)
            else:
                Grid[Row + 1][Column + 1] += 1

    elif Row == LastRow: # Last ROw
        if Column == 0:  # 2 3 6 # NNNNNNNNNNNNNn
            if Grid[Row - 1][Column] == 9:  # 2
                Grid[Row - 1][Column] = -100
                counter += 1
                Circle(Row - 1, Column)
            else:
                Grid[Row - 1][Column] += 1

            if Grid[Row - 1][Column + 1] == 9:  # 3
                Grid[Row - 1][Column + 1] = -100
                counter += 1
                Circle(Row - 1, Column + 1)
            else:
                Grid[Row - 1][Column + 1] += 1

            if Grid[Row][Column + 1] == 9:  # 6
                Grid[Row][Column + 1] = -100
                counter += 1
                Circle(Row, Column + 1)
            else:
                Grid[Row][Column + 1] += 1

        elif Column == LastColumn: # 214 # PPPPPPPPPPPPPPPPP
            if Grid[Row][Column - 1] == 9:  # 4
                Grid[Row][Column - 1] = -100
                counter += 1
                Circle(Row, Column - 1)
            else:
                Grid[Row][Column - 1] += 1

            if Grid[Row - 1][Column - 1] == 9:  # 1
                Grid[Row - 1][Column - 1] = -100
                counter += 1
                Circle(Row - 1, Column - 1)
            else:
                Grid[Row - 1][Column - 1] += 1

            if Grid[Row - 1][Column] == 9:  # 2
                Grid[Row - 1][Column] = -100
                counter += 1
                Circle(Row - 1, Column)
            else:
                Grid[Row - 1][Column] += 1
        else: # 1 2 3 4 6 # LLLLLLLLLLLLLLLLLLLL
            if Grid[Row][Column + 1] == 9:  # 6
                Grid[Row][Column + 1] = -100
                counter += 1
                Circle(Row, Column + 1)
            else:
                Grid[Row][Column + 1] += 1

            if Grid[Row][Column - 1] == 9:  # 4
                Grid[Row][Column - 1] = -100
                counter += 1
                Circle(Row, Column - 1)
            else:
                Grid[Row][Column - 1] += 1

            if Grid[Row - 1][Column - 1] == 9:  # 1
                Grid[Row - 1][Column - 1] = -100
                counter += 1
                Circle(Row - 1, Column - 1)
            else:
                Grid[Row - 1][Column - 1] += 1

            if Grid[Row - 1][Column] == 9:  # 2
                Grid[Row - 1][Column] = -100
                counter += 1
                Circle(Row - 1, Column)
            else:
                Grid[Row - 1][Column] += 1

            if Grid[Row - 1][Column + 1] == 9:  # 3
                Grid[Row - 1][Column + 1] = -100
                counter += 1
                Circle(Row - 1, Column + 1)
            else:
                Grid[Row - 1][Column + 1] += 1
    else: # MIDLE
        if Column == 0: #2 3 6 8 9 # MMMMMMMMMMMMM
            if Grid[Row][Column + 1] == 9:  # 6
                Grid[Row][Column + 1] = -100
                counter += 1
                Circle(Row, Column + 1)
            else:
                Grid[Row][Column + 1] += 1

            if Grid[Row + 1][Column] == 9:  # 8
                Grid[Row + 1][Column] = -100
                counter += 1
                Circle(Row + 1, Column)
            else:
                Grid[Row + 1][Column] += 1

            if Grid[Row + 1][Column + 1] == 9:  # 9
                Grid[Row + 1][Column + 1] = -100
                counter += 1
                Circle(Row + 1, Column + 1)
            else:
                Grid[Row + 1][Column + 1] += 1

            if Grid[Row-1][Column] == 9: # 2
                Grid[Row - 1][Column] = -100
                counter += 1
                Circle(Row - 1, Column)
            else:
                Grid[Row - 1][Column] += 1

            if Grid[Row-1][Column+1] == 9: # 3
                Grid[Row - 1][Column + 1] = -100
                counter += 1
                Circle(Row - 1, Column + 1)
            else:
                Grid[Row - 1][Column + 1] += 1
        elif Column == LastColumn:# 2 1 4 7 8 # OOOOOOOOOOOOOOOO

            if Grid[Row][Column - 1] == 9:  # 4
                Grid[Row][Column - 1] = -100
                counter += 1
                Circle(Row, Column - 1)
            else:
                Grid[Row][Column - 1] += 1

            if Grid[Row + 1][Column - 1] == 9:  # 7
                Grid[Row + 1][Column - 1] = -100
                counter += 1
                Circle(Row + 1, Column - 1)
            else:
                Grid[Row + 1][Column - 1] += 1

            if Grid[Row + 1][Column] == 9:  # 8
                Grid[Row + 1][Column] = -100
                counter += 1
                Circle(Row + 1, Column)
            else:
                Grid[Row + 1][Column] += 1


            if Grid[Row-1][Column-1] == 9: # 1
                Grid[Row - 1][Column - 1] = -100
                counter += 1
                Circle(Row - 1, Column - 1)
            else:
                Grid[Row - 1][Column - 1] += 1

            if Grid[Row-1][Column] == 9: # 2
                Grid[Row - 1][Column] = -100
                counter += 1
                Circle(Row - 1, Column)
            else:
                Grid[Row - 1][Column] += 1

        else: # AAAAAAAAAAAAAAAAAAAAAAAAa
            if Grid[Row][Column + 1] == 9:  # 6
                Grid[Row][Column + 1] = -100
                counter += 1
                Circle(Row, Column + 1)
            else:
                Grid[Row][Column + 1] += 1

            if Grid[Row][Column - 1] == 9:  # 4
                Grid[Row][Column - 1] = -100
                counter += 1
                Circle(Row, Column - 1)
            else:
                Grid[Row][Column - 1] += 1

            if Grid[Row + 1][Column - 1] == 9:  # 7
                Grid[Row + 1][Column - 1] = -100
                counter += 1
                Circle(Row + 1, Column - 1)
            else:
                Grid[Row + 1][Column - 1] += 1

            if Grid[Row + 1][Column] == 9:  # 8
                Grid[Row + 1][Column] = -100
                counter += 1
                Circle(Row + 1, Column)
            else:
                Grid[Row + 1][Column] += 1

            if Grid[Row + 1][Column + 1] == 9:  # 9
                Grid[Row + 1][Column + 1] = -100
                counter += 1
                Circle(Row + 1, Column + 1)
            else:
                Grid[Row + 1][Column + 1] += 1

            if Grid[Row-1][Column] == 9: # 2
                Grid[Row - 1][Column] = -100
                counter += 1
                Circle(Row - 1, Column)
            else:
                Grid[Row - 1][Column] += 1

            if Grid[Row-1][Column+1] == 9: # 3
                Grid[Row - 1][Column + 1] = -100
                counter += 1
                Circle(Row - 1, Column + 1)
            else:
                Grid[Row - 1][Column + 1] += 1

            if Grid[Row-1][Column-1] == 9:
                Grid[Row-1][Column-1] = -100
                counter += 1
                Circle(Row-1,Column-1)
            else:
                Grid[Row-1][Column-1] += 1

    return counter
# print(Grid)
print('\n'.join([''.join([str(cell) for cell in row]) for row in Grid]))
Step = 1
while Step > 0:
    for Row in range(len(Grid)):
        for Column in range(len(Grid[0])):

            if Grid[Row][Column] == 9:
                Grid[Row][Column] = -100
                Circle(Row, Column)
            else:
                Grid[Row][Column] += 1
    tally = 0
    for Row in range(len(Grid)):
        for Column in range(len(Grid[0])):
            Grid[Row][Column] = Grid[Row][Column]
            if Grid[Row][Column] <= 0:
                Grid[Row][Column] = 0
                tally += 1

    if tally == (10 * 10):
        print("It happened on step: ", Step)
        break
    Step += 1
    # print("\n")
    # print('\n'.join([''.join([str(cell) for cell in row]) for row in Grid]))
print(tally,"\n")
