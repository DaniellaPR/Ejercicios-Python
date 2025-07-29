#-*-coding:1252-*-
n = int(input("¿Cuántos primos?... "))
i = 2
j = 0
cont = 0
while cont < n:
    primos = True  
    for j in range(2, i):
        if i%j == 0:
            primos = False
            break
    if primos:
        print(i, end = " ")
        cont += 1
    i += 1
print("Gracias por usar el programa")
