print ("""
6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:

Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares) # valdría [1, 5, 7]
	
	""")

numeros = [-12, 84, 13, 20, -33, 101, 9]
print ("\nOtra lista: numeros = [-12, 84, 13, 20, -33, 101, 9]")

def separar(lista):				# recibe lista como parametro
	numeros.sort()				# ordena lista con funcion '.sort()'
	pares = []					# crea lista vacia para almacenar pares
	impares = []				# crea lista vacia para almacenar impares
	for n in numeros:			# itera sobre lista 'numeros'
		if n%2 == 0:			# si el modulo es 0
			pares.append(n)		# guarda en la lista de pares
		else:					# si el modulo no es 0
			impares.append(n)	# guarda en la lista de impares
	return pares, impares		# retorna ambas listas ya ordenadas

pares, impares = separar(numeros)	# a
print(pares)
print(impares)

print ()