##### Sets (Conjuntos) #####
'''
Es un tipo de datos, que almacena un conjunto de elementos, pero que no tiene ni índice ni orden.
Se define encerrando los datos entre corchetes, y separándolos con coma.
Para acceder a los elementos, debemos recorrer todo el conjunto con un for.
'''

#Definición
conjunto = {1, 2, 3}
conjunto2 = {'Jesus', 'Te Ama', 5}


###Métodos para conjuntos

#Para saber si un elemento está dentro de un conjunto
1 in conjunto
 
#Agregar elementos
conjunto.add('Jesus') #Agrega de a un elemento
conjunto.update(['te ', 'ama']) #Agregar Varios elementos
 
#Eliminar elementos
conjunto.remove('Jesús')#Si el elemento no se encuentra, tira error
conjunto.discard(1) #Si el elemento no se encuentra, no tira error
conjunto.clear() #Elimina todo los elementos del conjunto
del conjunto #Elimina al conjunto
 
#Unión entre dos conjuntos
conjunto3 = conjunto.union(conjunto2)
conjunto.update(conjunto2)#Otra opción es agregando los elementos de un conjunto a otro
 
#Intersección
conjunto3 = conjunto.intersection(conjunto2)

#Diferencia
conjunto.difference(conjunto2) #Entrega un set conteniendo los miembros diferentes entre dos o más sets
conjunto.difference_update(conjunto2) #Remueve los elementos en este set que también se incluyen en otro set específico
conjunto.intersec_update(conjunto2) #Remueve los elementos en este set que no se encuentran presentes en otro set específico.
conjunto.isdisjoint(conjunto2) #Entrega si dos sets tienen una intersección o no
conjunto.issubset(conjunto2) #Entrega si otro set contiene este set o no
conjunto.issuperset(conjunto2) #Entrega si este set contiene otro set o no
conjunto.pop(1) #Remueve un elemento específico
conjunto.symmetric_difference(conjunto2) #Entrega un set con la diferencia simétrica de dos sets