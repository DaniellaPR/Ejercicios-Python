#-*-coding:cp1252-*-

def es_primo(x):
    if x <=1:
        return False
    for i in range(2, x//2 + 1):
        if x %i== 0:
            return False
    return True

def generar_primos(cantidad, desde):
    lista = []
    actual = desde
    while len(lista) < cantidad:
        if es_primo(actual):
            lista.append(actual)
        actual += 1
    return lista

t = int(input("Ingrese cuántos números primos desea: "))
v = int(input("Ingrese desde qué valor desea empezar: "))

primos = generar_primos(t, v)
print(f"\nLos primeros {t} números primos desde {v} son:")
print(primos)

print("Gracias por usar el programa...")
