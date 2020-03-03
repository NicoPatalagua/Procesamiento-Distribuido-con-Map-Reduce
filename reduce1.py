import sys
def reduce(lines):
    ObjContadorcito = {}
    for line in lines:
        line = line.split(",")
        word = line[0]
        number = line[1]
        if word in ObjContadorcito:
            ObjContadorcito[word] += int(number)
        else:
            ObjContadorcito[word] = 1
    return ObjContadorcito
lines = []
for line in sys.stdin:
    lines.append(line.strip())
a = reduce(lines)
for word, number in a.items():
    out = str(word) + "," + str(number)
    print(out)