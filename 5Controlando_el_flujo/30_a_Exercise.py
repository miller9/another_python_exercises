def arithmetic_menu():
	print ("""
1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

    Mostrar una suma de los dos números
    Mostrar una resta de los dos números (el primero menos el segundo)
    Mostrar una multiplicación de los dos números
    En caso de no introducir una opción válida, el programa informará de que no es correcta.
""")
	print ("---")
	print ("")	
	num1=float( input("Please enter the first number:") )
	num2=float( input("Please enter the second number:") )
	print ()
	
	while True:
		print ("""Choose the option to compute:
1: Sum of the numbers
2: Substraction of the numbers
3: Product of the numbers
4: Exit
""")	
		option=int(input())
		if (option==1):
			print ("The sum is:", num1+num2)
			print ()		
		elif (option==2):
			print ("The substraction is:", num1-num2)
			print()
		elif (option==3):
			print ("The product is:", num1*num2)
			print ()
		if (option==4):
			print ("Bye bye!")
			break
		else:
			print ("Invalid Option, please try again!")	# If the value is a String, the program breaks
			print ()		
	print ("---")


arithmetic_menu()






