import sys
def Count(lines):
    ObjContadorcito = []
    for words in lines:
        words = words.lower()
        words = words.strip()
        year=((str((str(words.split(",")[2])).split(" ")[0])).split("-")[0])
        month = ((str((str(words.split(",")[2])).split(" ")[0])).split("-")[1])
        ObjContadorcito.append([year + "-" + month, 1])
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




def contar(lineas):
    contador = []
    for palabras in lineas:
        palabras = palabras.lower()
        palabras = palabras.strip()
        anio = ((str((str(palabras.split(",")[2])).split(" ")[0])).split("-")[0])
        mes = ((str((str(palabras.split(",")[2])).split(" ")[0])).split("-")[1])
        contador.append([anio + "-" + mes, 1])
    return contador


lineas = []

for linea in sys.stdin:
    if linea[0] == '{':
        lineas.append(linea.strip())

contador = contar(lineas)

for conteo in contador:
    palabra = conteo[0]
    numero = conteo[1]
    salida = str(palabra) + "," + str(numero)
    print(salida)
