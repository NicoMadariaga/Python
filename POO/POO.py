##### Programación Orientada a Objetos #####
'''
Fundamentos:

Clases:
una clase es una entidad que define una serie de elementos que determinan un estado (datos) y 
un comportamiento (operaciones sobre los datos que modifican su estado).

Objeto: 
Es una instancia de esa clase

Atributos/Propiedades:
Son las características de las clases(variables)
Visibilidad de atributos:
    • Los atributos dentro de una clase, pueden ser públicos o privados.
    • Por defecto están como públicos.
    • Públicos: Se pueden ver tanto dentro como fuera de la clase.
    • Privados: Solo son accesibles, desde dentro de la clase.

Métodos (Funciones):
Son las acciones que pueden realizar los objetos

Abstracción:
Utilizar un objeto, sin tener la necesidad de conocer la funcionalidad interna de ese objeto

Herencia:
Una clase puede heredar de otra clase principal, las cuales tb heredan sus atributos y métodos.

Modularidad:
Dividir el programa en partes más pequeñas.

Encapsulación:
La modificación de las clases, por lo general se deben realizar dentro de las mismas.
'''

### Clases
#Definir una clase
#Los nombres de las clsaes se definen con la primer letra en mayuscula y camelcasse

class MyClass():
    #Atributos
    atributo = "Esto es un atributo"

    def function():#Se puede tener una función como atributo
        return "Esto es una función"

###Objeto (Instancia de una clase)
# En este caso instanciamos una clsae (vacía) y la asignamos variable
clase = MyClass()

#Referenciasa los atributos
print(clase.atributo)

#Instanciar una clase con un estado inicial
#Para esto se define una metodo (constructor) especial __init__
# Self es para poder acceder a todo lo que esta en la misma clase

class Person():
    typee = 'Persona'
    __atributo_privado = "Soy privado" #Atributo privado
    #Constructor de la clase
    def __init__(self, name, surname, age, alias = 'Alias'):#atributo con valor por defecto
        self.name = name
        self.surname = surname
        self.age = age
        self.full_name = f'Nombre: {name}, Apellido: {surname}, Alias:{alias}'
    
    def turn_years (self):
        self.age += 1
        return (self.age)

    def caminando(self):
        print(f'{self.name} esta caminando')

    def get_atributo(self):#Metodo para acceder a un atributo privado
        return self.__atributo_privado 

p = Person('Juan', 'Perez', 38)

print(f'Tipo: {Person.typee}, Nombre: {p.name}, Apellido: {p.surname}, Edad: {p.age}' )
p.turn_years()
print(p.age)
print(p.caminando())
print(p.get_atributo())

###Herencia
class Employee(Person):
    position = 'position'

e = Employee('Jorge', 'Aimar', 38, 'Pepe')
print(e.full_name)
print(e.position)
e.position = 'JEFE'
print(e.position)
