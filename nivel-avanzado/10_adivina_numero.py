import random
import math

print("---------Bienvenido a adivina el número---------\n → Ingresa un rango")
lower = int(input("Ingrese el número más bajo: "))
upper = int(input("Ingrese el número más alto: "))

x = random.randint(lower, upper)
max_intentos = math.ceil(math.log(upper - lower + 1, 2))
print(f"Tienes solo {max_intentos} intentos para adivinar")

count = 0
while count < max_intentos:
    count += 1

    guess = int(input("Adivina un número: "))

    if guess == x:
        print("Yeii, lo hiciste en ",count, " intento/s")
        break
    elif guess > x:
        print("El número es más bajo!")
    else:
        print("El número es más alto!")

if count == max_intentos and guess != x:
    print("\nEl número era: ", x)
    print("\tNo adivinaste")
