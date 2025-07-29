#-*-coding:cp1252-*-
import random
# Constantes
min = 0  # Dígito más bajo para obtener aleatorios
max = 10  # Dígito más alto para obtener aleatorios

cod = None
m = 0
n = 0
otro = 's'

while otro == 's':
    print("Generación de código bancario")
    m = int(input("¿De cuántos dígitos desea el código?... "))
    n = int(input("¿Cuántas veces desea que aparezcan cada uno de los 2 dígitos que deben repetirse?... "))
    sol = None
    if m >= n*2:
        # Generar los 2 valores especiales que se repetirán
        r1 = random.randint(min, max-1)
        r2 = random.randint(min, max-1)
        while r2 == r1:
            r2 = random.randint(min, max-1)
        
        # Llenar el arreglo con valores aleatorios excepto los especiales
        arr = [0] * m
        i = 0
        while i < len(arr):
            aleat = random.randint(min, max-1)
            if aleat != r1 and aleat != r2:
                arr[i] = aleat
                i += 1
        
        # Colocar los valores especiales en posiciones aleatorias
        i = 0
        while i < n:
            pos_aleat = random.randint(min, len(arr)-1)
            if arr[pos_aleat] != r1:
                arr[pos_aleat] = r1
                i += 1
        i = 0
        while i < n:
            pos_aleat = random.randint(min, len(arr)-1)
            if arr[pos_aleat] != r1 and arr[pos_aleat] != r2:
                arr[pos_aleat] = r2
                i += 1
        sol = arr
    cod = sol
    if cod is None:
        print("No es posible generar el código")
    else:
        print("Código generado:", cod)
    otro = input("¿Desea generar otro código (s/n)?... ").lower()
    print("\n")
print("Gracias por usar este programa. Presione tecla para finalizar...")
