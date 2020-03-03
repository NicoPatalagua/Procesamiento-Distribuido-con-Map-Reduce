import sys
def Count(lines):
    ObjContadorcito = []
    for words in lines:
        words = words.lower()
        words = words.strip()
        city = (str(words.split(",")[6]))
        price = (str(words.split(",")[1]))
        ObjContadorcito.append([city, price, 1])
    return ObjContadorcito
lines = []
for linea in sys.stdin:
    if linea[0] == '{':
        lines.append(linea.strip())
a = Count(lines)
for Counter in a:
    word = Counter[0]
    number = Counter[1]
    contadorcito=Counter[2]
    Out = str(word) + "," + str(number)+","+str(contadorcito)
    print(Out)
