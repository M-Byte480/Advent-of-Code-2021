file1 = open("AdventOfCodeDay13.txt", "r")
lines = file1.readlines()

Graph = []
Fold = []
for p in lines:
    Graph.append(p.replace("\n",""))
for p in range(len(Graph)):
    if Graph[p] == "":
        for q in range(len(Graph)-(p+1)):
            Fold.append(Graph.pop(p+1))
        Graph.pop(p)
        break

file1.close()

def Folding(str, axes):
    if str == "y": # We are folding along a row
        distance = len(Grid) - axes - 1
        for fold in range(distance):
            shift = axes+fold+1 - distance
            for move in range(len(Grid[axes])):
                if Grid[axes-shift][move] != "#":
                    Grid[axes-shift][move] = Grid[axes+fold+1][move]
        for fold in range(distance+1):
            del Grid[axes]


    else: # We are folding along a column
        distance = len(Grid[0]) - axes - 1
        for fold in range(distance):
            shift = axes+fold+1 - distance
            for move in range(len(Grid)):
                if Grid[move][axes - shift] != "#":
                    Grid[move][axes - shift] = Grid[move][axes + fold + 1]
        for fold in range(distance+1):
            for column in range(len(Grid)):
                del Grid[column][axes]

for p in range(len(Fold)):
    Fold[p] = Fold[p].replace("fold along ","").replace("="," ").split(" ")
    Fold[p][1] = int(Fold[p][1])

for p in range(len(Graph)):
    Graph[p] = Graph[p].split(",")
    Graph[p][0] = int(Graph[p][0])
    Graph[p][1] = int(Graph[p][1])

# print(Graph)
print(Fold)

LargestX = Graph[1][0]
LargestY = Graph[1][1]
for largestX in range(len(Graph)):
    value = Graph[largestX][0]
    if value > LargestX:
        LargestX = value

for largestY in range(len(Graph)):
    value = Graph[largestY][1]
    if value > LargestY:
        LargestY = value

# print(LargestX)
# print(LargestY)
Grid = []
for Y in range(LargestY+1):
    Grid.append([])
    for X in range(LargestX+1):
        Grid[Y].append(".")


for Hash in Graph:
    Grid[Hash[1]][Hash[0]] = "#"


for loop in Fold:
    Folding(loop[0],loop[1])
print('\n'.join([''.join([str(cell) for cell in row]) for row in Grid]))
