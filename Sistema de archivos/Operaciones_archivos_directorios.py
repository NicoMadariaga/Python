##### OPERACIONES DE ARCHIVOS y DIRECTORIOS #####

from io import open
import shutil #Modulo para la manipulación de archivos (Copiar y Mover)
import os # Para eliminar archivo


### Copiar y Mover Directorios

#Crea una carpeta
os.mkdir("./mi_carpeta") 

# Elimina una carpeta
os.rmdir("./mi_carpeta") 

#Copiar una carpeta
shutil.copytree("./mi_carpeta", "./carpeta_nueva" ) 

#Muestra en una lista el contenido de una Directorio
os.listdir("./mi_carpeta") # ('.' o './' ) Para ver la carpeta actual 

#Retorna la ruta actual desde donde se ejecuta nuestro script
os.getcwd() 

### Copiar y Mover Archivos

#Copia un archivo
shutil.copy("archivo.txt", "./carpeta_nueva/archivo_copiado.txt") 

#Mover un archivo
shutil.move("./carpeta_nueva/archivo_copiado.txt", "./mi_carpeta/archivo_copiado.txt") 

#Eliminar un archivo
os.remove("archivo_copiado.txt") 

#Obtener la dirección donde esta ubicado un archivo
os.path.abspath("archivo.txt")

#Saber si existe un archivo
os.path.isfile("./archivo.txt")#Devuelve True si existe el archivo
os.path.isfile("archivo.txt") #igual, pero sin indicar el directorio

