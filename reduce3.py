import sys
def reduce(lines):
    ObjContadorcito = {}
    for line in lines:
        line = line.split(",")
        word = line[0]
        price = int(line[1])
        number =line[2]
        if word in ObjContadorcito:
            if price < ObjContadorcito[word][0]:
                ObjContadorcito[word][0] = price
                ObjContadorcito[word][1] = number
        else:
            ObjContadorcito[word] = [price, number]
    for i in ObjContadorcito:
        ObjContadorcito[i]=(str(list(ObjContadorcito[i])))
    return ObjContadorcito
lines = []
for line in sys.stdin:
    lines.append(line.strip())
a = reduce(lines)
for word, number in a.items():
    out = str(word) + "," + str(number)
    print(out)
