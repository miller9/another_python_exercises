def comparing_lists():
	print ("""
	7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
	pero no debe repetise ningún elemento en la nueva lista:	
	""")
	print ("---")
	a = ["h",'o','l','a',' ', 'm','u','n','d','o']
	b = ["h",'o','l','a',' ', 'l','u','n','a']
	c = []
	print ("The A list is: 		",a)
	print ("The B list is: 		",b)
	for value in a:
		if value in b and value not in c:
			c.append(value)

	print ("The C list is:		",c)
	print ()
						#######		INCLUDE A DYNAMIC MENU TO ENTER THE LISTS...

comparing_lists()
