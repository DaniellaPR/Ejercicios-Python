#-*-coding:cp1252-*-
#Corrección del ejercicio de PI por la serie de Leibniz
#Por: Jorge Alarcón
i = 0 #Contador para iterar
n = 0 #Número de términos de la serie
total = 0 #Sumatoria de términos
nuevo = "s" #Para repetir el proceso completo
termino = 0 #Cada término de la serie
num = 1 #Numerador de cada término
den = 1 #Denominador de cada término
pi = 0 #Valor calculado de pi
print ("Cálculo de pi mediante la serie de Leibniz")
while nuevo == "s":
    n = int(input("Ingrese el número de términos para calcular pi con base en la serie de Leibniz... "))
    if n < 1: #Para cuando coloca valores fuera de rango bajo 1
        print ("Se requiere de al menos 1 término para generar la serie")
    elif n>5000: #Para cuando coloca valores superiores al límite
        print("El límite de términos que este programa puede procesar es 5000")
    else: #Si se puede obtener la serie
        print("Serie: ", end="")
        num = 1
        den = 1
        total = 1.0 #Inicia con el valor del primer término
        for i in range(0, n):
            termino = num/den
            if i > 0: #Para imprimir el + o el - según corresponda, solo será con i > 0 porque el primer + no es visible, y también para sumar o restar el total.
                if i % 2 == 0: #Término par
                    print (" + ", end="")
                    total += termino
                else: #Término impar
                    print (" - ", end="")
                    total -= termino
            print ("("+str(num) + "/" + str(den)+")" , end="")
            den += 2
        pi = total * 4 #La serie calcula pi/4, así que se debe multiplicar por 4
        print()
        print(f"Con {n} términos el valor calculado de pi es: {pi}")
    nuevo = input("Desea generar un nuevo cálculo (s/n)?... ")
print("\nGracias por usar este programa")
