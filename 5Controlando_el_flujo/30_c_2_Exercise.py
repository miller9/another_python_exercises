def sum_of_even_numbers():
	print ("""
	3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:

	Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. 
	El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.
	""")
	print ()
	print ("The even numbers until 100 is:", list(range(0,102,2)))
	print ()
	my_list=list(range(0,102,2))
	i=0
	res=0
	# This another way to do it, without using the function "sum()"
	while i<len(my_list):
		res += my_list[i]
		i+=1
	print ("The sum of the even numbers from 0 to 100 is:",res)
	print ("---")

sum_of_even_numbers()
