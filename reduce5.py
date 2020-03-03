import sys
def reduce(lines):
    ObjContadorcito ={}
    ObjContadorcito2={}
    for line in lines:
        line = line.split(",")
        word = line[0]
        number =line[1]
        if word in ObjContadorcito:
            ObjContadorcito[word]+=int(number)
        else:
            ObjContadorcito[word]=1
    for i in ObjContadorcito:
        year = str(i).split("-")[0]
        month = str(i).split("-")[1]
        sell = ObjContadorcito[i]
        if year in ObjContadorcito2:
            seller=ObjContadorcito[year + "-" + str(ObjContadorcito2[year])]
            if sell>seller:
                ObjContadorcito2[year]=month
        else:
            ObjContadorcito2[year]=month
    return ObjContadorcito2
lines = []
for line in sys.stdin:
    lines.append(line.strip())
a = reduce(lines)
for word, number in a.items():
    out = str(word)+","+str(number) 
    print(out)
