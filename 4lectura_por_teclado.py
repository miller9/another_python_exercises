def lectura():

	print ("Se usa la instrucción input() que lee y devuelve una cadena:")
	print ("---")
	print ("Ingrese su nombre:")
	nombre = input()
	print ("El nombre ingresado es: "+str(nombre))	
	print ("---")
	print ("Ingrese el año actual: ")
	año = input()
	print ("El año ingresado es: "+str(año))
	print ("Aunque leemos un número, en realidad es una cadena de texto")	
	print ("Se convierte a cadena con la instrucción: str(x)")
	print ("---")	
	# Podemos mostrar un mensaje antes de leer el valor
	print ("Podemos mostrar un mensaje antes de leer el valor, en la misma línea de código:")
	valor = input("Introduce un valor: ")
	print ("El valor ingresado es: "+str(valor))
	print ("---")
	# Lo que se ingresa por teclado siempre son cadenas = Strings:
	print ("Lo que se ingresa por teclado siempre son cadenas = Strings:")
	print ("# Una cadena y un número no se pueden operar ==> valor + 100 ")
	print ("Lanza error porque no se puede sumar un string con un entero")
	# Convierto el String "valor" en un entero:
	valor = int(valor)
	# Imprimo el entero y ahora si se puede operar con otros enteros:	
	print ("---")
	print ("")
	val_entero = input("Introduce un número entero: ")
	print ("El entero ingresado es: "+str(val_entero))
	print ("---")
	print ("Para convertir a entero ==> Cast con int(), de cadena a entero:")
	# La función int() de entero, devuelve un número entero a partir de una cadena
	print ("valor = "+str(valor))	
	valor = int(valor)
	print ("valor + 15 = "+str(valor+15))
	print ("---")
	print ("Para convertir a float ==> Cast con float(), de cadena a flotante:")
	# La función float() de flotante, devuelve un número flotante a partir de una cadena
	valor = float(valor) 
	print ("El 'valor' que tenía guardado, pero ahora en tipo float es: "+str(valor))
	print ("10 + valor = "+str(10+valor))
	print ("---")
	print ("Lectura por teclado + cast a float, se haría así:")
	print ('value = float( input("Introduce un número decimal o entero: ") )')
	value = float( input("Introduce un número decimal o entero: ") )
	print ("El numero ingresado es convertido a tipo float: "+str(value))
	print ("---")
	print ("---")

lectura()


