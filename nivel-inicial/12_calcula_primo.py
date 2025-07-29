#-*-coding:1252-*-
i = 0                                                                                #Dfinir cada variable
k = 0
j = 0
primo = True
nuevo = None
verdadero = True

print("El programa finaliza con cualquier número menor o igual a cero")              #Indicar como funciona el programa

while verdadero:                                                                     #Bandera para saber si cumple la condición para que siga, a través de un bucle
    n = int(input("Ingrese un número entero positivo... "))                          #Ingreso de número por el usuario
    if n <= 0:                                                                       #Si cumple la condición no se repetirá el buble
        verdadero = False
        break

    primo = True                                                                     #Bandera de número primo
    if n <= 1: 
        primo = False
    else:
        for i in range(2, n//2+1):                                                   #Para optimizar, dividir el número a la mitad. No calculará demasiadas divisiones.
            if n % i == 0:                                                           #Si el residuo es cero, no es primo
                primo = False
    if primo:                                                                        #Si es primo buscar el contador
        print(f"El {n} si es primo")
        cont = 0
        for j in range (2, n + 1):                                                   #Contar todos los primos desde el 2 como primer primo hasta el número ingresado
            nuevo = True                                                             #Identificar todos estos número scontados como un nuevo primo
            for k in range (2, j):
                if j % k == 0:                                                       #Si no es primo no va a hacer nada
                    nuevo = False
            if nuevo:                                                                #Si es primo, se sumará en un contador
                cont += 1
        print(f"El {n} ocupa el puesto {cont} en el listado de números primos.\n")
    else:                                                                            #Si no es primo, indicarlo
        print(f"El {n} no es primo\n")
        
        
print("Gracias por usar el programa")
    
