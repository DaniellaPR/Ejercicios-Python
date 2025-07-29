#-*-coding:cp1252-*-
cad = input("Ingrese una oración... ").strip()
palabras = cad.split()

print(f"\n\"{cad}\" tiene {len(palabras)} palabras que son:\n")
for palabra in palabras:
    print(palabra)
