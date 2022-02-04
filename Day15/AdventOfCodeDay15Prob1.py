file1 = open("AdventOfCodeDay15.txt", "r")
lines = file1.readlines()
file1.close()

# Beginning of initialization
graph = []

for z in range(len(lines)):
    lines[z] = (lines[z].replace("\n",""))

for z in range(len(lines)):
    graph.append([])
    for p in range(len(lines[z])):
        graph[z].append(int(lines[z][p]))
# End of Initialization
print('\n'.join([''.join([str(cell) for cell in row]) for row in graph]))
# Beginning of defining the algorithm
def dijsktar(heatmap):
    #starting = heatmap[0][0]
    pass