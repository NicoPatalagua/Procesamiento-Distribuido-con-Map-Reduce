import sys
def Count(lines):
    ObjContadorcito = []
    for words in lines:
        words = words.lower()
        words = words.strip()
        city = (str(words.split(",")[6]))
        state = (str(words.split(",")[8]))
        ObjContadorcito.append([city,state])
    return ObjContadorcito
lines = []
for i in sys.stdin:
    if i[0] == '{':
        lines.append(i.strip())
ObjContadorcito = Count(lines)
for j in ObjContadorcito:
    city = j[0]
    state = j[1]
    Out = str(state) + "," + str(city)
    print(Out)