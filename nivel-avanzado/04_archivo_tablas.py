#-*-coding:cp1252-*-
n = int(input("Hasta que tsbla desea generar?: "))
for i in range(1, n+1):
    file = open(f"tabla{i}.txt", "w")
    with open(f"tabla{i}.txt", "w") as file:
        file.write(f"   Tabla del {i}   ")
        file.write(f"-------------------")
        for j in range(12):
            result = i*j
            file.write(f"{i} x {j} = {result}")
            j += 1
    i += 1
        
nombre = "tabla5.txt"
n = 5
max_val = 12
contenido = f"Tabla del {n}"

n = int(input("Hasta que tsbla desea generar?: "))
for i in range(1, n+1):
    f = open(f"tabla{i}.txt", "w")
    longitud = f.write(f"----- --- "+ "-"*(file-11)+"\n")
for j in range(12):
    f.write(f"{i+1} x {j+1} = {i+1}*{j+1}\n")
f.close()
