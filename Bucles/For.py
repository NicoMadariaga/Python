##### FOR #####
'''
El bucle for, a diferencia del while es que ya se sabe la cantidad de iteraciones de antemano, 
esto se debe a que en el for no existe una condición a evaluar, 
sino un iterable que define las veces que se ejecutará el código.

Los iterables son aquellos objetos que como su nombre indica pueden ser iterados, lo que dicho de otra forma es, que puedan ser indexados. Ejemplos de estos son las cadenas, listas, diccionarios, tuplas, etc.
Los iteradores (variables) son objetos que hacen referencia a un elemento, y que tienen un método next que permite hacer referencia al siguiente.
'''

for x in 'Python':
   print(x)

### Range
'''
El range() genera una secuencia de números que van desde 0 por defecto hasta el número que se pasa como parámetro.
range(inicio, fin)
Se pueden pasar hasta tres parámetros separados por coma, donde el primer es el inicio de la secuencia, el segundo el final y el tercero el salto que se desea entre números.
range(inicio, fin, salto)
'''

for n in range(0,5):
    print(n) #0 1 2 3 4


### For anidados
lista = [[56, 34, 1],
        [12, 4, 5],
        [9, 4, 3]]
       
for i in lista:
   for j in i:
       print(j)
