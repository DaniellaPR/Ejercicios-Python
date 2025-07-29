#-*-coding:1252-*-
#Definimos las variables
print("Enter para acabar...")
condicion="a"
materia=[]
notas=[]
contador=1
vacio=23
repetir=False
while condicion!="":    
    condicion=input("Ingrese el nombre de la materia: ")
    materia.append(condicion)    
    if condicion != "":
        notas.append(float(input("Ingrese la calificación de la materia: ")))
        
materia=materia[:-1]

print("Los datos recibidos son:")
print("MATERIA"," "*23,"CALIFICACIÓN")
print("-------"," "*23,"------------")
for i in range(len(materia)):
    espacio=35-len(materia[i])
    print(materia[i]," "*espacio,notas[i])
    
print("\nAsignaturas a repetir:")

for i in range(len(materia)):
    if notas[i]<6:
        espacio=35-len(materia[i])
        print(materia[i]," "*35,notas[i])
        repetir=True
    
if repetir==False:
    print("Felicidades no tiene materias por repetir")
