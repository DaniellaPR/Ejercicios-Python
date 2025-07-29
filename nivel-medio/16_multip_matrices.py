#Ejercicio 3
#-*-coding:cp1252
#Escribir un programa que permita ingresar dos matrices, donde la primera matriz es de 2x3 y la segunda es de 3x2, como las del ejemplo

#Definicion de variables
m1=[[0 for i in range(3)] for j in range(2)]
m2=[[0 for i in range(2)] for j in range(3)]
m3=[[0 for i in range(2)] for j in range(2)]

#Solicitamos al usuario los datos
for i in range(2):
    for j in range(3):
        m1[i][j]=int(input(f"Ingrese dato componente {i+1},{j+1}: "))        


for i in range(3):
    for j in range(2):
        m2[i][j]=int(input(f"Ingrese dato componente {i+1},{j+1}: "))

#Realizamos el proceso

for i in range(2):
    for j in range(2):
        for k in range(3):
            m3[i][j]+=m1[i][k]*m2[k][j]
            
#Imprimimos los resultados
print("\nEl producto de multiplicar la primera por la segunda matriz ingresadas es: ")

for i in range(2):
    for j in range(2):
        if j==0:
            print("|",end=" ")
        if 0<=m3[i][j]<10:    
            print("    ",m3[i][j],end=" ")
        elif -10<m3[i][j]<0:
            print("   ",m3[i][j],end=" ")
        elif -100<m3[i][j]<=-10:
            print("  ",m3[i][j],end=" ")
        elif -1000<m3[i][j]<=-100:
            print(" ",m3[i][j],end=" ")
        elif 10<=m3[i][j]<100:
            print("  ",m3[i][j],end=" ")
        elif 100<=m3[i][j]<1000:
            print(" ",m3[i][j],end=" ")
        
    print("|")
