##### BOLEANS #####
#Solo pueden almacenar dos valores (True o False)
from ast import Not
from fcntl import F_SEAL_SHRINK
from operator import xor


boolean = True
boolean2 = False

### Operaciones

#AND
result = True and False #False
result = True and True #True
result = False and False #False

#OR
result = True or False #True
result = True or True #True
result = False or False #False

#NOT
result = not True #False
result = not False #True

print(result)