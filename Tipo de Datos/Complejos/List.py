##### LIST ####
"""
Se trata de conjuntos ordenados de elementos, encerrados por corchetes y separados por comas. 
El orden comienza con el índice 0 para el primer lugar de la Lista. 
Pueden agruparse valores de distintos tipos de datos, y es posible agregar, eliminar o modificar elementos de las listas en cualquier momento 
(decimos que las Listas son mutables en Python)
"""

#Definición de lista
lista = [10, 'Juan', True]

#Obtener elementos de una lista
elemento = lista[1] #'Juan'
elemento2 = lista[0:2] #[10, 'Juan']

#Modificar una lista
lista[1] = 'Jesús' #[10, 'Jesús', True]


###Listas Multidimensionales (o listas concatenadas).
#En Python, como en otros lenguajes, podemos almacenar listas dentro de otras listas (Listas anidadas)
listaAnidada = [[1, 2, 3], [4, 5, 6]]
print(listaAnidada) #[[1, 2, 3], [4, 5, 6]]
print(listaAnidada[1]) #[4, 5, 6]
print(listaAnidada[1][1]) #5

### Metodos
#Obtener la cantidad de elementos de una lista
len(lista) #3
 
#Agregar un elemento al final de la lista.
lista.append(40) #[10, 'Juan', True, 40]
 
#Insertar un elemento en el índice especificado, corriendo los elementos siguientes un índice más
lista.insert(1, "Te Ama") #[10, "Te Ama", 'Juan', True, 40]
 
#Indica la posición donde se encuentra un elemento
lista.index(10) #0
 
#Eliminar un elemento en un índice dado
lista.pop(4) #[10, "Te Ama", 'Juan', True]
 
#Elimina un elemento pasado como parámetro. Si hay varios elemento iguales, elimina el primero encontrado
lista.remove(10)#["Te Ama", 'Juan', True]
 
 
#Ordena los elementos de la lista de menor a mayor, los elementos deben ser del mismo tipo
lista.sort()
 
#Invertir los elementos de una lista
lista.reverse()
 
#Buscar un elemento en una lista
10 in lista
 
#Contar cuantas veces aparece un elemento en una lista
lista.count(10)
 
#Agregar todos los elementos de una lista al final
lista.extend(lista2)

#Comparar si dos listas son iguales (misma longitud, mismos elementos y mismo orden)
lista == lista2
