# Advent Of Code Day 2 Problem 1
# Find the product of the Final Horizontal and the Vertical position
file1 = open("AdventOfCodeDay2.txt", "r")
lines = file1.readlines()

horizontal = 0
depth = 0
aim = 0

# Iterate through the instructions
for i in range(len(lines)):
    # Split the current line into instruction and value
    list1 = (str(lines[i]).split())
    value = int(list1[1]) # Store the value in a variable

    # Follow instructions accordingly to the puzzle requirement:
    if list1[0] == "forward":
        horizontal = horizontal + value
        depth = depth + aim * value
        
    elif list1[0] == "down":
        aim = aim + value
        
    elif list1[0] == "up":
        aim = aim - value

# Return product of final horizontal and depth
print(horizontal * depth)
file1.close()
