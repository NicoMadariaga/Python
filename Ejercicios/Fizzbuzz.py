#Escribe un programa que muestre los numeros del 1 al 100, sustituyendo los múltiplos de 3 por la palabra 'Fizz',
#los multiplos de 5 por la palabra 'Buzz',
# y los multiplos de ambos (3 y 5) por la palabra 'FizzBuzz'.

for i in range(0,101):
    if (i % 15) == 0:
        print('FizzBuzz')
    elif (i % 3) == 0:
        print('Fizz')
    elif (i % 5) == 0:
        print('Buzz')
    else:
        print(i)