def conjuntos():

	print ("""	Los conjuntos
	
	Son colecciones desordenadas de elementos únicos utilizados para hacer pruebas de pertenencia a grupos 
	y eliminación de elementos duplicados.
	""")
	print ("---")
	conjunto = set()
	print ("conjunto = set()	:	 Creación del conjunto")
	print ("conjunto		:	", conjunto)
	conjunto = {1,2,3}
	print ("conjunto = {1,2,3}	:	 Asignando valores")
	print ("conjunto		:	", conjunto)
	print ()
	print ("""	Método add()
	Sirve para añadir elementos al conjunto. Si un elemento ya se encuentra, no se añadirá de nuevo.
	""")
	print ("conjunto.add(4)		: 	 Agregar el valor '4' al conjunto")
	conjunto.add(4)
	print ("conjunto		:	", conjunto)
	print ("conjunto.add(0)		:	 Agregar el valor '0' al conjunto")
	conjunto.add(0)
	print ("conjunto		:	", conjunto)
	print ()
	print ("""	Colecciones desordenadas
	Se dice que son desordenados porque gestionan automáticamente la posición de sus elementos, 
	en lugar de conservarlos en la posición que nosotros los añadimos.
	""")
	print ("conjunto.add('H')	:	 Agregar el valor 'H' al conjunto")
	conjunto.add('H')
	print ("conjunto		:	", conjunto)
	print ("conjunto.add('Z')	:	 Agregar el valor 'Z' al conjunto")
	conjunto.add('Z')
	print ("conjunto		:	", conjunto)
	print ("conjunto.add('A')	:	 Agregar el valor 'A' al conjunto")
	conjunto.add('A')
	print ("conjunto		:	", conjunto)
	print ("conjunto.add(0)		:	 Agregar el valor '0' al conjunto --> Como ya está, no lo agrega nuevamente")
	conjunto.add(0)
	print ("conjunto		:	", conjunto)
	print ()
	print ("Pertenencia a grupos con in:")
	grupo = {'Hector','Juan','Mario'}
	print ("grupo = {'Hector','Juan','Mario'} --> Asignación de elementos")
	print ("grupo			:	", grupo)
	print ("'Hector' in grupo	:	", 'Hector' in grupo)
	print ("'Maria' in grupo	:	", 'Maria' in grupo)
	print ("'Juan' in grupo		:	", 'Juan' in grupo)
	print ("'Hector' not in grupo	:	", 'Hector' not in grupo)
	print ("'Maria' not in grupo	:	", 'Maria' not in grupo)
	print ()
	print ("Auto-eliminación de elementos duplicados:")
	print ("test = {'Hector','Hector','Hector'} --> Asignación de elementos")
	test = {'Hector','Hector','Hector'}
	print ("test			:	", test)
	print ()
	print ("test.add('Ana')		:	 Agregar elemento 'Ana'")
	test.add('Ana')
	print ("test			:	", test)
	print ("test.add('Mile')	:	 Agregar elemento 'Mile'")
	test.add('Mile')
	print ("test			:	", test)	
	print ("test.add('Ana')		:	 Agregar elemento repetido --> No lo agrega porque ya está")
	test.add('Ana')
	print ("test			:	", test)
	print ()
	print ("""	Cast de lista a conjunto y viceversa
	Es muy útil transformar listas a conjuntos para borrar los elementos duplicados automáticamente.
	""")
	print ("l = [1,2,3,3,2,1]	:	 Crear lista")	
	l = [1,2,3,3,2,1]
	print ("l			:	", l)
	print ("c = set(l)		:	 Convertir lista a conjunto")
	c = set(l)
	print ("c			:	", c)
	print ("l = list(c)		: 	 Convertir conjunto a lista")
	l = list(c)
	print ("l			:	", l)
	print ("l2 = [1,2,3,4,4,3,2,1]	:	 Creación de otra lista")
	l2 = [1,2,3,4,4,3,2,1]
	print ("l2			: 	", l2)
	print ("l2 = list( set( l2 ) )	:	 Convertir en una sola línea: lista-conjunto-lista")
	l2 = list( set( l2 ) )
	print ("l2			: 	", l2)
	print ()
	print ("""	Cast de cadena a conjunto
	Sirve para crear un conjunto con todos los caracteres de la cadena.
	""")
	s = "Al pan pan y al vino vino"
	print ('s = "Al pan pan y al vino vino":')
	set(s)
	print ("set(s)			: 	 Convertir cadena a conjunto")
	print ("s			:	", s)
	print ("s[3] 			:	 Mostrar tercer elemento del conjunto 's'")
	print ("s[3]			:	", s[3])
	print ()


conjuntos()


