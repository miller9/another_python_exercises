def par_impar():
	n = 0
	while n < 10:			# while = mientras
		if (n%2) == 0:		# if = si (de condicion)
			print(n,'es un número par')
			n=(n+1)
		else:				# else = sino (def condicion)
			print(n,'es un número impar')
			n=(n+1)



print ("This function returns a list whit the first 10 numbers indicating if they're odd or even:")
par_impar()
