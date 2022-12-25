#***NUMEROS PRIMOS***
'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def primo(numero):
    if numero == 0 or numero == 1:
        return False
    else:
        esprimo = True
        for i in range (2, numero):#Cheuqeuo si el numero es divisible por algun otro número
            if (numero%i) == 0:
                esprimo = False
                break
        return esprimo

###Main
try:
    #Corroboro si el numero ingresado es primo
    numero = int (input ("ingrese un numero mayor a 1: "))
    if primo(numero):
        print(f'El número {numero}, es primo')
    else:
        print(f'El número {numero}, No es primo')

    #imprimimos los números primos del 1 100
    print('Los números primos del 1 al 100 son:')
    lista_primos = []
    for i in range(2, 100):
        if primo(i):
            lista_primos.append(i)

    print(lista_primos)

except:
    print('Debes ingresar un número')

