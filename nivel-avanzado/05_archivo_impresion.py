#-*-coding:cp1252-*-
f = str(input("Ingrese la frase que desea imprimir: "))
n = int(input("Ingrese cuantas veces desea que se repita: "))
e = str(input("Ingrese cuanto espacio desea: "))
a = str(input("Ingrese el ancho máximo: "))
x = 0

archivo = "Salida.txt"
k = 0
while x < n:
    while k<a:
        j = " "
        for i in range(a):
            print(f"{j*(e*i)}+{f}")
            k += 1
            i += 1
    else:
        j = " "
        for i in range(a-1):
            while k<a:
                print(f"{j*(e*i)}+{f}")
                k += 1
            i += 1
        
arch = open(archivo, "w")
