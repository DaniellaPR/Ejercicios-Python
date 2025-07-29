#-*-coding:1252-*-
i=0
j=0
dc =0
dt =0
rep=None
primo = True
while rep!="n":
    n = int(input("Cuántos números?..."))
    for i in range (n):
        dc = n-1
        dt = i+1
        for j in range (i+1):
            print(dt, end = " ")
            dt += dc
            dc -= 1
        print()
    rep = input("Desea generar otra pirámide? (s/n)...")
print()
print("Fin del programa")
