#-*-coding:cp1252-*-

altura=int(input("Igrese la altura del triangulo: "))
inverso=altura                                          #Establecemos una variable que nos ayude a empezar desde la base del triangulo
for i in range (1,altura+1):    
    for j in range(inverso):        
        print("*",end="")
    inverso-=1
    print()
