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

for Element in range(len(Data)):
    temp = []
    for Display in range(4):
        Compare = len(Data[Element][1][Display])
        if Compare == 2:
            temp.append('1')
        elif Compare == 3:
            temp.append('7')
        elif Compare == 4:
            temp.append('4')
        elif Compare == 7:
            temp.append('8')
        else:
            temp.append(Data[Element][1][Display])
    Storage.append(" ".join(temp))

Final = []
final_answer = []
for i in range(len(Storage)):
    if "1" in Storage[i] and "7" in Storage[i] and "4" in Storage[i] and "8" in Storage[i]:
        continue
    Num069 = []
    Num523 = []
    for x in range(4):
        # Test = splitword(Data[i][1][x])
        From = Data[i][0]
        for q in range(len(From)):
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
        # print(Num4)
        # print(Num1)
        # print(tester)
        for Num in Num523:
            if Num1[0] in Num and Num1[1] in Num:
                Num3 = Num
            elif tester[0] in Num and tester[1] in Num:
                Num5 = Num
            else:
                Num2 = Num

        for Num in Num069:
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
    # print(wholeList)

    # print(Data)
    # print(Data[0])
    # print(Data[0][1])
    # print(Data[0][1][0])
    # print(Data[0][1][0][0])
    # print(wholeList)
    # print(Data[i][1])




    for line in range(len(Data)):
        rightNumber = ""
        for test in range(4):
            for element in range(10):
                if len(Data[line][1][test]) == len(wholeList[element]):
                    counter = 0
                    for Char in range(len(Data[line][1][test])):
                        if Data[line][1][test][Char] in wholeList[element]:
                            counter = counter + 1
                        else:
                            break
                    if counter == len(Data[line][1][test]):
                        rightNumber = rightNumber + str(wholeList.index(wholeList[element]))
                        break
        if len(rightNumber) == 4:
            break
    final_answer.append(rightNumber)
        # print(final_answer)
        # print(rightNumber)
        # if len(final_answer[line]) == 4:
        #     break

print(final_answer)
# print(Data)
# print(Storage)
# print(Final)
file1.close()
