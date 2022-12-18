### ¿Es un Anagrama? ###
'''
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
'''

def anagrama (palabra1, palabra2):
    #convertimos las dos palabras en minusculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Si son iguales o tienen distinto tamaño, no es un anagrama.
    if (palabra1 == palabra2) or (len(palabra1) != len(palabra2)):
        return False
    else:
        #Convertimos los string en listas ordenadas para luego compararlas
        palabra1 = sorted(palabra1)
        palabra2 = sorted(palabra2)
        if palabra1 == palabra2:
            return True
        else:
            return False

p1 = 'perro'
p2 = 'orrepo'

print(anagrama(p1, p2))

