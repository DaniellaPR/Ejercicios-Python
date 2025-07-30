#-*-coding: cp1252-*-
archivo = "archivo.txt"
linea = ""

print("   BLOQUE DE NOTAS   ")
print()
print("Escriba líneas de texto para almacenarlas en un archivo (archivo.txt)")
print("Cuando su archivo esté completo, escriba FIN (en mayúsculas)")
print()

with open(archivo, "w") as file:
    while True:
        linea = input("> ")
        if linea == "FIN":
            break
        file.write(linea + "\n")

print("\nEl archivo se ha generado correctamente.\n")

print("Contenido del archivo:")
with open(archivo, "r") as file:
    for linea in file:
        print(linea.strip())

print("\nGracias por usar el bloc de notas.")
