##### ARCHIVOS #####

# El objetivo es la persistencia de datos.
# Fase necesaria para la manipulación de un archivo: Creación - Apertura - Manipulación - Cierre
# Debemos utilizar el módulo io.

from io import open

#Crear/Abrir un archivo
archivo_texto = open("archivo.txt","w") #abre un archivo (archivo.txt), y si no existe lo crea, en el directorio donde estamos ejecutando la aplicación. 
#Modos de abrir un archivo:
# "w" en modo escritura.
# "r" en modo lectura.
# "r+" en modo lecto escritura.
# "a" en modo append (agregar)
# Nota: siempre que creemos o modifique mmos un archivo, debemos abrirlo primero y luego cerrarlo.

#Escribimos el archivo
texto = "Hola Mundo"
archivo_texto.write(texto) 
lista = ["linea 1", "linea2"]
archivo_texto.writelines(lista) #Toma como parámetro una lista de String y lo escribe en el archivo, 
#un elemento al lado del otro, salvo que tenga un salto de linea.

#Cerramos el archivo en memoria
archivo_texto.close() 

### Lectura de un archivo

#Abrimos el archivo en modo lectura 
archivo_texto = open("archivo.txt","r") #Al abrirlo en modo solo lectura, no podremos escribirlo
texto = archivo_texto.read() #Leemos el contenido y lo asignamos a una variable
texto = archivo_texto.readline() #Lee solo la linea en la que estamos posicionado
texto = archivo_texto.readlines() #Crea una lista, con un elemento por linea del texto
print(texto)
archivo_texto.close()
#Nota: el puntero queda apuntando al ultimo caracter, por lo que si volvemos a hacer la lectura, obtendremos un texto vacío.

# Leer un archivo por lineas
linea_texto = archivo_texto.readlines() #Nos almacena en una lista el texto separado por líneas
print(linea_texto)


### Modificar un archivo
archivo_texto = open("archivo.txt","a")#abre un archivo en modo append (agregar)
texto = "\nAgregamos otro texto"
archivo_texto.write(texto) #Escribimos el archivo. Lo agrega a la ultima linea.
archivo_texto.close() #Cerramos el archivo en memoria

### Posicionar el puntero
archivo_texto.seek(5) #Posiciona el puntero(cursor) en la posición 5 dentro del texto
texto = archivo_texto.read(5) # Lee el texto hasta la posición 5.


   

