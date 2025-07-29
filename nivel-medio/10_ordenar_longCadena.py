# -*- coding: cp1252 -*-
c = input("Ingrese una cadena de caracteres... ")
pal = c.split()

# Ordenamos con sorted y una función clave: la longitud
pal_ordenadas = sorted(pal, key=len)

print("\nPalabras ordenadas por longitud:")
for i, palabra in enumerate(pal_ordenadas):
    print(f"palabra[{i+1}] = {palabra}")
