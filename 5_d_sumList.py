	
#	5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila, el cuarto elemento siempre debe #	ser el resultado de sumar los tres primeros. 

#	(La función llamada 'sum(lista)' devuelve una suma de todos los elementos de la lista)
#matriz = [ 
#    [1, 1, 1, 3],
#    [2, 2, 2, 7],
#    [3, 3, 3, 9],
#    [4, 4, 4, 13]
#]

# matriz_b = [matriz[:3][(matriz[0]+matriz[1]+matriz[2])]]

def sum_of_rows():

	matriz = [ 
	    [1, 1, 1, 3],
	    [2, 2, 2, 7],
	    [3, 3, 3, 9],
	    [4, 4, 4, 13]
	]

	print ("---")
	print ("This matrix adds each row and stores the result in the last value of each row:")
	print ("The matrix starts like this	: ")
	print (matriz)
	print ("---")
	print ("Without Slicing: ")
	matriz_b =     [[1,1,1, (matriz[0][0] + matriz[0][1] + matriz[0][2])] , 
			[2,2,2, (matriz[1][0] + matriz[1][1] + matriz[1][2])] ,
			[3,3,3, (matriz[2][0] + matriz[2][1] + matriz[2][2])] ,
			[4,4,4, (matriz[3][0] + matriz[3][1] + matriz[3][2])] 
		       ]

	print ("Size of the matrix: "+str(len(matriz_b)))
	print ("---")
	print ("The matrix is: ")
	print (matriz_b)
	print ("---")
	print ("---")
	i=0
	j=0
	print ("Looking another way to print the matrix: --> Have to fix it..")
	while i<len(matriz_b):
		#print ('['+str(matriz_b[i][j])+']',end="")	
		while j<len(matriz_b):
			print ('['+str(matriz_b[i][j])+']',end="")	
			j=j+1
		print ("--")
			#print ('['+str(matriz_b[i][j])+']',end="")	
		#i=i+1
		print ('['+str(matriz_b[i][j])+']',end="")
		i=i+1
	print ("**")

# print(mat.__str__())

sum_of_rows()














