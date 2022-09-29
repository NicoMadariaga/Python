##### STRING #####
#Estos datos son textos (cadena de caracteres), y se representan con comillas dobles (“”) o comillas simples (‘’).
cadena = "Hola Mundo"

#Cadena de dos o mas lineas
cadena2 = """Este es un texto
de mas de una lina"""


###Operadores de cadenas

#Concatenar
cadena = 'Hola'+' '+'mundo.'#Hola mundo.
 
#Multiplicar
cadena = 'Hola' * 3 #HolaHolaHola

#Añadir
cadena = 'Hola' #Hola
cadena += ' ' #Hola 
cadena += 'mundo' #Hola mundo


###Métodos

#Cantidad de caracteres de una cadena
len(cadena)
 
#Devuelve el índice(Comienza desde 0) desde el cual comienza una subcadena dentro de una cadena.
#Si la subcadena no está presente la función devuelve -1
cadena.find("Mundo")

#Obtener la posición de la última aparición de una subcadena
cadena.rfind('Mundo')

#Convertir todos los caracteres a minúscula
cadena.lower()
 
#Convertir todos los caracteres a mayúsculas
cadena.upper()
 
#Convierte el primer carácter de cada palabra en Mayúscula.
cadena.title()
 
#Eliminar los espacios en blanco al principio y al final de una cadena
cadena.strip()
 
#Reemplazar una subcadena dentro de una cadena
cadena.replace('mundo', 'world')
 
#Corta una subcadena
cadena2 = cadena[5:10] # Subcadena desde el indice 5 al 9
cadena2 = cadena[:10] #Comienza desde el indice 0
cadena2 = cadena[5:] #Termina en el final
cadena2 = cadena[5:10:2] #devuelve los caracteres desde el indice 5 al 9, saltando de 2 en 2.
 
#Cuenta la cantidad de apariciones de una subcadena dentro de una cadena
cadena.count('Mundo')
 
#Saber si una cadena se encuentra dentro de otra
cadena2 in cadena
 
#Convertir una cadena a un tipo de dato entero
int(cadena)
 
#Imprimir los datos de una variable dentro de un texto
print(f"En la variable está {cadena2}")


