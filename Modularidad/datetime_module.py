#En este ejemplo importamos el módulo de Python para el manejo de fechas
from datetime import datetime

dt = datetime.now()    # Fecha y hora actual

print(dt)
print(dt.year)         # año
print(dt.month)        # mes
print(dt.day)          # día

print(dt.hour)         # hora
print(dt.minute)       # minutos
print(dt.second)       # segundos
print(dt.microsecond)  # microsegundos

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second)) #hour:minute:second
print(dt.strftime("%d/%m/%Y"))#day/month/year
print("{}/{}/{}".format(dt.day, dt.month, dt.year)) #day/month/year
print(dt.isoformat()) #2022-12-17T11:07:54.945615

print(type(dt)) #<class 'datetime.datetime'>

print(dt.timestamp()) #segundos transcurridos desde el primero de enero de 1970 a las 0 horas UTC hasta el momento a representar.


###Utilizamos el modulo time###
from datetime import time

current_tame = time( 12, 25, 0)

print(current_tame.hour)
print(current_tame.minute)
print(current_tame.second)


###Utilizamos el modulo date###
from datetime import date

current_date = date(2022, 12, 17)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date.today()#La fecha de hoy
print(current_date.year)
print(current_date.month)
print(current_date.day)

#Operaciones
current_date = date(current_date.year, current_date.month, current_date.day+1)
print(current_date.year, current_date.month, current_date.day)
