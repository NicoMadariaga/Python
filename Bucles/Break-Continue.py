##### BREAK - CONTINUE ##### 
#Se utilizan tanto en el while como en el for.

# Break 
#La Sentencia break, permite cortar el ciclo de repetición antes de que se cumpla la condición. 
# En caso de que el break esté dentro de un bucle anidado, este termina el bucle interno donde se encuentra, no el externo.
i = 0	
while i != 8:
	print(i) #0 1 2 3
	i += 1
	if i == 4:
		break

		
#Nota: while true: se utiliza cuando queremos que en la iteración se ejecute continuamente, hasta que aparezca un break.


#Continue
# La sentencia continue hace que se salte el resto del bloque hasta finalizar la iteración,y en caso de que se cumpla la condición pasa a la siguiente iteración. 
i = 0
while i <= 5:
	print(i)
	i += 1
	continue
	i += 1 #No se ejecuta nunca
