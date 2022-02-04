# Sum of first 3 elements (sum of element one, two and three) and compare it with the next pair of 3 elements (sum of element two, three and four)

file1 = open("AdventOfCodeDay1.txt", "r")
Lines = file1.readlines()

counter = 0

with open("AdventOfCodeDay1.txt", "r") as file:
    element1 = file.readline()

element3 = 0
element6 = 0

for i in range(len(Lines)-3):
    # The three elements with incrementation accordingly to the for loop
    element1 = int(Lines[i])
    element2 = int(Lines[i+1])
    element3 = int(Lines[i+2])

    # Their Sum
    x = element1 + element2 + element3

    # Add the next three elements
    element4 = int(Lines[i+1])
    element5 = int(Lines[i+2])
    element6 = int(Lines[i+3])

    y = element4 + element5 + element6

    # Compare the sums
    if y > x:
        counter = counter + 1
        
    
print(counter)
file1.close()
