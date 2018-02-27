	
#	5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila, el cuarto elemento siempre debe #	ser el resultado de sumar los tres primeros. 
#	Modificar las sumas incorrectas utilizando la técnica del slicing
#	La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

#matriz = [ 
#    [1, 1, 1, 3],
#    [2, 2, 2, 7],
#    [3, 3, 3, 9],
#    [4, 4, 4, 13]
#]

# matriz_b = [matriz[:3][(matriz[0]+matriz[1]+matriz[2])]]

def slicing_sum_of_rows():

	matriz_d = [ 
	    [1, 1, 1, 3],
	    [2, 2, 2, 7],
	    [3, 3, 3, 9],
	    [4, 4, 4, 13]
	]

	print ("---")
	print ("This matrix adds each row and stores the result in the last value of each row:")
	print ("The matrix starts like this	: ")
	print (matriz_d)
	print ("---")
	print ("Using the 'Slicing' Technique: )")
	print ("And the function sum(x):")

	matriz_d[0][-1] = sum(matriz_d[0][:-1])
	matriz_d[1][-1] = sum(matriz_d[1][:-1])
	matriz_d[2][-1] = sum(matriz_d[2][:-1])
	matriz_d[3][-1] = sum(matriz_d[3][:-1])	

	# print ("Size of the matrix: "+str(len(matriz_d)))
	print ("---")
	print ("The matrix is: ")
	print (matriz_d)
	print ("---")
	print ("---")
	

slicing_sum_of_rows()














