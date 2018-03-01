def sum_of_even_numbers():
	print ("""
3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:

Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

""")
	print ("The even numbers until 100 is:", list(range(0,102,2)))
	print ()
	print ("The sum of even numbers until 100 is:", sum(range(0,102,2)))
	# print ("The sum of even numbers until 100 is:", sum(list(range(0,102,2))) --> This way it works too.
	print ("---")

sum_of_even_numbers()
