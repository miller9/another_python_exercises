def comparing_lists():
	print ("""
	7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
	pero no debe repetise ningún elemento en la nueva lista:	
	""")
	print ("---")
	a=(list(range(0,31,3)))
	print ("First list is	 --> ", a)
	b=(list(range(0,31,2)))
	print ("Second list is 	 --> ", b)

#	c=[1]*len(b)	# Strange trick!?
	c=[ ]
	for index,value in enumerate(a):
		if (a[index] in b):
		#	c += str(value)		# If I concatenate, I get an array of 'Characters', not the array of numbers that i want 
			c.append(value)		# This way, it works well because the list is growing with the numbers on both lists.
	print ("New list is      --> ",c)
	print ()
						#######		INCLUDE A DYNAMIC MENU TO ENTER THE LISTS...

comparing_lists()
