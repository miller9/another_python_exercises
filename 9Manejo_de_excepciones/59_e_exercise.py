print ("""
5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. 
La función debe añadir el elemento al final de la lista con la condición 
de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista 
se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

  Error: Imposible añadir elementos duplicados => [elemento].

Prueba de agregar los elementos 10, -2, "Hola" a la lista de elementos con
la función una vez la has creado y luego muestra su contenido.
Nota: Puedes utilizar la sintaxis: elemento in lista


	""")

elementos = [1,5,-2]
def agregar_una_vez(lista, elem):
	
	try:
		if elem in lista:
			raise ValueError
		else:
			lista.append(elem)
	except ValueError:
	#	print ("Error: Imposible añadir elementos duplicados => ",elem,".")					# ok
		print ("Error: Imposible añadir elementos duplicados => {}".format(elem),"...")		# ok
		print ()


# agregar_una_vez(10,-2,"Hola")
print ("---")
print ("Lista original:		",elementos)

print ("\nAgregar el valor '10':")
agregar_una_vez(elementos,10)
print ("La lista es: 		",elementos)

print ("\nAgregar el valor '-2':")
agregar_una_vez(elementos,-2)
print ("La lista es: 		",elementos)

print ('\nAgregar el valor "Hola":')
agregar_una_vez(elementos,"Hola")
print ("La lista es: 		",elementos)

print ()
print (elementos)
print ()