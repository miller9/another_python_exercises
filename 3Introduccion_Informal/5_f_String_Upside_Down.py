#	6) Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un 	#	alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?:

#	"'Nombre Apellido' ha sacado un 'Nota' de nota"
#	(Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1])


def string_upside_down():
	string_1 = "zeréP nauJ,01"
	print ("The string starts like this: "+string_1)	
	string_2 = string_1[::-1]
	print ("---")
	print ("The right string is: "+string_2)
	print ("---")
	print ( string_2[3:], "ha sacado un ", string_2[:2], " de nota." )
	print ("---")

string_upside_down()









