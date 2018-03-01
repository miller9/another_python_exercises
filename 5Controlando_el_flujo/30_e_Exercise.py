def a():
	print ("""
5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

numeros = [1, 3, 6, 9]

""")
	index=0
	numeros=[1,3,6,9]
	while True:
		value=int(input("Please enter an integer number from 0 to 9: "))
		if value<0 or value>9:
			print ("Its not a valid option, please try again!")
		# numeros=numeros+numeros.append(value)
		# if value>=0 and value<=9:
		for numero in numeros:
			if (numeros[index]==value):
				print ("ok, the number is on the list.")
				print ()
				break
			else:
				index+=1		
#	index+=1

a()
