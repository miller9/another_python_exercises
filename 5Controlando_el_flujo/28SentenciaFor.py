def for_senten():
	print ("")	
	print (""" Recorriendo los elementos de una lista utilizando While:
""")
	numeros = [1,2,3,4,5,6,7,8,9,10]
	indice = 0
	while indice < len(numeros):
		print(numeros[indice])
		indice+=1
	print ("")
	print ("Sentencia For (Para) con listas:")
	print ("")
	for numero in numeros:  # Para [variable] en [lista]	# Por "cada variable" en el arreglo "numeros"
		print(numero)					# imprima lo que hay en "cada variable"
	print ("")
	print ("""Modificar ítems de la lista durante el recorrido: (al vuelo):

Para asignar un nuevo valor a los elementos de una lista mientras la recorremos, podríamos intentar asignar al número el nuevo valor: --> Multiplicar cada valor guardado en el arreglo por 10:
""")
	for numero in numeros:
		numero *= 10
	print (numeros)
	print ("")
	print ("Sin embargo, ésto no funciona. La forma correcta de hacerlo es haciendo referencia al índice de la lista en lugar de la variable:")
	indice = 0
	numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for numero in numeros:
		numeros[indice] *= 10
		indice+=1
	print ("")
	print (numeros)
	print ("")
	print ("Podemos utilizar la función enumerate() para conseguir el índice y el valor en cada iteración fácilmente:")
	print ("")
	numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	for indice,numero in enumerate(numeros):
		numeros[indice] *= 10
	print (numeros)
	print ("")
	print (" For con cadenas:")
	print ("")
	cadena = "Hola amigos"
	for caracter in cadena:
		print(caracter)
	print ("")
	print ("---")
	print ("Pero debemos recordar que las cadenas son inmutables:")
	print ("como lanza error, ver for en comentarios...")
#	for i,c in enumerate(cadena):
#		cadena[i] = "*"
	print ("---")
	print ("")
	print ("Sin embargo siempre podemos generar una nueva cadena:")
	print ("cadena = ",cadena)	
	cadena2 = ""
	for caracter in cadena:
		cadena2 += caracter * 2
	print ("cadena2 = ",cadena2)
	print ("")
	print ("""La función range():
Sirve para generar una lista de números que podemos recorrer fácilmente, pero no ocupa espacio en memoria porque se interpreta sobre la marcha:
""")
	for i in range(10):
		print(i)
	print ("")
	print ("range(10): Range va desde el primer valor(que incluye) hasta el indicado en el argumento(no incluye):")
	print (range(10))
	print ("")
	for i in [0,1,2,3,4,5,6,7,8,9]:
		print(i)
	print ("")
	print ("Si queremos crear la lista literalmente, podemos transformar el range a una lista: --> list(range(10))")
	list(range(10))
	print (list(range(10)))
	print ("---")
	
for_senten()








