#-*-coding:1252-*-
print("Bienvenido al sistema de devolución de libros")                                #Bienvenida al programa
an_esperado = int(input("Ingrese el año esperado de devolución del libro... "))      #Preguntar por la fecha esperada de devolución
mes_esperado = int(input("Ingrese el mes esperado de devolución del libro... "))
dia_esperado = int(input("Ingrese el día esperado de devolución del libro... "))

an_dev = int(input("Ingrese el año en que se devolvió el libro... "))                 #Preguntar por la fecha de devolución
mes_dev = int(input("Ingrese el mes en que se devolvió el libro... "))
dia_dev = int(input("Ingrese el día en que se devolvió el libro... "))


anos = (an_dev-an_esperado)                                                          #Para saber cuantos días, meses o años se pasó
meses = (mes_dev-mes_esperado)                      
dias = (dia_dev-dia_esperado)
                                   #Establecemos un condicionante para saber si su cumplen mas de 30 días entre mes y mes
if dias<0 and meses!=0:                               #Y al mismo tiempo asegurara la condicion para devolver el libro antes de la fecha establecida                                           
    dias= 30+dias
    meses-=1
if meses<0:                                         #Establecesmos un condicional para arreglar un posible error en el condicionante anterior
    meses=0
dias_impresion=dias                                 #Guardamos el valor de días para poder imprimir posteriormente

centavos=0
multa=True
if anos>0 or meses>0 or dias>0:                             #Hacemos condicionales para saber el valor de las multas
        centavos=0
        if an_dev != an_esperado:
            centavos=10000
            multa=False
        while mes_dev != mes_esperado:
            mes_esperado +=1
            centavos +=500
            multa=False         
        while dias>0:
            centavos +=15
            dias -=1         
               

if centavos != 0:                                            #si hay multa la imprimirá, asi como el número de días que se pasó
    print("\nSe pasó con", str(dias_impresion), "día(s),", str(meses), "mes(es),", str(anos), "año(s),")
    print(f"Su multa es de {centavos} centavos")
else:                                                        #Si no, indicará que no tiene multa
    print("\nNo tiene multa. Lo ha devuelto puntualmente.")

print("\nGracias por usar el programa")                      #Indicar que finalizó el programa
