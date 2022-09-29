##### Functions – f(x) #####
# Una función es un módulo de código que realizan una tarea específica. Encapsulan una tarea y se reutilizan.
# Pueden o  no retornar un valor
# Permite dividir un problema
# Permite probar parte de un programa de forma individual.

#Partes de una Funcion:
'''
def: (palabra clave para definir una función)
Nombre:
Parámetros:(ninguno o mas – cantidad ilimitada)
Cuerpo: (bloque de código)
Valor de retorno (ninguno o uno)

def nombre (parámetro1, parámetro2,..):
    #cuerpo de la función
    return #valor del retorno
'''
from tkinter.tix import INTEGER


def suma (a,b):
    resultado = a + b
    return resultado

#Por fuera de la función: llamado o invocación (para q la función se ejecute) 
'''
Nombre (“identificador”)
- Solo puede contener letras, dígitos numéricos o guión bajo
- No pueden empezar con un número
- No puede ser igual a alguna palabra reservada en el lenguaje.
- Representativo de lo que hace la función.

Cuerpo de función:
- Bloque de código como cualquier otro (se pueden crear variables).
- Si incluye variables locales, su ámbito se restringe a la función.
- Los parámetros se pueden usar como variables dentro de la función. Si su valor cambia, no se modifica fuera de la función.

Valor de retorno (return):
- Es el resultado de la operación que realiza la función.
- Puede ser cualquier tipo de dato.
- Puede no estar, si la función no necesita retornar nada.
- Si la función retorna algo, solo puede retornar una cosa por vez.
- Donde aparece la instrucción return, la función corta su ejecución.

Como crear una función.
- Dentro del mismo archivo donde esta el programa.
- En un archivo diferente y luego importarlo desde el programa: from archivo import * (*Indica que se llaman a todas las funciones del archivo, se puede declara solo las que se vayan a usar.

- Definir exactamente qué operación realizara (Nombre adecuado)
- Definir que datos necesitará al llamarla (parámetros)
- Definir si hay un valor de retorno y cual será.
- Crear el algoritmo que realizara la tarea.
- Colocar el valor de retorno (return).
'''

'''
Función Lambda 
Son funciones simples de un solo código, que no requieren definición.

Ej:
nombre_funcion = lambda parámetro: #codigo de la función.
'''

'''
Variables Locales y Globales.
- Locales: son las que están definidas dentro de la función, y solo pueden ser utilizadas por esta.
- Globales: están definidas fuera de la función, y están disponibles dentro y fuera de estas.

Una variable local podemos convertirla para poder utilizarla de forma global Ej:
    global variable
    variable = # línea de código
'''

###Funciones predefinidas de Python.
#Algunos ejemplos:
variable = 10
isinstance (variable, int)# Nos indica si esa variable es del tipo que le pasamos por parámetro.
type(variable) # Nos indica el tipo de dato de la variable.
del (variable) # Elimina una variable.

#Nota: inpu(). Split() = toma multiples entradas de datos en una misma línea, por ejemplo si el usuario ingresa: 10 20 25, toma los números separados por el espacio
X, y, z = int(input().split()

map() aplica una función a cada elemento de un iterable(lista, tupla, diccionario)
	map(función, iterable)
