#-*-coding:cp1252-*-
cad = str(input("Ingrese una cadena... "))
original = cad
sep = ' '
i = 0
j = 0
cad = cad.lower().replace(" ", "")
letrasiguales = True
j = len(cad)-1
while i<j:
    if i != " " and j != " ":
        if cad[i] != cad[j]:
            letrasiguales = False
            break
        i += 1
        j -= 1

if (letrasiguales):
    print(f"{original} si es un palíndromo")
else:
    print(f"{original} no es un palíndromo")
