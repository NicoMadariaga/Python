##### Dictionaries (diccionarios) #####

#Es un tipo de datos, que almacena un conjunto de elementos, pero cada elemento contiene una clave (key) y un valor).
#Son pares encerrados entre llaves, separados por coma. Clave y valor se separan con dos puntos.
#No tiene un orden como las listas.
#Las claves no pueden repetirse.
#Las claves hacen las veces de índice, permitiendo acceder a los valores por medio de corchetes.

#Definición
diccionario = {'Nombre': 'Juan', 'Edad': 29, 'DNI': 31509658}
diccionario2 = dict(Nombre = 'Maria', Edad = 30, dni = 20379548)
 
#Acceso
print(diccionario['Nombre'])
print(diccionario.get('Edad'))
 
#Modificar un elemento, si la clave no existe, crea un nuevo elemento
diccionario['Edad'] = 30

### Iterar Un diccionario

#Iterar por la clave
for x in diccionario:
   print(x)
 
#Iterar por valor
for y in diccionario.values():
   print(y)
 
#Iterar por clave y valor
for x, y in diccionario.items():
   print(x, y)

### Métodos para diccionarios
clave = 'Nombre'
valor = 'Jun'

#Longitud de un diccionario
len(diccionario)
 
#Vaciar un diccionario
diccionario.clear()
 
#Corroborar si una clave o un valor están dentro de un diccionario
clave in diccionario
valor in diccionario.values()
 
#Consultar el valor para una clave
diccionario.get(clave)
diccionario.get(clave, 'El valor no es encontrado') #Nos permite declarar un valor por si la clave no se encuentra
 
#Agregar elementos
diccionario.update({'clave', 'valor'})
 
#Eliminar un elemento
del diccionario[clave]
diccionario.pop(clave)
 
#Obtener todas las claves
diccionario.keys()
 
#Obtener todos los valores
diccionario.values()

### Diccionarios anidados
anidados = {'anidado1': diccionario, 'anidado2': diccionario2}
