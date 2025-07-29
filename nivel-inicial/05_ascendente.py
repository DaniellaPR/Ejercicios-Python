#-*-coding:cp1252-*-
print("Ingrese número en orden ascendente")  #Indicar de qué trata el programa

anterior = -1
es_ascendente = True

while es_ascendente:
    num = int(input("Ingrese un entero positivo (con cero finaliza)... "))
    if num == 0:
        break
    if num <= anterior:
        es_ascendente = False
    anterior = num

if es_ascendente:
    print("Los números que ingresó están en orden ascendente\n")
else:
    print("Los números que ingresó NO están en orden ascendente\n")

print("Gracias por usar el programa...")
