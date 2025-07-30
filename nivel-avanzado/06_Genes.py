# 5               ← Número de genes
# 2               ← Número de mutaciones reversas
# 2 4             ← Mutación 1 (invertir genes entre 2 y 4)
# 1 3             ← Mutación 2
# 3               ← Número de consultas
# 5               ← ¿Dónde está el gen 5?
# 2               ← ¿Dónde está el gen 2?
# 4               ← ¿Dónde está el gen 4?
# 0               ← Fin del programa

#-*-coding:cp1252-*-
    """
    Realiza una mutación reversa en el genoma desde la posición i hasta j.
    Las posiciones están basadas en 1, así que se ajustan para listas en Python.
    """
def mutacion_inversa(genoma, i, j):
    mut = []
    for k in range(j-1, i-2, -1):
        mut.append(genoma[k])
    genoma = genoma[:i-1] + mut + genoma[j:]
    return genoma
def leer_genes(nombre):
    archivo = open(nombre, "r")
    lista = []
    linea = archivo.readline().strip()
    lista.append(linea.strip())
    while linea != "":
        linea = archivo.readline().strip()
        if linea != "":
            lista.append(linea.strit())
    archivo.close()
    return lista

i = 0
contElementos = 0
contGenomas = 1
n = r = q = qi = pos = ini = fin = 0
texto = ""

datos = leer_genes("genes.txt")
n = int(datos[contElementos])
contElementos += 1

while n != 0:
    genoma = []
    for i in range(n):
        genoma.append(i+1)
    r = int(datos[contElementos])
    contElementos += 1
    for i in range(r):
        parejaIniFin = datos[contElementos].split(" ")
        contElementos += 1
        ini = parejaIniFin[0]
        fin = parejaIniFin[1]
        genoma = mutacion_inversa(genoma, ini, fin)
    q = int(datos[contElementos])
    contElementos += 1
    texto += "Genoma " + str(contGenomas) + "\n"
    contGenomas += 1
    for i in range(q):
        q1 = int(datos[contElementos])
        contElementos += 1
        pos = int(genoma.index(q1)) + 1
        texto += str(pos) + "\n"
    n = int(datos[contElementos])
    contElementos += 1

print(texto)
archivo = open("out.txt", "w")
archivo.write(texto)
archivo.close()

print("Gracias por usar el programa")

#Versión 2:
def mutacion_reversa(genoma, i, j):
    """
    Realiza una mutación reversa en el genoma desde la posición i hasta j.
    Las posiciones están basadas en 1, así que se ajustan para listas en Python.
    """
    i -= 1
    genoma[i:j] = genoma[i:j][::-1]
    return genoma
  
def leer_genes(nombre_archivo):
    """
    Lee el archivo 'genes.txt' y devuelve una lista de líneas sin saltos de línea.
    """
    with open(nombre_archivo, "r") as archivo:
        return archivo.read().splitlines()

datos = leer_genes("genes.txt")

indice = 0
caso = 1
salida = ""

while True:
    n = int(datos[indice])
    indice += 1
    if n == 0:
        break

    genoma = list(range(1, n + 1))
    r = int(datos[indice])
    indice += 1

    for _ in range(r):
        i, j = map(int, datos[indice].split())
        indice += 1
        genoma = mutacion_reversa(genoma, i, j)

    q = int(datos[indice])
    indice += 1
    salida += f"Genoma {caso}\n"

    for _ in range(q):
        gene = int(datos[indice])
        indice += 1
        posicion = genoma.index(gene) + 1
        salida += str(posicion) + "\n"
    caso += 1

print(salida)
with open("out.txt", "w") as archivo:
    archivo.write(salida)

print("Gracias por usar el programa.")
