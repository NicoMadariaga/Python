##### WHILE #####
'''
El uso del while nos permite ejecutar una bloque de código repetidas veces, mientras una condición determinada se cumpla. 
Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal.
Llamaremos iteración a una ejecución completa del bloque de código.
Por lo tanto no se sabe de antemano cuántas iteraciones va a haber ( a diferencia del for)
'''

x = 5
while x != 0:
   print(x) #5 4 3 2 1 
   x -= 1
 
#También se puede escribir
while x != 0: print(x); x -= 1

### Else y while
#La sección de código que se encuentra dentro del else, se ejecutará cuando el bucle termine, 
# pero solo si lo hace porque la condición se deja de cumplir, y no porque se ha hecho uso del break.
x = 5
while x != 0:
   print(x)
   x -= 1
else:
   print('El bucle finalizó')   


#While anidados
i = 0
j = 0
while i < 3:
   while j < 3:
       print(i,j)
       j += 1
   i += 1
   j = 0
