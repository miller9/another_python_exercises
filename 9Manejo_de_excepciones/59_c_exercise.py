print ("""
	3) Localiza el error en el siguiente bloque de código. 
	Crea una excepción para evitar que el programa se bloquee
	y además explica en un mensaje al usuario la causa y/o solución:

	colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
	colores['blanco']
	--> El programa no tiene una clave 'blanco', por ello se bloquea
	--> Error que lanza = KeyError: 'blanco'
	""")

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
	x=input("\nIngrese el color que quiere buscar: ")
	if x in colores:
		print ("\nEl color que buscas pertenece al diccionario!: ")
except KeyError:
	if x not in colores:
		print ("\nKeyError --> En el diccionario NO hay clave ",x," Por favor ingrese una clave válida:")
		print ("Claves válidas: 'rojo', 'verde', 'negro'.")

"""
try:										# otra forma
	colores['blanco']
except KeyError:
	print ("La clave ingresada no está en el diccionario.")
"""

print ()
print ()