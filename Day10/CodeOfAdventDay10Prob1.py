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

for Line in range(len(Syntax)):
    Stack = []
    for Bracket in range(len(Syntax[Line])):
        bracket = Syntax[Line][Bracket]
        if bracket in Openings:
            Stack.append(bracket)
        else:
            if Openings.index(Stack.pop()) != Closing.index(bracket):
                error.append(bracket)
                break

print(error.count(")")*3 + error.count("]")*57 + error.count("}") * 1197 + error.count(">")*25137)
