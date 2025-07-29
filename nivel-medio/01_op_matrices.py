#-*-coding:cp1252-*-
a = []
b = []
s = []
r = []
i = 0
j = 0
nf = 0
nc = 0
nf = int(input("Ingrese el npumero de filas para las matrices... "))
nc = int(input("Ingrese el npumero de columnas para las matrices... "))

#Generacíón de 4 matrices
a = [[0 for i in range(nc)] for j in range(nf)]
b = [[0 for i in range(nc)] for j in range(nf)]
s = [[0 for i in range(nc)] for j in range(nf)]
r = [[0 for i in range(nc)] for j in range(nf)]

#Ingreso de las matrices A y B
print("Va a ingresar la matriz A")
for i in range(nf):
    for j in range(nc):
        print(f"Matriz A, ingrese el elemento [{i}][{j}]...", end = "")
        a[i][j] = int(input())
print("Va a ingresar la matriz B")
for i in range(nf):
    for j in range(nc):
        print(f"Matriz B, ingrese el elemento [{i}][{j}]...", end = "")
        b[i][j] = int(input())

#Ver matrices
print("Matriz A")
for i in range(len(a)):
    print("|", end = "")
    for j in range(len(a[0])):
        if a[i][j] < 100:
            print(" ", end = "")
        print(str(a[i][j])+ " ", end = "")
    print("|")

print("Matriz B")
for i in range(len(b)):
    print("|", end = "")
    for j in range(len(b[0])):
        if b[i][j] < 100:
            print(" ", end = "")
        print(str(b[i][j])+ " ", end = "")
    print("|")

#Se hace la suma y resta
for i in range(nf):
    for j in range(nc):
        s[i][j] = a[i][j] + b[i][j]
        r[i][j] = a[i][j] - b[i][j]

#Multiplicación
if len(a[0]) != len(b):
    raise ValueError("Las matrices no son multiplicables")
    
# Crear la matriz resultante C con el tamaño adecuado
filas_a = len(a)
columnas_b = len(b[0])
C = [[0] * columnas_b for _ in range(filas_a)]
    
# Realizar la multiplicación de matrices
for i in range(filas_a):
    for j in range(columnas_b):
        for k in range(len(b)):
            C[i][j] += a[i][k] * b[k][j]

#Ver multiplicación
print()
print("Multiplicacion A * B")
for i in range(nf):
    print("|", end = "")
    for j in range(nc):
        if C[i][j] < 10:
            print(" ", end = "")
        print(str(C[i][j])+ " ", end = "")
    print("|")
        
#Resultados
print()
print("Suma A + B")
for i in range(nf):
    print("|", end = "")
    for j in range(nc):
        if s[i][j] < 10:
            print(" ", end = "")
        print(str(s[i][j])+ " ", end = "")
    print("|")
print()
print("Resta A - B")
for i in range(nf):
    print("|", end = "")
    for j in range(nc):
        if r[i][j] < 10:
            print(" ", end = "")
        print(str(r[i][j])+ " ", end = "")
    print("|")
print()
