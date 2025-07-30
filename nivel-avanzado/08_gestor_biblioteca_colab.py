#-*-coding:cp1252-*-
#Ángel Chavez, Paula Pozo, Israel Hernández, Josué Tenesaca y Gabriel Vásconez
import os #Se importa la librería os que se utilizará para la función de cargar archivos

#------FUNCIÓN PARA AGREGAR LIBROS-----#
#Se define una función que permitirá al usuario agregar los datos de un libro nuevo en el archivo
def AgregarLibro():
    seguir="S"
    file=open(arch,"a")
    while seguir!="N" and seguir!="n":
        sf="Sin Información"
        print("\n"+"-"*40)
        print("De no conocer algun dato, presione ENTER")
        print("-"*40+"\n")
        #Con input el usuario ingresa el título del libro y el dato es registrado
        titulo=input("Ingrese el título del libro: ").strip()
        if titulo=="":
            titulo=sf
        #De la misma manera se ingresa el nombre del autor del libro
        autor=input("Ingrese el nombre del autor: ").strip()
        if autor=="":
            autor=sf
        #Finalmente se ingresa el año de publicación del libro
        publicacion=input("Ingrese el año de publicación: ").strip()
        if publicacion=="":
            publicacion=sf
        #Los datos ingresados por el usuario se escribiran en el archivo de texto
        file.writelines("-"+titulo+ "-" +autor+"-"+publicacion+"-"+"\n")
        #Se pregunta al usuario si desea ingresar un libro distinto
        seguir=input("\nDesea ingresar otro libro? (S/N): ")
        print()
    file.close()

#------FUNCIÓN PARA BUSCAR LIBROS-----#
#Se define una función que permitirá al usuario buscar un libro en el archivo según su Título, Autor o Año de publicación
def BuscarLibro():
    seguir="S"
    #Se lee el archivo de la lista de libros para tener todos los datos de los libros
    try:
        with open(arch,"r") as file:
            tamaño=len(file.readlines())
    except:
        print("No se ha registrado ninguna acción con el programa, no existe ningún archivo todavía")
    else:
        datos=[]
        while seguir!="N" and seguir!="n":
            print("Categorías de búsqueda disponibles:")
            print("  1)Título \n  2)Autor \n  3)Año de publicación \n")
            #Se le pide al usuario decidir de qué manera va a buscar su libro
            cat=input("¿Por qué categoría deasea buscar? (1-2-3) \n>").strip()
            #Si desea buscarlo por Título del libro se leeran los datos de los Títulos de cada libro para encontrar uno que coincida
            if cat=="1":
                file=open(arch,"r")
                autor=""
                coincidencia =False
                a=input("Ingrese el título de la obra: ")
                for i in range(tamaño):
                    cont=0
                    linea=file.readline()
                    for j in range(len(linea)):
                        if linea[j]=="-":
                            cont+=1
                            if cont==1:
                                inicio=j+1
                            if cont==2:
                                final=j
                        if cont==2:
                            autor= linea[inicio:final]
                            break
                    if autor==a:
                        datos.append(linea)
                        coincidencia =True
                if not coincidencia:
                    print("\n---No se encontraron libros publicados con el nombre ingresado.---\n")
                file.close()
            #Si desea buscarlo por Autor se leeran los datos de los Autores para encontrar uno que coincida
            elif cat=="2":
                file=open(arch,"r")
                autor=""
                coincidencia =False
                a=input("Ingrese el autor de la obra: ")
                for i in range(tamaño):
                    cont=0
                    linea=file.readline()
                    for j in range(len(linea)):
                        if linea[j]=="-":
                            cont+=1
                            if cont==2:
                                inicio=j+1
                            if cont==3:
                                final=j
                        if cont==3:
                            autor= linea[inicio:final]
                            break
                    if autor==a:
                        datos.append(linea)
                        coincidencia=True
                if not coincidencia:
                    print("\n---No se encontraron libros publicados con el autor ingresado.---\n")
                file.close()
            #Si desea buscarlo por año de publicación, se leeran los datos de años de publicación para encontrar uno que coincida
            elif cat=="3":
                file=open(arch,"r")
                autor=""
                coincidencia =False
                a=input("Ingrese el año de publicación de la obra: ")
                for i in range(tamaño):
                    cont=0
                    linea=file.readline()
                    for j in range(len(linea)):
                        if linea[j]=="-":
                            cont+=1
                            if cont==3:
                                inicio=j+1
                            if cont==4:
                                final=j
                        if cont==4:
                            autor= linea[inicio:final]
                            break
                    if autor==a:
                        datos.append(linea)
                        coincidencia =True
                if not coincidencia:
                    print("\n---No se encontraron libros publicados en el año ingresado.---\n")
                file.close()

            else:
                print("\n-Opción inválida-\n")
            #Se le mostrará al usuario la información acerca del libro que buscó mediante la función
            for dato in datos:
                partes=dato.split("-")
                if len(partes) >=4:
                    print("\nInformación de libro:")
                    print(f"  Título: {partes[1]}")
                    print(f"  Autor: {partes[2]}")
                    print(f"  Año: {partes[3]}")
            datos = []
            seguir=input("\nDesea buscar otro libro? (S/N): ")
    return print()

#------FUNCIÓN PARA MOSTRAR LISTA DE LIBROS-----#
#Se define una función para mostrar los libros al usuario
def VerLista(uso_externo = False):
    if uso_externo: #Argumento opcional para poder ser utilizada de distinta manera al ser llamada por otras funciones del programa
        try:  
            with open(arch, "r") as file:
                lineas = file.readlines()
        except:
            print("No se ha registrado ninguna acción con el programa, no existe ningún archivo todavía")
        else:
            libros = []
            for linea in lineas:
                partes = linea.split("-")
                if len(partes)>=4:
                    titulo=partes[1].strip()
                    autor=partes[2].strip()
                    año=partes[3].strip()
                    libros.append((titulo, autor, año))         
            if libros:
                print("\nLista de libros como se registraron en el archivo:")
                contador=1
                for libro in libros:
                    print(f"{contador}. Titulo: {libro[0]}, Autor: {libro[1]}, Año: {libro[2]}")
                    contador+=1
                print()
            else:
                print("\nNo hay libros registrados para mostrar.\n")
    #Caso de uso normal de la funcion, cuando se utiliza por su cuenta
    else:
        try:  #Parte para ser a prueba de usuarios para archivo no existente y archivo vacÍo
            with open(arch, "r") as file:
                lineas = file.readlines()
        except:
            print("No se ha registrado ninguna acción con el programa, no existe ningún archivo todavía")
        else:
            print("Categorias de visualización disponibles:")
            print("  1) Ver por Título \n  2) Ver por Autor \n  3) Ver por Registro en Archivo")
            opcion = input("¿Cómo desea ver la lista? (1-2-3) \n>").strip()  #Preguntar por categoría de visualización

            libros = []  #Lista para almacenar los libros
            if opcion == "1":                          #Por título
                for linea in lineas:
                    partes=linea.split("-")
                    if len(partes)>=4:
                        titulo=partes[1].strip()
                        autor=partes[2].strip()
                        año=partes[3].strip()
                        libros.append((titulo, autor, año))

                if libros:
                    libros.sort()  #Ordena los libros por título alfabéticamente
                    print("\nLista de libros por título:")
                    contador=1
                    for libro in libros:
                        print(f"{contador}. Título: {libro[0]}, Autor: {libro[1]}, Año: {libro[2]}")
                        contador+=1
                    print()
                else:
                    print("\nNo hay libros en la biblioteca.\n")

            elif opcion=="2":                          #Por autor
                for linea in lineas:
                    partes = linea.split("-")
                    if len(partes)>=4:
                        titulo=partes[1].strip()
                        autor=partes[2].strip()
                        año=partes[3].strip()
                        libros.append((autor, titulo, año))

                if libros:
                    libros.sort()  #Ordena los libros por autor alfabéticamente
                    print("\nLista de libros por autor:")
                    contador=1
                    for libro in libros:
                        print(f"{contador}. Autor: {libro[0]}, Título: {libro[1]}, Año: {libro[2]}")
                        contador+=1
                    print()
                else:
                    print("\nNo hay libros para mostrar.\n")
            elif opcion == "3":
                for linea in lineas:
                    partes = linea.split("-")
                    if len(partes)>=4:
                        titulo=partes[1].strip()
                        autor=partes[2].strip()
                        año=partes[3].strip()
                        libros.append((titulo, autor, año))
                    
                if libros:
                    print("\nLista de libros como se registraron en el archivo:")
                    contador=1
                    for libro in libros:
                        print(f"{contador}. Título: {libro[0]}, Autor: {libro[1]}, Año: {libro[2]}")
                        contador+=1
                    print()
                else:
                    print("\nNo hay libros registrados para mostrar.\n")
            else:
                print("\nOpción inválida\n")


#------FUNCIÓN PARA ACTUALIZAR LOS LIBROS-----#
#Se define una función que le permite al usuario actualizar los datos de un libro en concreto
def ActualizarDatos():
    hay_libros = True
    try:              #Parte para ser aprueba de usuarios para archivo no existente/archivo vacio
        file = open(arch, "r")
    except:
        print("No se ha registrado ninguna acción con el programa, no existe ningun archivo todavia")
        hay_libros = False
    else:
        libro = file.readline()
        if libro == "":
            print("No se han registrado ningun libro todavía... ")
            hay_libros = False
        file.close()
    good = True       #Parte de variables para realizar la actualizacion de datos
    file = open(arch,"r")
    libros = file.readlines()
    cant_libros = int(len(libros))
    eliminar = ""
    VerLista(True)
    while good and hay_libros:
        try:          #Parte para ser aprueba de usuario por si elige escribir de forma erronea
            cambio_datos = int(input("Ingrese el número del libro al que quiera actualizar... "))     #Elegir el libro que busca actualizar
            if cambio_datos > 0 and cambio_datos <= cant_libros:
                good = False
            else:
                print("El libro que busca actualizar no se encuentra")
        except:
            print("El número del libro no existe/Usted no ha ingresado un valor numerico entero... ")
    good = True
    while good and hay_libros:
        try:          #Parte para ser aprueba de usuario por si elige escribir de forma erronea
            cambio_tipo = int(input("¿Qué desea actualizar?\n1) Titulo\n2) Autor\n3) Año de publicación\n... "))    #Elegir el que quiere actualizar el usuario
            if cambio_tipo > 0 and cambio_tipo <= 3:
                good = False
            else:
                print("No ha ingresado correctamente una de las 3 opciones... ")
        except:
            print("La opción que intenta elegir no existe/Usted no ha ingresado un valor numerico entero... ")

    cambio = libros[cambio_datos-1]
    good = True
    resultado = ""
    if cambio_tipo == 1:        #Para actualizar Titulo del libro seleccionado
        cambio = cambio.split("-")
        inter = str(input("Ingrese el nuevo Titulo: "))
        cambio[1] = inter
        for i in range(len(cambio)):
            if i != len(cambio)-1:
                cambio[i] += "-"
            resultado += cambio[i]
    elif cambio_tipo == 2:      #Para actualizar autor del libro seleccionado
        cambio = cambio.split("-")
        inter = str(input("Ingrese el nuevo Autor: "))
        cambio[2] = inter
        for i in range(len(cambio)):
            if i != len(cambio)-1:
                cambio[i] += "-"
            resultado += cambio[i]
    elif cambio_tipo == 3:      #Para actualizar año de publicación del libro seleccionado
        cambio = cambio.split("-")
        while good:             #Parte de codigo para prueba de usuario, para mal ingreso del año o año de publicacion improbable/imposible
            try:
                inter = int(input("Ingrese el nuevo Año de Publicación: "))
                if inter >= 879 and inter <= 2024:
                    good = False
                else:
                    print("El año de publicación ingresado no es posible")
            except:
                print("Usted no ha ingresado un año de forma numérica... ")
        cambio[3] = str(inter)
        for i in range(len(cambio)):
            if i != len(cambio)-1:
                cambio[i] += "-"
            resultado += cambio[i]
    libros[cambio_datos-1] = resultado
    file.close()
    file = open(arch, "w")
    file.writelines(libros)     #Actualizacion de los datos en el archivo
    file.close()
    print("\n-Datos Actualizados-\n")

#------FUNCIÓN PARA BORRAR LIBROS-----#
#Se define una función para borrar todos los libros registrados en el archivo
def BorrarDatos():
    borrar = input("¿Está seguro que desea borrar todos los datos de la biblioteca?(s/n): ").strip() #Mensaje de confirmación
    if borrar == "S" or borrar == "s":
        with open(arch, "w") as file:
            file.write("")                                                  #Borrar datos usando una cadena vacía
        print("\nTodos los datos han sido borrados de la librería.\n")      #Mensaje de borrado
    else:
        print("\nOperación cancelada.\n")                                   #Si no quiere borrar datos, se cancela

#------FUNCIÓN PARA CARGAR ARCHIVO DE USUARIO-----#
#Se define una función que permitirá al usuario cargar su propio archivo con sus propios libros sin tener que usar el programa con anterioridad
def CargarArchivo():
    bucle_carga = True
    directorio = os.getcwd() #Se usa la funcion .getcwd para conseguir la ruta exacta del programa en el sistema donde se este corriendo
    carga_incorrecta = True
    print("Antes de comenzar a usar el programa deberá decidir si desea empezar una lista de libros nuevo o cargar una existente")
    while bucle_carga:
        print("1. Empezar Lista Nueva \n2. Cargar Lista Existente")
        desea_cargar = input("\n¿Que desea hacer? \n>").strip() #Se le pide al usuario decidir si empezar una lista nueva o cargar una lista creada por el mismo
        if desea_cargar == "1":
            print("Usted ha decidido comenzar una lista de libros nueva") #Al empezar una lista nueva el programa continua con normalidad
            bucle_carga = False
        elif desea_cargar == "2": #Al desear cargar una lista existente se le darán instrucciones detalladas al usuario sobre como cargar este archivo
            print("Usted ha decidido cargar una lista de libros existente")
            print("Para cargar correctamente una lista existente, deberá seguir paso a paso las instrucciones a continuación caso contrario el archivo no podrá ser cargado")
            print("1. Deberá crear un archivo de texto llamado 'bibliografia' sin tildes ni espacios")
            print("2. Dentro de este archivo de texto deberán encontrarse los datos de los libros en el siguiente formato")
            print("-Nombre del libro 1-Nombre del autor 1-Año de publicación 1-\n-Nombre del libro 2-Nombre del autor 2-Año de publicación 2-\netc...")
            print("Los guiones son obligatorios, de otro modo el programa no interpretará los datos correctamente\nRecuerde que cada línea de texto representa un libro")
            print(f"3. Este archivo deberá copiarse en el siguiente directorio:\n{directorio}")
            print("Si ha seguido estas instrucciones correctamente el programa cargará su archivo con los libros registrados")
            #Si las instrucciones han sido seguidas correctamente el usuario podrá cargar el archivo correctamente
            while carga_incorrecta:
              #Para confirmar si el usuario quiere cargar el archivo o abortarla para comenzar con una lsita nueva se le pide decidir con input
                print("1. Cargar el archivo \n2. Abortar la carga de archivo")
                cargar = input("\n¿Qué desea hacer?\n>").strip()
                if cargar == "1": #Si el usuario decide cargar un archivo se comprobará si el archivo ha sido cargado correctamente en el directorio del programa
                    try:
                        with open(arch, "r") as file:
                            lineas = file.readlines()
                            cumple_formato = ComprobarFormato(len(lineas)) #Se usa la función auxiliar ComprobarFormato para comprobar que los libros escritos dentro del archivo estén correctamente formateados
                            if cumple_formato:
                                print("\nArchivo cargado correctamente!\n") #Si el archivo se carga correctamente al programa comenzará normalmente
                                carga_incorrecta = False
                            else: #Caso contrario el usuario decidirá si desea volver a intentar cargar el archivo o simplemente empezar una lista nueva
                                print("\nLos libros cargados en el archivo no tienen el formato correcto\nIntente otra vez\n")
                    except: #Se realiza una excepción si el archivo no se ha cargado correctamente en el directorio del programa
                        print("\nEl Archivo no se ha cargado correctamente según las instrucciones\nIntente otra vez\n")
                elif cargar == "2": #Si el usuario decide abortar la carga de archivo, el programa comenzará normalmente con una lista nueva
                    print("\nSe ha abortado la carga de archivo existente\nSe creará una lista de libros nueva\n")
                    carga_incorrecta = False
                else:
                    print("\nOpción inválida\n")
                bucle_carga = False
        else:
            print("\nOpción inválida\n")

#------FUNCIÓN PARA COMPROBAR QUE EL FORMATO DE ARCHIVO SEA CORRECTO-----#
#Se define una función de apoyo que comprobara el formato de los libros registrados en el archivo de texto que se comprobarán en la función CargarArchivo
def ComprobarFormato(longitud):
    formato = False
    #Con un bucle for la función comprobará línea a línea si los libros contienen una cadena separada por 4 guiones para que el programa pueda leerlos posteriormente
    for i in range(longitud):
        with open(arch, "r") as file:
            linea_actual = file.readline()
            if linea_actual.count("-") != 4:
                formato = False
            else:
                formato = True
    return formato #La Función devolverá un booleano que se usará en la función CargarArchivo para saber si el archivo esta formateado correctamente

#------FUNCIÓN PARA MARCAR UN LIBRO COMO FAVORITO-----#
#Se define una funcion extra que permitira al usuario marcar un libro como favorito y será registrado en un archivo de texto distinto
def AsignarFavoritos():
    file = open(archfav,"a")
    file.write("")
    file.close()
    hay_libros = True
    try:              #Parte para ser aprueba de usuarios para archivo no existente/archivo vacio
        file = open(arch, "r")
    except:
        print("No se ha registrado ninguna acción con el programa, no existe ningun archivo todavia")
        hay_libros = False
    else:
        libro = file.readline()
        if libro == "":
            print("No se han registrado ningun libro todavía... ")
            hay_libros = False
        file.close()
    good = True       #Parte de variables para realizar la asignacion de favoritos
    file = open(arch,"r")
    libros = file.readlines()
    cant_libros = int(len(libros))
    file.close()
    VerLista(True)
    while good and hay_libros:
        try:          #Parte para ser aprueba de usuario por si elige escribir de forma erronea
            asignar_favorito = int(input("Ingrese el número del libro al que quiera marcar como favorito... "))     #Elegir el libro que busca asignar como favorito
            if asignar_favorito > 0 and asignar_favorito <= cant_libros:
                good = False
            else:
                print("El libro que busca marcar como favorito no se encuentra")
        except:
            print("El número del libro no existe/Usted no ha ingresado un valor numerico entero... ")
    file = open(archfav,"r")
    todos_favoritos = file.readlines()
    file.close()
    file = open(archfav,"a") #Se utiliza archfav para registrar los libros favoritos
    #Se comprueba que el libro en cuestion no este ya registrado como favorito
    if todos_favoritos.count(libros[asignar_favorito-1]) == 0: 
        file.write(libros[asignar_favorito-1])
        print("El libro ha sido exitosamente marcado como un libro favorito")
    else:
        print("El libro escogido ya esta marcado como favorito!")
    file.close()

#------FUNCIÓN PARA VER LA LISTA DE LIBROS FAVORITOS-----#
#Se define una función extra que le permitirá al usuario ver su lista de libros favoritos registrada
#Esta función sera bastante similar a la funcion VerLista, pero usando el archfav como archivo para leer    
def VerFavoritos():
    try:  #Parte para ser a prueba de usuarios para archivo no existente y archivo vacÍo
        with open(archfav, "r") as file:
            lineas = file.readlines()
    except:
        print("No se ha registrado ningun libro favorito con el programa, no existe ningún archivo de favoritos todavía")
    else:
        print("Categorias de visualización disponibles:")
        print("  1) Ver por Título \n  2) Ver por Autor \n  3) Ver por Registro en Archivo de Favoritos")
        opcion = input("¿Cómo desea ver la lista? (1-2-3) \n>").strip()  #Preguntar por categoría de visualización

        libros = []  #Lista para almacenar los libros
        if opcion == "1":                          #Por título
            for linea in lineas:
                partes=linea.split("-")
                if len(partes)>=4:
                    titulo=partes[1].strip()
                    autor=partes[2].strip()
                    año=partes[3].strip()
                    libros.append((titulo, autor, año))

            if libros:
                libros.sort()  #Ordena los libros por título alfabéticamente
                print("\nLista de libros favoritos por título:")
                contador=1
                for libro in libros:
                    print(f"{contador}. Título: {libro[0]}, Autor: {libro[1]}, Año: {libro[2]}")
                    contador+=1
                print()
            else:
                print("\nNo hay libros favoritos en la lista de favoritos.\n")

        elif opcion=="2":                          #Por autor
            for linea in lineas:
                partes = linea.split("-")
                if len(partes)>=4:
                    titulo=partes[1].strip()
                    autor=partes[2].strip()
                    año=partes[3].strip()
                    libros.append((autor, titulo, año))

            if libros:
                libros.sort()  #Ordena los libros por autor alfabéticamente
                print("\nLista de libros favoritos por autor:")
                contador=1
                for libro in libros:
                    print(f"{contador}. Autor: {libro[0]}, Título: {libro[1]}, Año: {libro[2]}")
                    contador+=1
                print()
            else:
                print("\nNo hay libros favoritos para mostrar.\n")
        elif opcion == "3":
            for linea in lineas:
                partes = linea.split("-")
                if len(partes)>=4:
                    titulo=partes[1].strip()
                    autor=partes[2].strip()
                    año=partes[3].strip()
                    libros.append((titulo, autor, año))
            if libros:
                print("\nLista de libros favoritos como se registraron en el archivo de favoritos:")
                contador=1
                for libro in libros:
                    print(f"{contador}. Título: {libro[0]}, Autor: {libro[1]}, Año: {libro[2]}")
                    contador+=1
                print()
            else:
                print("\nNo hay libros favoritos registrados para mostrar.\n")
        else:
            print("\nOpción inválida\n")
#------FUNCIÓN PARA BORRAR TODOS LOS LIBROS DE LA LISTA DE FAVORITOS-----#
#Se define una función extra que permitirá al usuario borrar su lista de libros favoritos
#Esta función sera bastante similar a la función BorrarDatos pero usando el archfav como archivo con el texto a eliminar            
def BorrarFavoritos():
    borrar = input("¿Está seguro que desea borrar todos los datos de su lista favorita?(s/n): ").strip() #Mensaje de confirmación
    if borrar == "S" or borrar == "s":
        with open(archfav, "w") as file:
            file.write("")                                                  #Borrar datos usando una cadena vacía
        print("\nTodos los datos han sido borrados de la lista de favoritos.\n")      #Mensaje de borrado
    else:
        print("\nOperación cancelada.\n")                                   #Si no quiere borrar datos, se cancela

#Variables globales
arch="bibliografia.txt" #Archivo que contendrá todos los libros registrados con el programa
archfav = "bibliografia_favorita.txt" #Archivo que contendrá los libros marcados como favoritos por el usuario
opcion="s" #Cadena que contiene las decisiones del usuario en el menu principal

#Programa principal
print(" " + "-"*36)
print(" ¡Bienvenido al Gestor Bibliográfico!")
print(" " + "-"*36)
print()
CargarArchivo()
while opcion!="9":
    #Se crea un menu principal simple y comprensivo para cualquier usuario que llamará a las funciones dependiendo de las decisiones del usuario
    print("-----------------Menú------------------")
    print("1. Agregar Libro \n2. Buscar Libro \n3. Ver Lista de Libros \n4. Guardar/Actualizar Archivo de Datos \n5. Borrar Datos \n6. Marcar un Libro como Favorito \n7. Ver Lista de Libros Favoritos \n8. Borrar Lista de Libros Favoritos \n9. Salir")
    opcion=input("\n¿Qué desea hacer? \n>").strip()
    if opcion=="1":
        AgregarLibro()
    elif opcion=="2":
        datos=BuscarLibro()
        print(datos)
    elif opcion=="3":
        VerLista()
    elif opcion=="4":
        ActualizarDatos()
    elif opcion=="5":
        BorrarDatos()
    elif opcion=="6":
        AsignarFavoritos()
    elif opcion=="7":
        VerFavoritos()
    elif opcion=="8":
        BorrarFavoritos()
    elif opcion=="9":
        print("\nGracias por usar el programa\n")
    else:
        print("\nOpción inválida\n")
