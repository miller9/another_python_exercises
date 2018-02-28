#	Los operadores relacionales
#	Sirven para comparar dos valores, dependiendo del #	resultado de la comparación pueden devolver:
#	Verdadero (True), si es cierta
#	Falso (False), si no es cierta


def op_relacional():
	print ("Igual que 	==> 3==2")
	print (3 == 2) #devuelve False
	print ("Distinto de	==> 3!=2") 
	print (3 != 2) #devuelve True
	print ("Mayor que	==> 3>2") 
	print (3 > 2)
	print ("Menor que	==> 3<2")
	print (3 < 2)
	print ("Mayor o igual 	==> 3>=2")
	print (3>=2)
	print ("Menor o igual 	==> 3<=2")
	print (3<=2)
	print ("Menor o igual 	==> 1<=2")
	print (1<=2)
	print ("---")
	print ("Variables: a=10, b=5:")
	a=10
	b=5
	print ("a es menor o igual que b?")
	print (a<=b)
	print ("a es mayor o igual que b?")
	print (a>=b)
	print ("a es diferente de b?")
	print (a!=b)
	print ("a es igual b*2?")
	print (a==b*2)
	print ("---")
	print ("Comparación de cadenas:")
	z="Hola"
	print ("z = 'Hola'")	
	print (" z == 'Hola'?")
	print (z == "Hola")
	print (" z != 'Hola'?")
	print (z != "Hola")
	print ("---")
	print ("Comparación de caracteres específicos:")
	print ("c='Hola'")
	c="Hola"
	print ("c[0] == 'H'?")
	print (c[0] == "H")
	print ("---")
	print ("Comparación de Arrays:")
	print ("a1 = [1,2,3] - a2 = [2,3,4]")
	a1=[1,2,3]
	a2=[2,3,4]
	print ("a1==a2?")
	print (a1 == a2)
	print ("len(a1) == len(a2) ?")
	print (len(a1)==len(a2))
	print ("---")
	print ("Comparación con los índices:")
	print ("El último elemento de a1 es igual al primer elemento de a2?")
	print (a1[-1] == a2[0])
	print ("---")
	print ("Lógicos:")
	print (" True == True ?")
	print (True == True)
	print (" True == False ?")
	print (True == False)
	print (" True != False ?")
	print (True != False)
	print (" True > False ?")
	print (True > False)
	print (" True < False ? ")
	print (True < False)
	print ("---")
	print ("Ariméticamete True=1 y False=0:")
	print ("True * 3 ?")
	print (True * 3)
	print ("False * 3 ?")
	print (False * 3)
	print ("True / 5 ?")
	print (True/5)
	print ("False / 5 ?")
	print (False/5)
	print ("True * False ?")
	print (True * False)
	print ("True * True ?")
	print (True * True)	
	print ("False * False ?")
	print (False*False)
	print ("---")


	

op_relacional()







