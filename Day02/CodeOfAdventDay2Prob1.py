# Advent Of Code Day 2 Problem 1
# We have given instruction and find the product of the final X coordinate and the Y coordinate
file1 = open("AdventOfCodeDay2.txt", "r")
lines = file1.readlines()


# We start at (0, 0)
x = 0
y = 0

for i in range(len(lines)):
    # Split the current line into two elements, the instruction and its value
    list1 = (str(lines[i]).split())

    # Take the value based on the instruction
    if list1[0] == "forward":
        x = x + int(list1[1])
    elif list1[0] == "down":
        y = y + int(list1[1])
    elif list1[0] == "up":
        y = y - int(list1[1])

# Returns their product for the puzzle solution
print(x * y)
file1.close()
