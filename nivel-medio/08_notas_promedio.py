# -*- coding: cp1252 -*-
n = int(input("Ingrese el número de notas... "))
notas = []
suma = 0
mayores = []
menores = []

for i in range(n):
    nota = float(input(f"Ingrese la nota #{i+1}: "))
    notas.append(nota)
    suma += nota

promedio = suma / n
print(f"\nLas notas son: {notas}")
print(f"El promedio del curso es: {promedio:.2f}")

mejor = max(notas)
peor = min(notas)
print(f"La mejor nota es: {mejor}")
print(f"La peor nota es: {peor}")

#Clasificación según el promedio
nbp = 0
for nota in notas:
    if nota >= promedio:
        mayores.append(nota)
    else:
        menores.append(nota)
        nbp += 1

print(f"\nNotas mayores o iguales al promedio: {mayores}")
print(f"Notas menores al promedio: {menores}")
print(f"Número de estudiantes por debajo del promedio: {nbp}")
