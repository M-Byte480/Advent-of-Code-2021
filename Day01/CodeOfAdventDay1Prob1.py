# Count how many incrementation are there based on the adjacent elements

file1 = open("AdventOfCodeDay1.txt", "r")
Lines = file1.readlines()

counter = 0

with open("AdventOfCodeDay1.txt", "r") as file:
    # Assign first element (or the first line)
    element1 = file.readline()

# Algorithm for counting the number of increments
for i in Lines:
    element2 = i
    if element2 > element1:
        counter = counter + 1
    element1 = element2
    
print(counter + 1)
