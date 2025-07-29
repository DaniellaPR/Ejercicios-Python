#-*-coding:cp1252-*-
frase=input("Ingrese la cadena: ")
minus=frase.lower()
mayus=frase.upper()
mayusculas=0
minusculas=0
for i in range(len(frase)):
    if frase[i]!=minus[i]:
        mayusculas+=1
    elif frase[i]!=mayus[i]:
        minusculas+=1

print(f"Mayuculas: {mayusculas}")
print(f"Minusculas: {minusculas}")
