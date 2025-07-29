#-*-coding:cp1252-*-
#Solicitar al usuario que ingrese el número máximo hasta donde buscar primos gemelos
maximo = int(input("¿Hasta qué valor desea buscar primos gemelos?... "))
gemelos = 0                                       #Contador de primos gemelos
#Dentro del rango 2 hasta el máximo que puso el usuario
for num in range(2, maximo+1):                    #Comprobar si el número es primo
    primo = True                                  #Banderas para determinar si son primos
    for i in range(2, int(num//2) + 1):           #Verificar si tiene divisores solo hasta la mitad para optimizar
        if num % i == 0:
            primo = False

    primo2 = True                                 #Solo si el número es primo, verificar si num+2 es primo también
    for i in range(2, int((num + 2)//2) + 1):
        if (num + 2) % i == 0:
            primo2 = False

    if primo and primo2:                          #Si ambos son primos aumentar el contador de gemelos
        gemelos += 1

print(f"Hasta el {maximo}, se han encontrado {gemelos} parejas de primos gemelos")
print("Gracias por usar este programa")
