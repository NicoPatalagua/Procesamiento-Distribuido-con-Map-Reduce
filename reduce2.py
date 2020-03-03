import sys
def reduce(lines):
    ObjContadorcito = {}
    for line in lines:
        line = line.split(",")
        word = line[0]
        price = int(line[1])
        number = int(line[2])
        if word in ObjContadorcito:
            ObjContadorcito[word][0] += price
            ObjContadorcito[word][1] += number
        else:
            ObjContadorcito[word] = [price, number]
    for i in ObjContadorcito:
        ObjContadorcito[i]=(int(list(ObjContadorcito[i])[0])/int(list(ObjContadorcito[i])[1]))
    return ObjContadorcito
lines = []
for line in sys.stdin:
    lines.append(line.strip())
a = reduce(lines)
for word, number in a.items():
    out = str(word) + "," + str(number)
    print(out)