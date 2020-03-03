import sys
def reduce(lines):
    ObjContadorcito = {}
    ObjContadorcito2 = {}
    ObjContadorcito3 = {}
    for line in lines:
        line = line.split(",")
        state = line[0]
        city = line[1]
        if state in ObjContadorcito:
            ObjContadorcito[state].add(city)
        else:
            ObjContadorcito[state] = {city}
    for item in ObjContadorcito:
        if (len(ObjContadorcito[item])) in ObjContadorcito2:
            ObjContadorcito2[len(ObjContadorcito[item])] += 1
        else:
            ObjContadorcito2[len(ObjContadorcito[item])] = 1
    for item in ObjContadorcito2:
        ObjContadorcito3[ObjContadorcito2[item]] = item
    return ObjContadorcito3
lines = []
for line in sys.stdin:
    lines.append(line.strip())
a = reduce(lines)
for word, number in a.items():
    Out = str(word) + "," + str(number)
    print(Out)
