def comparing_lists():
	print ("""
7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:	
	""")
	print ("---")
	a=(list(range(0,31,3)))
	print ("First list is:	", a)
	b=(list(range(0,31,2)))
	print ("Second list is:	", b)
	i=0
	cont=0
#	c=[1]*len(a)
	c=" "	#Its working, but its a string, it must be a list....

	for index,value in enumerate(a):
		if (a[index] in b):
			c += str(value)+","
			i+=1

	print ("New list is: 	",c)
	print ("")

comparing_lists()
