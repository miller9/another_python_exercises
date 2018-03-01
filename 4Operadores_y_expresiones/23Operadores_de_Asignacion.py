def operad_asig():
	print ("---")
	print ("Operadores de asignación:")
	print ("Actúan directamente sobre la variable actual modificando su valor")
	print ("---")
	a=0
	print ("Asignación normal	==> a=0 ")
	print ("a+=1 			==> Incrementa en 1 el valor de a: ")
	a+=1	
	print (a)
	print ("a += 5 			==> Incrementa en 5 el valor de a: ")
	a+=5 # suma en asignación
	print (a)
	print ("a -= 4 # resta en asignación:")
	a -= 4 # resta en asignación
	print (a)
	print ("a *= 6 # producto en asignación:")
	a *= 6 # producto en asignación
	print (a)
	print ("a /= 2 # división en asignación:")
	a /= 2 # división en asignación
	print (a)
	print ("a %= 2 # módulo en asignación:")
	a %= 2 # módulo en asignación
	print (a)
	print ("---")
	print ("a=5")
	a=5
	print ("a **= 5 # potencia en asignación:")
	a **= 5 # potencia en asignación)
	print (a)
	print ("---")
	print ("Expresiones en el siguiente código ==> Ver comentarios")
	print ("---")
	n = 0 	 			#  Asignación de 0 en n
	while n < 10:			#  Expresión relacional n < 10, que devuelve True
		if (n % 2) == 0: 	# Expresión aritmética y expresión relacional
			print(n,'es un número par')
		else:
			print(n,'es un número impar')
		n += 1			# expresión aritmética n = n + 1 equivalente a operación en asignación n+=1
	print ("---")




operad_asig()








