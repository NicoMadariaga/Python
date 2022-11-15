##### MANEJO DE ERRORES Y EXEPCIONES #####
# Se utilizan para manejar errores en partes de código en donde son susceptibles a estos.
# Las excepciones son errores en tiempo de ejecución. 


### try y except 
#try: se coloca código que esperamos que pueda lanzar algún error.
#except: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, 
# se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
#Se pueden ejecutar tantos except como sea necesario.

try:# Codigo que queremos controlar
    a = int(input( 'Ingrese un numero: '))
except: #Acción que se ejecuta si hay un error en el bloque try
    print('Te dije que ingreses un Numero')

### Else
# El else se ejecuta si en el try no hubo error

try:# Codigo que queremos controlar
    a = int(input( 'Ingrese un numero: '))
except: #Acción que se ejecuta si hay un error en el bloque try
    print('Te dije que ingreses un Numero')
else:
    print('Ingresaste el numero correcto crack')


### Finally
#Este bloque se ejecuta siempre, indistintamente si en el try hubo un error o no.

try:
    a = int(input( 'Ingrese un numero: '))
except: 
    print('Te dije que ingreses un Numero')
else:
    print('Ingresaste el numero correcto crack')
finally:
    print('El programa finalizo')


###Captura de exepciones por tipo
#Se utiliza para capturar errores específicos
#El exept se ejecuta solo si el error es del tipo que le declaramos

try:
    a = int(input( 'Ingrese un numero: '))
except TypeError: #No se ejecuta este coódigo
    print('Error del tipo TypeError')
except ValueError: 
    print('Error del tipo ValueError')


#Captura de la información del error
try:
    a = int(input( 'Ingrese un numero: '))
except ValueError as error: #error es la variable que almacena la info del error
    print(error)

#Exceptions: es para capturar cualquier tipo de error
try:
    a = int(input( 'Ingrese un numero: '))
except Exception as error: 
    print(error)

