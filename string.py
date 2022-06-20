#Cadena de caracteres
cadena = 'Hola Mundo' #Tambien se puede escribir con ""
cadena2 = """Hola Mundo 
con salto de linea"""
print(cadena)
print(cadena2)

#Operadores con cadenas

#Concatenar
cadena = 'Hola '
cadena2 = 'Mundo Concatenado'
print(cadena + cadena2)

#Multiplicar
print(cadena * 3)

#Añadir
cadena += 'mundo añadido'
print(cadena)

#Metodos para cadenas

print(len(cadena)) #Longitud de una cadena
print(cadena.find('mundo')) #Indica en el índice que se encuentra una subcadena dentro de una cadena. Si la subcadena no está presente la función devuelve -1
print(cadena.lower()) #Convertir todos los caracteres a minúscula
print(cadena.title()) #Convierte el primer carácter de cada palabra en Mayúscula.
cadena.strip() #Eliminar los espacios en blanco al principio y al final de una cadena
print(cadena.replace('añadido', 'reemplazado')) #Reemplazar una subcadena dentro de una cadena

#Corta una subcadena
cadena2 = cadena[5:10] # Subcadena desde el indice 5 al 9
cadena2 = cadena[:10] #Comienza desde el indice 0
cadena2 = cadena[5:] #Termina en el final
cadena2 = cadena[5:10:2] #devuelve los caracteres desde el indice 5 al 9, saltando de 2 en 2.

cadena.count('mundo')#Cuenta la cantidad de apariciones de una subcadena dentro de una cadena
cadena.find('mundo') #Obtener la posición donde comienzo de una subcadena
cadena.rfind('mundo') #Obtener la posición de la última aparición de una subcadena
cadena in cadena2 #Es para saber si una cadena se encuentra dentro de otra.
int(cadena) #Convertir una cadena a un tipo de dato entero
