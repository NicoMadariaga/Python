from io import open

#Creamos un archivo
archivo = open('archivo_prueba.txt', 'w')

#Escribimos el archivo
archivo.write('Esta es la primer linea.\n')

#Agregamos varias lineas
lineas = ['Agregamos una linea\n', 'Agregamos dos linea\n', 'Agregamos tres linea\n']
archivo.writelines(lineas)

#Cerramos el archivo
archivo.close()

#Leemos el contenido del archivo.
archivo = open('archivo_prueba.txt', 'r')
texto = archivo.read()
print(texto)
archivo.close()

#Leemos el contenido del archivo y lo asignamos a una lista.
archivo = open('archivo_prueba.txt', 'r')
lista = archivo.readlines()
print(lista)
archivo.close()

#Modificamos un archivo
archivo = open('archivo_prueba.txt', 'a')
archivo.write('Esto es una linea nueva')
archivo.close()

#Modificamos un archivo en una posición especifica
archivo = open('archivo_prueba.txt', 'r+')
archivo.seek(2)
archivo.write('Esto es una linea nueva, en la linea 2')
archivo.close()


