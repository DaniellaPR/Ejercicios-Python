#-*-coding:cp1252-*-
cad = str(input("Ingrese una cadena... "))
inv = ""
i = len(cad)-1
while i>=0:
    inv += cad[i]
    i -= 1
print(inv)
print()
