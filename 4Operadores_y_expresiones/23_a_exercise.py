"""
1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

    Si los dos números son iguales
    Si los dos números son diferentes
    Si el primero es mayor que el segundo
    Si el segundo es mayor o igual que el primero
"""

def conditions():
	print ("---")
	print ("Please, enter the first number:")
	first_n=input()
	print ("Please, enter the second number:")
	second_n=input()
	print ("---")
	print ("Numbers are equal?")
	print (first_n == second_n)
	print ("Numbers are different?")
	print (first_n != second_n)
	print ("First number is greater than second number?")
	print (first_n > second_n)
	print ("Second number is greater or equal than first number?")
	print (second_n >= first_n)
	print ("---")

conditions()
