#-*-coding:cp1252-*-
num = int(input("¿Cuántos datos va a ingresar?... "))
lista = []
for i in range(num):
    n = int(input(f"Ingrese el dato #{i+1}: "))
    lista.append(n)
mayor = lista[0]
for elemento in lista:
    if elemento>mayor:
        mayor = elemento

print(f"El mayor de {lista} es {mayor}")
print("Fin del programa")
