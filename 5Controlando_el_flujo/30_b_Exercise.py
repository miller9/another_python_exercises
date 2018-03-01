def just_odd_numbers():
	print ("""
2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
	""")
	print ()
	while (True):
		number=(float(input("Please enter an odd number:")))
		if (number%2!=0):
			print ("Thanks for ur help, see u")
			print ()
			break		
		else:
			print ()		
			print ("Its not an odd number, please try again!")
			print ()
		

just_odd_numbers()
