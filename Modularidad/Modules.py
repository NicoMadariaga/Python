##### Módulos #####
#Es código ya hecho para reutilizar y organizar (Modularización y reutilización).
#Son como las librerías en otros programas.
#Se pueden utilizar los que tiene Python por defecto, y crear los nuestros propios, o utilizar los de otros usuarios.

'''
Idealmente un módulo debe poder cumplir las condiciones de caja negra, es decir, 
ser independiente del resto de los módulos y comunicarse con ellos (con todos o sólo con una parte) 
a través de entradas y salidas bien definidas. 
'''
'''
Crear un módulo:
Crear un archivo dentro del proyecto, con el nombre del módulo.
Dentro, colocamos las funciones, clases y todo el código que necesitemos 
(sus variables, clases e incluso otros módulos).
'''
### Para utilizar un modulo
from datetime import datetime # Del paquete datetime, importamos el modulo datetime
from math import sqrt # importar una función de un módulo.

#Para utilizar una función de un modulo
dia = datetime.now()
print(dia.day) #Utilizamos una función del modulo.