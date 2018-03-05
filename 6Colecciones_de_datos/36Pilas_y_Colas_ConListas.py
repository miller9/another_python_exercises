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
	print ()
	print ()
	print ("""	Las colas

	Son colecciones de elementos ordenados que únicamente permiten dos acciones:

	Añadir un elemento a la cola
	Sacar un elemento de la cola

	La peculiaridad es que el primer elemento en entrar es el primero en salir. 
	En inglés se conocen como estructuras FIFO (First In First Out).
	Debemos importar la colección deque manualmente para crear una cola:

	from collections import deque
		
	""")
	from collections import deque
	print ("cola = deque()")
	cola = deque()
	print ("cola			:	", cola)
	print ()
	print (" Podemos añadir elemento directamente pasando una lista a la cola al crearla:")	
	print ()
	print ("cola = deque(['Hector','Juan','Miguel'])")
	cola = deque(['Hector','Juan','Miguel'])
	print ("cola			:	", cola)
	print ()
	print (" Y también utilizando el método .append():")
	print ("cola.append('Maria')")
	cola.append('Maria')
	print ("cola			:	", cola)
	print ()
	print ("cola.append('Arnaldo')")
	cola.append('Arnaldo')
	print ("cola			:	", cola)
	print ()
	print ("""	popleft() en lugar de pop()

	A la hora de sacar los elementos utilizaremos el método popleft() para extraerlos por la parte
	izquierda (el principio de la cola).
	Al igual que antes, debemos asegurarnos de almacenar los elementos al sacarlos o los perderemos.

	
	""")
	print ("cola		  :", cola)
	print ()
	print ("cola.popleft()	  : Eliminar primer elemento")
	cola.popleft()
	print ("cola		  :", cola)
	print ()
	x = cola.popleft()
	print ("x = cola.popleft()")
	print ("x		  :", x)
	print ()
	print ("cola		  :", cola)
	print ()
	print ("---")
	print ()

pilas_colas()






