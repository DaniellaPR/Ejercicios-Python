#-*-coding:cp1252-*-
import random
ga = []
nga = 0
gb = []
ngb = 0
rep = [] #Almacena ga y gb
max = 0 #Límite máximo
i = 0 #Contador segundo grupo
j = 0 #Contador segundo grupo

max = int(input("Indique límite máximo de valores... "))
nga = int(input("Tamaño del primer grupo de datos... "))
ngb = int(input("Tamaño del segundo grupo de datos... "))

ga = [0]*nga
gb = [0]*ngb

for i in range(nga):
    ga[i] = random.randint(1, max)
    
for i in range(ngb):
    gb[i] = random.randint(1, max)
    
print(f"Grupo 1: {ga}")
print(f"Grupo 1: {gb}")

for i in range(nga):
    for j in range(ngb):
        if ga[i] == gb[j] and ga[i] not in rep:
            rep.append(ga[i])
rep.sort()
print(f"Repetidos: {rep}")

print("Gracias por usar este programa")
