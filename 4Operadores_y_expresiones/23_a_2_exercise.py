"""
1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

    Si los dos números son iguales
    Si los dos números son diferentes
    Si el primero es mayor que el segundo
    Si el segundo es mayor o igual que el primero
"""

def conditions_a_2():
	print ("---")
	first_n = int( input("Please, enter the first number: ") )
	second_n = int( input("Please, enter the second number: ") )
	print ("---")
	print ("Numbers are equal?					", first_n == second_n)
	print ("Numbers are different?					", first_n != second_n)
	print ("First number is greater than second number?		", first_n > second_n)
	print ("Second number is greater or equal than first number?	", second_n >= first_n)
	print ("---")

conditions_a_2()
