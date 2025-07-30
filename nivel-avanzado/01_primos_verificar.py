#-*-coding:cp1252-*-
import math
def es_primo(x):
    if x <=1:
        return False
    for i in range(2, x//2 + 1):
        if x %i== 0:
            return False
    return True

r = "s"
while r.lower() == "s":
    num = int(input("Ingrese un número para saber si es primo o no: "))
    if es_primo(num):
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")
    r = input("¿Desea verificar otro número? (s/n): ")

print("\nGracias por usar el programa...\n")
