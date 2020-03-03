import sys
def reduce(lines):
    ObjContadorcito = []
    for line in lines:
        line = line.split(",")
        city = line[0]
        price = line[1]
        year = line[2]
        if year =='2015' and city =='stamford':
            ObjContadorcito.append(price)
    ObjContadorcito.sort()
    return ObjContadorcito
lines = []
for line in sys.stdin:
    lines.append(line.strip())
a = reduce(lines)
for price in a:
    Out = str(price)
    print(Out)