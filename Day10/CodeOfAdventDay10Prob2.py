file1 = open("AdventOfCodeDay10.txt", "r")
lines = file1.readlines()

Syntax = []
for x in lines:
    Syntax.append(x.replace("\n",""))

file1.close()

Stack = []

CurlyOP, CurlyCL = "{", "}"
SqrOP, SqrCL = "[", "]"
ParOP, ParCL = "(", ")"
AlliOP, AlliCL = "<", ">"

Openings = [CurlyOP, SqrOP, ParOP, AlliOP]
Closing = [CurlyCL, SqrCL, ParCL, AlliCL]

error = []
Line = 0
while Line != len(Syntax):
    Stack = []
    for Bracket in range(len(Syntax[Line])):
        bracket = Syntax[Line][Bracket]
        if bracket in Openings:
            Stack.append(bracket)
        else:
            if Openings.index(Stack.pop()) != Closing.index(bracket):
                del Syntax[Line]
                Line -= 1
                break
    Line += 1

print(Syntax)
Appendix = []
for Line in range(len(Syntax)):
    Stack = []
    Fix = []
    Syntax[Line] = Syntax[Line][::-1]
    for Bracket in range(len(Syntax[Line])):
        bracket = Syntax[Line][Bracket]
        if bracket in Closing:
            Stack.append(bracket)
        else:
            if len(Stack) == 0:
                Fix.append(Closing[Openings.index(bracket)])
                Appendix.append(Closing[Openings.index(bracket)])
            else:
                Temp = Stack.pop()
                if Closing.index(Temp) == Openings.index(bracket):
                    continue
                else:
                    Fix.append(Openings.index(Closing.index(Temp)))
                    Appendix.append(Openings.index(Closing.index(Temp)))
    Appendix.append("SPLIT")
    # Syntax[Line] = Syntax[Line][::-1] + Fix[Line]
del Appendix[-1]
print(Syntax)
print(Appendix)
print("".join(Appendix))
Data = ("".join(Appendix)).split("SPLIT")
print(Data)

total = []
for Object in Data:
    Score = 0
    for bracket in Object:
        Score = Score * 5
        if bracket == ")":
            Score += 1
        elif bracket == ">":
            Score += 4
        elif bracket == "}":
            Score += 3
        elif bracket == "]":
            Score += 2

    total.append(Score)

print(sorted(total)[int(len(total)/2)])
