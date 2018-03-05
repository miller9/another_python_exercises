def diccionarios():

	print ("---")
	print ("""
	Los diccionarios:

	Son junto a las listas, las colecciones más utilizadas. Se basan en una estructura mapeada donde cada elemento de 
	la colección se encuentra identificado con una clave única. Por tanto, no puede haber dos claves iguales. 
	En otros lenguajes se conocen como arreglos asociativos.

	""")
	print ("vacio = {}		:	 Creación de diccionario vacío")
	vacio = {}
	print ("vacio			:	", vacio)
	print ()
	print ("Tipo de una variable:")
	print ("type(vacio)		:	",type(vacio))
	print ()
	print ("Definición: Para cada elemento se define la estructura -> clave:valor")
	print ()
	print ("colores = {'amarillo':'yellow','azul':'blue', 'rojo':'red','naranja':'orange','morado':'purple'}")
	colores = {'amarillo':'yellow','azul':'blue', 'rojo':'red','naranja':'orange','morado':'purple'}
	print ("colores			:	", colores)
	print ()
	print ("También se pueden añadir elementos sobre la marcha:")
	print ("colores['verde'] = 'green'")
	colores['verde'] = 'green'
	print ("colores			:	", colores)
	print ()
	print ("colores['azul']		:	", colores['azul'])
	print ("colores['amarillo']	:	", colores['amarillo'])
	print ()
	print ("Las claves también pueden ser números, pero son un poco confusas:")
	print ("numeros = {10:'diez',20:'veinte'}")
	numeros = {10:'diez',20:'veinte'}
	print ("numeros			:	", numeros)
	print ("numeros[10]		:	", numeros[10])
	print ()
	print ("Modificación de valor a partir de la clave:")
	print ("colores['amarillo'] = 'white'")
	colores['amarillo'] = 'white'
	print ("colores			:	", colores)
	print ()
	print ("Función del() --> Sirve para borrar un elemento del diccionario.")
	print ("del(colores['amarillo'])")
	del(colores['amarillo'])
	print ("colores			:	", colores)
	print ()
	print ("Trabajando directamente con registros:")
	print ("edades = {'Hector':27,'Juan':45,'Maria':34}")
	edades = {'Hector':27,'Juan':45,'Maria':34}
	print ("edades			:	", edades)
	print ()
	print ("Incrementar la edad=valor de alguna clave:")
	edades['Hector']+=1
	print ("edades['Hector']+=1")
	print ("edades			:	", edades)
	print ()
	print ("Sumar valores de algunas claves 'edad=valor':")
	print ("edades['Juan'] + edades['Maria']	:", edades['Juan'] + edades['Maria'])
	print ()
	print ("""	Lectura secuencial con for .. in ..
	Es posible utilizar una iteraciín for para recorrer los elementos del diccionario:
	""")
	for edad in edades:
		print(edad)
	print ()
	print ("""	El problema es que se devuelven las claves, no los valores
	Para solucionarlo deberíamos indicar la clave del diccionario para cada elemento.	
	""")
	for clave in edades:
		print(edades[clave])
	print ()
	print ("	Mostrar ambos valores a la vez:")
	for clave in edades:
		print(clave,edades[clave])
	print ()
	print ("""	El método .items()	
	Nos facilita la lectura en clave y valor de los elementos porque devuelve ambos valores en cada iteración automáticamente:
	""")
	for c,v in edades.items():
		print(c,v)
	print ("")
	print ("""	Ejemplo utilizando diccionarios y listas a la vez:
	Podemos crear nuestras propias estructuras avanzadas mezclando ambas colecciones. 
	Mientras los diccionarios se encargarían de manejar las propiedades individuales de los registros, 
	las listas nos permitirían manejarlos todos en conjunto.
	""")
	print ("personajes = []")
	personajes = []
	print ("personajes			:	", personajes)
	print ()
	print ("p1 = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}")
	p1 = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}
	print ("personajes.append(p1)		: Agregar el diccionario 'p1' a la lista 'personajes':")
	personajes.append(p1)
	print ("personajes			:	", personajes)
	print ()
	print ("	Crear diccionarios p2 y p3, luego agregarlos a la lista 'personajes': ")
	print ()
	print ("p2 = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}")
	print ("p3 = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}")
	p2 = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
	personajes.append(p2)
	p3 = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
	personajes.append(p3)
	print ()
	print ("personajes: 	", personajes)
	print ()
	print ("Recorrer y mostar lista que almacena el diccionario completo:")
	print ()
	for x in personajes:
		print(x['Nombre'], x['Clase'], x['Raza'])
	print ()
	print ("---")


diccionarios()





