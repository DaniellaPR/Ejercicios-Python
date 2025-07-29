#-*-coding:cp1252-*-
#Ejercicio 2


#Definimos las variables
condicion=0
l=[]
a=1
media=0
desv=0

while condicion!="":
    condicion=input(f"Ingrese dato {a}: ")
    if condicion!="":        
        l.append(float(condicion))
    a+=1    

#Encontramos la media
for i in range(len(l)) :
    media+=l[i]
media/=len(l)    

#Encontramos el cuadrado de la desviacion estandar
for i in range(len(l)):
    desv+=(l[i]-media)*(l[i]-media)
desv/=len(l)-1

#Encontramos la raiz de la desviación estandar hasta con 2 decimales

#Establecemos variables para poder encontrar la raiz 

cercania=2                          #Cercania es la variable que usaremos para repetir el proceso de encontrar, hasta 2 decimales (de ser posible)
contador=0
impar=1
comparar=0                           #Variable que usaremos para encontrar el valor mas proximo a la raiz
desv2=desv                  

while impar<=desv2:                  #Nos aproximamos lo maximo posible a la raiz (si fuera una raiz exacta por ejemplo 9, en contador se almacena el 3)
    desv2-=impar                     #El metodo para encontrar la raiz esta basado en acercarse a la raiz mediante la resta sucesiva de numeros impares
    impar+=2
    contador+=1

if desv2>0:                          #Si el valor en desv es 0 entonces significara que la raiz era exacta
    cercania=0                      
    

while cercania<2:          
    for i in range(0,10):           #Probamos uno a uno los valores posibles de las decimas para verificar cual es el valor mas proximo, tiene que ser mas cercano por la centesima superior e inferior
        for j in range(0,10):
            if j==0 and i==0:       
                anterior=contador+ i/10 + j/100
                c1=desv-((anterior)*(anterior))
                cercania+=1
            else:
                
                actual=contador+ i/10 + j/100
                c2=desv-((actual)*(actual))
                if c2<0:
                    c2=(-1)*c2
                
                if c2<c1:   
                    anterior=actual            #Se actualiza el valor para comparar en caso de que el actual este mas cerca que el valor anterior
                    c1=c2
                    cercania=0                 #Se reinicia el contador
                    cercania+=1
                if c1<c2:
                    cercania+=1
            if cercania>=2:         #Establecemos condiciones para que salga del bucle en caso de encontrar el valor centecimal mas proximo
                break
        if cercania>=2:         
            break
    
#Imprimimos los resultados    
    
print("La media de los números ingresados es:",media)
print("La desviación típica (estándar) es:",anterior)      
