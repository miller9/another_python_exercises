def pilas_colas():

	print ("---")
	print ("""	Las pilas

	Son colecciones de elementos ordenados que únicamente permiten dos acciones:

		Añadir un elemento a la pila
		Sacar un elemento de la pila

	La peculiaridad es que el último elemento en entrar es el primero en salir. 
	En inglés se conocen como estructuras LIFO (Last In First Out).
	Las podemos crear como listas normales y añadir elementos al final con el append():
	
	""")
	print ("pila = [3,4,5]")
	pila = [3,4,5]
	print ("pila			:	", pila)
	pila.append(6)
	print ("pila.append(6)		:	", pila)
	pila.append(7)
	print ("pila.append(7)		:	", pila)
	print ()
	print ("""	Para sacar los elementos utilizaremos el método .pop():

	Al utilizar pop() devolveremos el último elemento, pero también lo borraremos. 
	Si queremos trabajar con él deberíamos asignarlo a una variable o lo perderemos:
		
	""")
	print ("pila			:	", pila)
	print ()
	print ("pila.pop()		:	 Elimino el último elemento de la pila:")
	pila.pop()
	print ("pila			:	", pila)
	print ()
	print ("n = pila.pop()")	
	n = pila.pop()
	print ("n			:	", n)
	print ("pila			:	", pila)
	print ()
	print ("pila2 = []		: 	 Creación de pila vacía")
	print ("""	Si hacemos pop() de una pila vacía, devolverá un error:

	Debemos asegurarnos siempre de que la len() de la pila sea mayor que 0 antes de extraer un elemento automáticamente.
	""")
	pila.pop()
	print ("pila.pop()")
	print ("pila			:	", pila)








	print ("---")

pilas_colas()























