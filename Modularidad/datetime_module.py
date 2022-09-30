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

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print(dt.strftime("%d/%m/%Y"))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))
print(dt.isoformat())

print(type(dt))