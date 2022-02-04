file1 = open("AdventOfCodeDay14.txt", "r")
lines = file1.readlines()
file1.close()

for temp in range(len(lines)):
    lines[temp] = lines[temp].replace("\n","")
input = lines.pop(0)
lines.pop(0)
for temp in range(len(lines)):
    lines[temp] = lines[temp].split(" -> ")
# print(input)
# print(lines)
# print(input)
# for step in range(10):
#     for iteration in range(len(input), 1, -1):
#         comp = input[iteration-2] + input[iteration-1]
#         a = input.index(comp) + 1
#         for z in lines:
#             if comp == z[0]:
#                 input = input[:a] + z[1] + input[a:]
#     print(input)
input = list(input)
for step in range(10):
    for iteration in range(len(input), 1, -1):
        comp = input[iteration-2] + input[iteration-1]
        # a = input.index(comp) + 1
        for z in lines:
            if comp == z[0]:
                input.insert(iteration-1, z[1])
                break
    # print("".join(input))
"".join(input)

# for step in range(4):
#     for iteration in range(0, len(input)-1,1):
#         comp = input[iteration] + input[iteration+1]
#         a = input.index(comp)
#         for z in lines:
#             if comp == z[0]:
#                 input = input[:a+1] + z[1] + input[a:]
#                 break
# print(list(input))
# output = list(input)
# # print(output)
# for step in range(1):
#     for iteration in range(0, len(input)-1, 2):
#         comp = [output[iteration] + output[iteration+1]]
#         del output[iteration+1]
#         del output[iteration]
#         comp = "".join(comp)
#         for z in lines:
#             if comp == z[0]:
#                 comp = list(comp)
#                 comp.insert(1,z[1])
#                 break
#         output = comp + output
#         print(output)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
largest = 0
smallest = 2**52
for i in alphabet:
    counter = input.count(i)
    if counter > largest :
        largestLetter = i
        largest = counter
    if counter != 0 and counter < smallest:
        smallest = counter
        smallestLetter = i
    # print(i,": ",counter)
print(largestLetter, " ", largest, " ", smallestLetter, " ", smallest)
print(largest - smallest)