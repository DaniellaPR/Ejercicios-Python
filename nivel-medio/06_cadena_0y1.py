#-*-coding:cp1252-*-
print("Va a ingresar datos que solo pueden ser cero o uno.")
print("Si ingresa un dato diferente, se entenderá que ya no desea más datos.\n")
lista = []
si =True
while si:
    try:
        n = int(input("Ingrese dato... "))
        if n == 0 or n == 1:
            lista.append(n)
        else:
            si = False
    except ValueError:
        print("Por favor, ingrese un número válido.")

c = lista.count(0)
uno = len(lista)-c
lista.clear()
lista.extend([0] * c)
lista.extend([1] * uno)

print(f"\nLista ordenada: {lista}")
