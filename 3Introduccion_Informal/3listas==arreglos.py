def listas():
	#Las listas o arrays Funcionan similar a los Strings:
	numeros = [12,13,14,15,16,17]
	print ("Array de numeros 			==>"+str(numeros))
	# Se pueden almacenar diferentes tipos de datos en una lista:
	datos = ["mile", 54, "colombia", 3.14, "dgilmour", "minina", 33, 34, 35, 36]
	print ("Array con diferentes tipos de datos 	==> "+str(datos))
	print ("---")
	print ("Índices y slicing Funcionan de una forma muy similar a las cadenas de caracteres:")	
	print ("Primer valor del array 			==> "+datos[0])
	print ("Ultimo valor del array			==> "+str(datos[-1]))
	print ("Desde el 4° valor hasta el final	==> "+str(datos[3:]))
	print ("---")
	# Se pueden concatenar listas:	
	print ("Suma de listas ==> Da como resultado una nueva lista que incluye todos los ítems:")
	print ("numeros + [21, 22, 23, 24, 25] 		==> "+str(numeros + [21, 22, 23, 24, 25]))
	print ("pero el array de numeros sigue siendo	==> "+str(numeros))
	print ("---")
	print ("Son modificables: A diferencia de las cadenas, en las listas sí podemos modificar sus ítems utilizando índices:")
	pares = [0,2,4,5,8,10]
	print ("Arreglo pares				==> "+str(pares))
	print (pares)
	pares[3]= 6
	print ("Arreglo pares				==> "+str(pares))
	print (pares)
	print ("---")
	print ("Integran funcionalidades internas, como el método .append() para añadir un ítem al final de la lista:")	
	print ("Agregar un elemento usando: pares.append(x)")
	pares.append(12)	
	print (pares)
	print ("---")
	print ("Agregar el resultado de una operación: pares.append(7*2)")
	pares.append(7*2)
	print (pares)
	print ("---")
	print ("Y una peculiaridad, es que también aceptan asignación con slicing para modificar varios ítems en conjunto:")
	letras = ['a','b','c','d','e','f']
	print ("Arreglo de letras			==> "+str(letras))
	print ("Mostrar los 3 primeros valores (slicing)==> letras[:3]")
	print (letras[:3])
	print ("Cambiar los 3 primeros valores (slicing)==> letras[:3] = ['A','B','C']")
	letras[:3] = ['A','B','C']
	print (letras)
	# Se puede eliminar contenido de las listas con Slicing:
	print ("---")
	print ("Asignar una lista vacía equivale a borrar los ítems de la lista o sublista:")
	letras[:3] = []
	print ("letras[:3] = []		      (slicing) ==> "+str(letras))
	print ("Se podría vaciar el arreglo completo con: letras = []")
	print ("---")
	print ("La función len() también funciona con las listas del mismo modo que en las cadenas:")
	print ("len(letras)				==> "+str(len(letras)))
	print ("len(pares)				==> "+str(len(pares)))
	print ("len(datos)				==> "+str(len(datos)))
	print ("len(numeros)				==> "+str(len(numeros)))
	print ("---")
	print ("Listas dentro de listas (anidadas):")
	print ("Podemos manipular fácilmente este tipo de estructuras utilizando múltiples índices, como si nos refieréramos a las filas y columnas de una tabla:")
	# Listas Anidadas:
	a = [1,2,3]
	b = [4,5,6]
	c = [7,8,9]
	r = [a,b,c]
	print ("Mostrar la lista anidada=Matriz 	==> "+str(r))
	print ("Primera sublista r[0]			==> "+str(r[0]))
	print ("Segunda sublista r[1]			==> "+str(r[1]))
	print ("Tercera sublista r[2]			==> "+str(r[2]))
	print ("Última sublista r[-1]			==> "+str(r[-1]))
	print ("---")
	print ("La lista anidada es lo mismo que una matriz:")
	print ("Puedo acceder a cada elemento --> nombreLista[columna][fila]:")
	print ("---")
	print ("Primera sublista, y de ella, primer ítem r[0][0]	==> "+str(r[0][0]))
	print ("Segunda sublista, y de ella, segundo ítem r[1][1]	==> "+str(r[1][1]))
	print ("Tercera sublista, y de ella, tercer ítem r[2][2]	==> "+str(r[2][2]))
	print ("Última sublista, y de ella, último ítem r[-1][-1]	==> "+str(r[-1][-1]))
	print ("---")
	print ("Segunda sublista, y de ella, primer ítem r[2][0]	==> "+str(r[2][0]))
	print ("Primera sublista, y de ella, último ítem r[0][2]	==> "+str(r[0][2]))


listas()


























