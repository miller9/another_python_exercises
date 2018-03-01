"""
3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

    Guarda en una variable numero_magico el valor 12345679 (sin el 8)
    Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)
    Multiplica el numero_usuario por 9 en sí mismo
    Multiplica el numero_magico por el numero_usuario en sí mismo
    Finalmente muestra el valor final del numero_magico por pantalla
"""

def magic_n():
	print ("---")
	magic_number=12345679
	print ("Please enter the user number -between 1 and 9-:")
	user_number=int(input())
	print ("user_number *= 9 :")
	user_number *= 9
	print (user_number)
	print ("magic_number *= user_number :")
	magic_number *= user_number
	print (magic_number)
	print ("---")
	print ("The new value of magic number is:")
	print (magic_number)


magic_n()
