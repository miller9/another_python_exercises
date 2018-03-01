def dynamics_lists():
	print ("""
6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

    Todos los números del 0 al 10 		 [0, 1, 2, ..., 10]
    Todos los números del -10 al 0 		 [-10, -9, -8, ..., 0]
    Todos los números pares del 0 al 20 	 [0, 2, 4, ..., 20]
    Todos los números impares entre -20 y 0 	 [-19, -17, -15, ..., -1]
    Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).

""")
	print ("---")
	print ("All numbers from 0 to 10:	", list(range(11)))
	print ()
	print ("All numbers from -10 to 0:	", list(range(-10,1)))
	print ()
	print ("All even numbers from 0 to 20:	", list(range(0,22,2)))
	print ()
	print ("All odd numbers from -20 to 0:	", list(range(-19, 1, 2)))
	print ()
	print ("All 5 multiples from 0 to 50: 	", list(range(0,51,5)))
	print ("---")
	print ()

dynamics_lists()




