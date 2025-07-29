import math
numeros = []
entrada = "algo"
contador = 1

while entrada != "":
    entrada = input(f"Ingrese dato {contador} (o Enter para terminar): ")
    if entrada != "":
        numeros.append(float(entrada))
        contador += 1

media = sum(numeros) / len(numeros)
suma_cuadrados = sum((x - media) ** 2 for x in numeros)
desviacion = math.sqrt(suma_cuadrados / (len(numeros) - 1))

print(f"\nMedia: {media}")
print(f"Desviación estándar: {round(desviacion, 2)}")
