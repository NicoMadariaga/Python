##### IF #####
'''
Los condicionales son estructuras de control que nos permiten controlar si un bloque de código se ejecuta si y solo si se dan unas condiciones en particular.
Nota: cabe destacar que un bloque de código en python se delimita por sangrías(4 espacios o un tab).
'''

### if
edad = 18
if edad >= 18:
    print("Es mayor de edad")


### if else
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


### elife
if edad > 18:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")
else: #edad = 18
    print("No sabe, No contesta")


###Operador ternario

#Existen tres partes en un operador ternario, que son exactamente iguales a los que había en un if else. 
# Tenemos la condición a evaluar, el código que se ejecuta si se cumple, y el código que se ejecuta si no se cumple. 
# En este caso, tenemos los tres en la misma línea.

# [código si se cumple] if [condición] else [código si no se cumple]
print("Es mayor de edad" if edad >= 18 else "Es menor de edad")

