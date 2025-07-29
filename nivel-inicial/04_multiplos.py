#-*-coding:cp1252-*-
mul = int(input("Ingrese un numero para sacar el múltiplo: "))
ter = int(input("Ingrese cuántos múltiplos: "))
i=1
print(f"Los primeros {ter} múltiplos del número {mul} son: ")
while ter>i:
    print(str(mul*i), end=(', '))
    i +=1

print("\nGracias por usar el programa...")
