#-*-coding:cp1252-*-

# Realice un programa que le pregunte al usuario cuántos términos desea visualizar, Los términos se presentarán como fracciones en 
# donde el numerador del siguiente número será una unidad más que el anterior, lo mismo con el denominador. Se deberá imprimir por consola
# el resultado de la suma de dichos términos. Se deberá preguntar al usuario si desea repetir el proceso. 
# Si se ingresan valores menores a cero o mayores a 10000, el programa debe indicar que no puede generar la serie.


pase="s"    
i=0
total=0
while pase=="s" :
    terminos=int(input("Cuantos terminos desea visualizar?... "))    
    if  terminos<0 or terminos>10000:
       print("No se puede generar dicha serie")
    else:            
        for i in range(1,terminos+1):
            actual= i / (i+1)
            total +=actual
            impresion=str(f"{i}/{i+1}")
            if i==terminos:
                print(impresion,end=" = ")
            else:
                print(impresion,end=" + ")
        print(total)
    pase=input("Desea repetir el proceso? (s/n)... ")
