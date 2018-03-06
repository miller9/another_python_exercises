def salidas():
	print ("""
		Salida por pantalla:

		La función print() es la forma general de mostrar información por pantalla. 
		Generalmente podemos mostrar texto y variables separándolos con comas:

		""")

	v = "otro texto"
	n = 10
	print("\nUn texto",v,"y un número",n)
	print ("""
	El método .format():
	Es una funcionalidad de las cadenas de texto que nos permite formatear información en una cadena
	(variables o valores literales) cómodamente utilizando identificadores referenciados:
	""")

	c = "Un texto '{}' y un número '{}'".format(v,n)
	print (c)




salidas()