# Code of Advent, Day 8 - Problem 1

file1 = open("AdventOfCodeDay8.txt", "r")
lines = file1.readlines()
# Data[Line][Side][Display]
Data = lines.copy()
for i in range(len(lines)):
    Data[i] = Data[i].replace("\n", "")
    Data[i] = Data[i].split(" | ")
    Data[i][1] = Data[i][1].split(" ")
    Data[i][0] = Data[i][0].split(" ")
Num0, Num1, Num2, Num3, Num4, Num5, Num6, Num7, Num8, Num9 = "", "", "", "", "", "", "", "", "", ""

def splitword(word):
    return [char for char in word]

Storage = []
count = 0
Final = []
for owo in range(len(Data)):
    print("We are testing line:", owo)
    temp = []

    Num069 = []
    Num523 = []
    From = Data[owo][0]
    print("We are testing: ", From)
    for q in range(len(From)):
        print("And ", q)
        if len(From[q]) == 2:
            Num1 = From[q]
        elif len(From[q]) == 3:
            Num7 = From[q]
        elif len(From[q]) == 7:
            Num8 = From[q]
        elif len(From[q]) == 4:
            Num4 = From[q]
        elif len(From[q]) == 6:
            Num069.append(From[q])
        elif len(From[q]) == 5:
            Num523.append(From[q])
        # I have taken the following logic from: https://www.reddit.com/r/adventofcode/comments/rbvpui/2021_day_8_part_2_my_logic_on_paper_i_used_python/
    tester = Num4.replace(Num1[0],"").replace(Num1[1],"")

    print("Here is my 4 digit number: ", Num4)
    print("Here is my 2 digit number: ", Num1)
    print("This is the weird part of 4: ", tester)
    for Num in Num523:
        print("We are testing: ", Num)
        if Num1[0] in Num and Num1[1] in Num:
            Num3 = Num
        elif tester[0] in Num and tester[1] in Num:
            Num5 = Num
        else:
            Num2 = Num

    for Num in Num069:
        print("We are now testing 069: ", Num)
        if (Num4[0] in Num) and (Num4[1] in Num) and (Num4[2] in Num) and (Num4[3] in Num):
            Num9 = Num
        elif (tester[0] in Num) and (tester[1] in Num):
            Num6 = Num
        else:
            Num0 = Num

    wholeList = []
    wholeList.append(Num0)
    wholeList.append(Num1)
    wholeList.append(Num2)
    wholeList.append(Num3)
    wholeList.append(Num4)
    wholeList.append(Num5)
    wholeList.append(Num6)
    wholeList.append(Num7)
    wholeList.append(Num8)
    wholeList.append(Num9)
    print("We now have a list of the numbers from 0 to 9. I dont use dict Sam because I am cool: ", wholeList)
    final_answer = ""
    for element in Data[owo][1]:
        print(element)
        if len(element) == 2:
            final_answer += '1'
        elif len(element) == 3:
            final_answer += '7'
        elif len(element) == 4:
            final_answer += '4'
        elif len(element) == 7:
            final_answer += '8'
        elif len(element) == 5:
            if element[0] in Num3 and element[1] in Num3 and element[2] in Num3 and element[3] in Num3 and element[4] in Num3:
                final_answer += '3'
            elif element[0] in Num5 and element[1] in Num5 and element[2] in Num5 and element[3] in Num5 and element[4] in Num5:
                final_answer += '5'
            else:
                final_answer += '2'
        elif len(element) == 6:
            if element[0] in Num6 and element[1] in Num6 and element[2] in Num6 and element[3] in Num6 and element[4] in Num6 and element[5] in Num6:
                final_answer += '6'
            elif element[0] in Num9 and element[1] in Num9 and element[2] in Num9 and element[3] in Num9 and element[4] in Num9 and element[5] in Num9:
                final_answer += '9'
            else:
                final_answer += '0'
        # Final.append(final_answer)
    Final.append(final_answer)
print(Final)
total = 0
for i in Final:
    total += int(i)
print(total)
file1.close()
