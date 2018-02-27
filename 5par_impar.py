def par_impar():
	n = 0
	while n < 10:			# while = mientras
		if (n%2) == 0:		# if = si (de condicion)
			print(n,'es un número par')
			n=(n+1)
		else:			# else = sino (def condicion)
			print(n,'es un número impar')
			n=(n+1)

print ("This function returns a list with the first 10 numbers indicating if they're odd or even:")
par_impar()

print ("---")
print ("---")

def par_impar2(a):
	x=a+10
	while a < x:				# while = mientras
		if (a%2) == 0:			# if = si (de condicion)
			print(a,'es un número par')
			a=(a+1)
		else:				# else = sino (def condicion)
			print(a,'es un número impar')
			a=(a+1)


print ("This function returns a list with numbers from 30 to 39 indicating if they're odd or even:")
par_impar2(30)


print ("---")
print ("---")

def even_odd3():
	# x=a+1
	# while a < x:
	a=int(input("what is the number to analyze: "))
	if (a%2) == 0:			
		print(a,'is an even number')

	else:				
		print(a,'is an odd number')



print ("This function ask for an argument & returns a message indicating if it's an odd or even number:")
even_odd3()

