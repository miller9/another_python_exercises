def on_the_list():
	print ("""
5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

numeros = [1, 3, 6, 9]

""")
	index=0
	numeros=[1,3,6,9]
	while True:
		value=int(input("Please enter an integer number from 0 to 9: "))
		if value>=0 and value<=9:
			if value in numeros:	# Si el valor ingresado está en la lista "numeros", agradece y sale.
				print ("It is on the list!, tahnk you.")
				print
				break
			else:
				index+=1		


		else: #value<0 or value>9:
			print ("Its not a valid option, please try again!")

	
on_the_list()
