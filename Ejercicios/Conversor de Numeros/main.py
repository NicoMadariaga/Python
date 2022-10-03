#Programa principal para el conversor de numeros
from conversor_numeros import *

##### MENU #####
print("1 - Convertir un N° decima a binario.")
print("2 - Convertir un N° binario a decimal.")

opcion = int(input('Ingrese la opción del menú: '))

if opcion == 1:
    decimal = int(input('Ingrese un nuemro desimal: '))
    result = decimal_binario(decimal)
elif opcion == 2:
    binario = input('Ingrese un nuemro binario: ')
    result = binario_decimal(binario)

print(result)