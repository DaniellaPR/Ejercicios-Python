#-*-coding:cp1252-*-
#Hacer que el usuario ingrese el número especificado
num = int(input("Ingrese un número positivo mayor a 10..."))

if num>=10:
    cuadrado=num**2
    print(f"El cuadrado de {num} es {cuadrado}")
else:
    print("Usted no ha seguido las instrucciones, no se puede operar.")
print("Gracias por usar este programa.")
