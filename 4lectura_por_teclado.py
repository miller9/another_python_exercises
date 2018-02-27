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
	print ("---")
	print ("")




lectura()
