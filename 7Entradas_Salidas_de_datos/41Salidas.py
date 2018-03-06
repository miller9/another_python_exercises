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
	print ("\nTambién podemos referenciar a partir de la posición de los valores utilizando índices:")
	print( "Un texto '{1}' y un número '{0}'".format(v,n) )
	print ("\nO podemos utilizar identificador con una clave y luego pasarlas en el format:")
	print( "Un texto '{v}' y un número '{n}'".format(n=n,v=v) )
	print("{v},{v},{v}".format(v=v))
	print ("\nFormateo avanzado: Alineamiento a la derecha en 30 caracteres:")
	print( "{:>30}".format("palabra") )
	print ("\nAlineamiento a la izquierda en 30 caracteres:")
	print( "{:30}".format("palabra") )  
	print ("\nAlineamiento al centro en 30 caracteres:")
	print( "{:^30}".format("palabra") )
	print ("\nTruncamiento a 3 caracteres:")
	print( "{:.5}".format("palabra") )
	print ("\nAlineamiento a la derecha en 30 caracteres con truncamiento de 3:")
	print( "{:>30.3}".format("palabra") )
	print ("\nFormateo de números enteros, rellenados con espacios:")
	print("{:4d}".format(10))
	print("{:4d}".format(100))
	print("{:4d}".format(1000))
	print ("\nFormateo de números enteros, rellenados con ceros:")
	print("{:04d}".format(10))
	print("{:04d}".format(100))
	print("{:04d}".format(1000))
	print ("\nFormateo de números flotantes, rellenados con espacios:")
	print("{:7.3f}".format(3.1415926))
	print("{:7.3f}".format(153.21))
	print ("\nFormateo de números flotantes, rellenados con ceros:")
	print("{:07.3f}".format(3.1415926))
	print("{:07.3f}".format(153.21))
	print ()

salidas()