def lectura():
	print ("""
	Entradas por teclado

	Función input() lee una cadena por teclado. 
	Su único inconveniente es que debemos transformar el valor a numérico si deseamos hacer operaciones con él:
	
	""")
	decimal = float( input("Introduce un número decimal con punto: ") )
	valores = []
	print("Introduce 3 valores")
	for x in range(3):
		valores.append( input("Introduce un valor --> ") )
	print ("\n El arreglo ingresado es: ",valores)
	print ()

lectura()


