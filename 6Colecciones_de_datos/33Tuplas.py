def tuplas():

	print ()
	print ("""	Las Tuplas
	Son unas colecciones parecidas a las listas, con la peculiaridad de que son inmutables.
	""")
	print ()
	print ("---")
	tupla = (100,"Hola",[1,2,3],-50, 'ana', 33)
	print ("La tupla equivale a :",tupla)
	print ()
	print ("Indexación y slicing:")
	print ("tupla[0]  :	", tupla[0])
	print ("tupla[-1] :	", tupla[-1])
	print ("tupla[2:] :	", tupla[2:])
	print ("tupla[2][-1]  : ", tupla[2][-1])
	print ()
	print ("Inmutabilidad:")
	print ("tupla[0] = 50 --> lanzaría error porque la tupla no se puede modificar")
	print ()
	print ("Función len():")
	print ("len(tupla) 	:	", len(tupla))
	print ("len(tupla[2]) 	:	", len(tupla[2]))
	print ()
	print ("""	Métodos integrados
	index()
	Sirve para buscar un elemento y saber su posición en la tupla. Da error si no se encuentra.
	""")
	print ("tupla.index(100) 	:	", tupla.index(100))
	print ("tupla			:	", tupla)
	print ("tupla.index('Hola')	:	", tupla.index('Hola'))
	print ("tupla.index('Otro')	:	 lanzaría error porque 'Otro' no está en la tupla")
	print ()
	print ("count() --> Sirve para contar cuantas veces aparece un elemento en una tupla.")
	print ("tupla.count(100)	:	", tupla.count(100))
	print ("tupla.count('Algo')	:	", tupla.count('Algo'))
	tupla2 = (100,100,100,50,10)
	print ("tupla2 = (100,100,100,50,10):	")
	print ("tupla2			:	", tupla2)
	print ("tupla2.count(100)	:	", tupla2.count(100))
	print ()
	print ("append() ? --> Al ser inmutables, las tuplas no disponen de métodos para modificar su contenido.")
	print ("tupla.append(10)	:	lanzaría error porque las tuplas no se pueden modificar")
	print ("tupla			:	", tupla)
	print ("---")
	print ()


tuplas()












