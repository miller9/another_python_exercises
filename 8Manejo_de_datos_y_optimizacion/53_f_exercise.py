print ("""
6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares, y la segunda con los números impares:

Por ejemplo:

pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]
	""")

def separar(lista):
	#l_ordenada=lista.sort()
	print ("La lista recibida como argumento es:",lista)
	lista.sort()
	print ("La lista ordenada es:",lista)
	pares=[]
	impares=[]
	for l,v in enumerate(lista):
		if (lista[l]%2==0):
			#print ("l es:",[l])
			pares+=str(v)			# crea lista de strings con los numeros pares
		else:
			impares+=str(v)			# crea lista de strings con los numeros impares ---> lista de enteros?
	# return pares, impares
	print ("La lista de pares es 	:",pares)
	print ("La lista de impares es  :",impares)

lista_1=[6,5,2,1,7]
separar(lista_1)
print ()


