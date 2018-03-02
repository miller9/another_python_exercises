def comparing_lists():
	print ("""
	7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
	pero no debe repetise ningún elemento en la nueva lista:	
	""")
	print ("---")
	a=(list(range(0,31,3)))
	print ("A list is	 --> ", a)
	b=(list(range(0,31,2)))
	print ("B list is 	 --> ", b)

#	c=[1]*len(b)	# Strange trick!?
	c=[ ]
	for value in a:
		if value in b and value not in c:
			c.append(value)

	print ("C list is	 --> ",c)
	print ()
						#######		INCLUDE A DYNAMIC MENU TO ENTER THE LISTS...

comparing_lists()
