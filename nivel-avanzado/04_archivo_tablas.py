# -*- coding: cp1252 -*-
n = int(input("¿Hasta qué tabla desea generar?: "))

for i in range(1, n + 1):
    with open(f"tabla{i}.txt", "w") as file:
        file.write(f"   Tabla del {i}\n")
        file.write(f"{'-' * 20}\n")
        for j in range(1, 13):
            result = i * j
            file.write(f"{i} x {j} = {result}\n")

print(f"\nSe han generado {n} archivos de tablas correctamente.")
