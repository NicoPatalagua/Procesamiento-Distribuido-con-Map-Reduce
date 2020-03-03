import sys
def Count(lines):
    ObjContadorcito = []
    for words in lines:
        words = words.lower()
        words = words.strip()
        year = ((str((str(words.split(",")[2])).split(" ")[0])).split("-")[0])
        ObjContadorcito.append([year, 1])
    return ObjContadorcito
lines = []
for linea in sys.stdin:
    if linea[0] == '{':
        lines.append(linea.strip())
a = Count(lines)
for Counter in a:
    word = Counter[0]
    number = Counter[1]
    Out = str(word) + "," + str(number)
    print(Out)
