import sys
def Count(lines):
    ObjContadorcito = []
    for words in lines:
        words = words.lower()
        words = words.strip()
        city = (str(words.split(",")[6]))
        price = (str(words.split(",")[1]))
        year = ((str((str(words.split(",")[2])).split(" ")[0])).split("-")[0])
        ObjContadorcito.append([city, price, year])
    return ObjContadorcito
lines = []
for i in sys.stdin:
    if i[0] == '{':
        lines.append(i.strip())
a= Count(lines)
for i in a:
    word = i[0]
    number = i[1]
    year = i[2]
    Out = str(word) + "," + str(number) + "," + str(year)
    print(Out)