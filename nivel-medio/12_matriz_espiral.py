#-*-coding:cp1252-*-
# Definimos el número de filas y columnas de la matriz
nf = 8
nc = 8

# Inicializamos una matriz de nf x nc con todos los elementos en 0
arr = [[0 for i in range(nc)] for j in range(nf)]

# Inicializamos un contador que se usará para llenar la matriz
cont = 1

# Recorremos la matriz en espiral, empezando desde las esquinas y moviéndonos hacia el centro
for k in range(min(nf, nc)):
    # Llenamos la fila superior de la espiral actual
    i = k
    for j in range(k, nc-1-k+1):
        arr[i][j] = cont
        cont += 1

    # Llenamos la columna derecha de la espiral actual
    j = nc-1-k
    for i in range(k+1, nf-1-k+1):
        arr[i][j] = cont
        cont += 1

    # Llenamos la fila inferior de la espiral actual, si es que existe
    i = nf-1-k
    if i > k:
        for j in range(nc-2-k, k-1, -1):
            arr[i][j] = cont
            cont += 1

    # Llenamos la columna izquierda de la espiral actual, si es que existe
    j = k
    if j < nc-1-k:
        for i in range(nf-2-k, k, -1):
            arr[i][j] = cont
            cont += 1

# Imprimimos la matriz resultante
for i in range(nf):
    print("| ", end="")
    for j in range(nc):
        # Añadimos un espacio extra para los números de un solo dígito, para que la matriz se vea bien alineada
        if arr[i][j] < 10:
            print(" ", end="")
        print(arr[i][j], end=" ")
    print("|")
