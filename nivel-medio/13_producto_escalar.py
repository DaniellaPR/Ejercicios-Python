#-*-coding:cp1252-*-
print("Ingrese datos para el primer vector:")
v1 = [int(input(f"Componente {i+1}: ")) for i in range(3)]

print("\nIngrese datos para el segundo vector:")
v2 = [int(input(f"Componente {i+1}: ")) for i in range(3)]

producto_escalar = 0
for i in range(3):
    producto = v1[i] * v2[i]
    producto_escalar += producto

print("\nPrimer vector:", v1)
print("Segundo vector:", v2)
print(f"\nEl producto escalar de los vectores ingresados es: {float(producto_escalar)}")
