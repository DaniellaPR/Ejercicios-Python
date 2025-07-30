#-*-coding:cp1252-*-
import random
# Función para generar el campo de minas
def generar_campo(porc, longitud):
    # Inicializar el campo con 0 (sin minas)
    minas = [0] * longitud
    # Calcular el número de minas basadas en el porcentaje
    num_minas = (porc * longitud) // 100
    for i in range(num_minas):
        m_colocada = False
        while not m_colocada:
            pos_mina = random.randint(0, longitud-1)
            if minas[pos_mina] != -1:  # Si no hay mina en esa posición
                minas[pos_mina] = -1  # Colocar una mina
                m_colocada = True

    # Actualizar los números alrededor de las minas
    for i in range(longitud):
        if minas[i] == -1:  # Si es una mina
            if i > 0 and minas[i - 1] != -1:
                minas[i - 1] += 1  # Aumentar la cuenta de minas alrededor
            if i < longitud - 1 and minas[i + 1] != -1:
                minas[i + 1] += 1  # Aumentar la cuenta de minas alrededor
    return minas

# Función para ver el campo de juego
def ver_campo(minas, abierto):
    for i in range(len(minas)):
        if abierto[i]:  # Si la casilla está abierta
            if minas[i] == -1:
                print("*", end=" ")  # Si es mina, mostrar "*"
            else:
                print(minas[i], end=" ")  # Mostrar el número de minas alrededor
        else:
            print("-", end=" ")  # Si la casilla no está abierta, mostrar "-"
        
        # Añadir salto de línea después de cada 10 casillas
        if (i + 1) % 10 == 0:
            print()
    print()
    
    # Mostrar la numeración de las posiciones en la parte inferior
    for i in range(1, len(minas) + 1):
        print(i, end=" ")
    print()

# Función para jugar el juego
def jugar(minas):
    r = 0
    num_minas = minas.count(-1)  # Contar el número de minas
    abierto = [False] * len(minas)  # Inicializar el estado de las casillas (todas cerradas)
    print("El siguiente grupo de guiones representa el campo de minas:")
    
    while r == 0:
        ver_campo(minas, abierto)
        op = int(input("¿Qué posición quieres abrir? (1 a " + str(len(minas)) + "): ")) - 1
        
        if op < 0 or op >= len(minas):  # Comprobar que la posición es válida
            print("Posición inválida, por favor elige una posición válida.")
            continue

        abierto[op] = True  # Marcar la casilla como abierta

        if minas[op] == -1:  # Si es mina
            r = 2  # Fin del juego, el jugador ha perdido
        if sum(abierto) == len(minas) - num_minas:  # Si se han abierto todas las casillas sin minas
            r = 1  # El jugador ha ganado

    if r == 1:
        print("¡Felicidades, has ganado!")
    elif r == 2:
        print("¡Era una mina... has perdido!")
        print("El campo era el siguiente:")
        for i in range(len(abierto)):
            abierto[i] = True  # Abrir todas las casillas
        ver_campo(minas, abierto)

# Función para iniciar el juego
def iniciar_juego():
    n = 0
    print("Bienvenido al juego de Buscaminas")
    while n < 8 or n > 50:  # Limitar el tamaño del campo entre 8 y 50
        n = int(input("¿Cuál es la longitud del campo de juego? (entre 8 y 50): "))
    return n

# Bucle principal para jugar múltiples rondas
rep = "s"
while rep == "s":
    n = iniciar_juego()  # Obtener la longitud del campo
    porc = 25  # Porcentaje de minas (puedes cambiar este valor si deseas)
    minas = generar_campo(porc, n)  # Generar el campo con minas
    jugar(minas)  # Iniciar el juego
    rep = input("¿Deseas jugar de nuevo? (s/n): ").lower()  # Preguntar si el jugador quiere jugar nuevamente
