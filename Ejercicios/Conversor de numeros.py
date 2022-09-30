#Conversor de numeros

#Convertir un numero decimal a binario
def decimal_binario(decimal):
    binario = ''

    if decimal == 0:
        binario = 0
    else:
        while decimal >= 1:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2

    return (binario)

#Función que convierte un numero binario en decimal 
def binario_decimal(binario):
    posicion = len(binario)-1
    decimal = 0
    for x in binario:
        decimal += int(x) * (2 ** posicion)
        posicion -= 1
    return(decimal)

#Main
decimal = int(input('Ingrese un nuemro desimal: '))
print(decimal_binario(decimal))

binario = input('Ingrese un numero binario: ')
print(binario_decimal(binario))
'''
tabla_hexa = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

while len(binario) != 0:
    if len(bianrio >= 4):
        cuatrprimeros = binario
        hexadecimal = 
'''