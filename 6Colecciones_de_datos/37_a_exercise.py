"""
Colecciones de datos (Enunciados)
"""

def ex1():

	print ("""	1) Realiza un programa que siga las siguientes instrucciones:

	Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
	Crea un conjunto llamado administradores con los administradores Juan y Marta.
	Borra al administrador Juan del conjunto de administradores.
	Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
	Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.

	Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista. 
	También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento.
	
	""")
	print ("---")
	print ()
	print (" Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos:")
	usuarios = set()
	usuarios = {"Marta","David","Elvira","Juan","Marcos"}
	print ("usuarios	:	", usuarios)
	print ()
#	lista_usuarios = ["Marta", "David", "Elvira", "Juan", "Marcos"]	# Crear lista y convertirla a conjunto
#	usuar = set (list( lista_usuarios ) )
#	print ("usuar", usuar)
	print ()
	print (" Crea un conjunto llamado administradores con los administradores Juan y Marta:")
	administradores = {"Juan","Marta"}
	print ("Administradores :	", administradores)
	print ()
	print (" Borra al administrador Juan del conjunto de administradores:")
	administradores.discard("Juan")
	print ("Administradores :	", administradores)

#	lista_admin = list (set (administradores))
#	for admin in lista_admin:
#		if (admin != "Juan"):
#			administradores = set ( list(lista_admin) )
#			print (administradores)

	print ()


	print (" Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios:")
	if ('Marcos' not in administradores):
		administradores.add('Marcos')
	print ("Administradores :	", administradores)
	print ("usuarios	:	", usuarios)
	
	print ()
	print ("Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no:")
	print ( )
	for users in usuarios:
		if (users in administradores):
			print (users,"		es un administrador")
		else:
			print (users,"		es un usuario")
	print ()
	print ("---")
	print ()

ex1()






