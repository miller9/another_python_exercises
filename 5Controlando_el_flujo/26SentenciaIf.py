
def if_sent():
	print ("---")
	print ("Condiciones --> Sentencia If (Si):")
	print ("Permite dividir el flujo de un programa en diferentes caminos. El if se ejecuta siempre que la expresión que comprueba devuelva True")
	print ("---")
	if True:  # equivale a if not False
		print("Es true, implica que se cumple la condición")
		print("También se muestre este print")
	print ("---")
	print ("Podemos encadenar diferentes If:")
	a = 5
	if a == 2:
		print("a vale 2")
	if a == 5:
		print("a vale 5")
	print ("---")
	print ("O también anidar If dentro de If:")
	a = 5
	b = 10
	if a == 5:
		print("a vale",a)
		if b == 10:
			print("	y b vale",b)
	print ("---")
	print ("Como condición podemos evaluar múltiples expresiones, siempre que éstas devuelvan True o False:")
	if a==5 and b == 10:
		print("Se cumplen ambas condicinoes, a vale 5 y b vale 10")
	print ("---")
	print ("---")
	print ("Sentencia Else (Sino)")
	print ("Se encadena a un If para comprobar el caso contrario (en el que no se cumple la condición).")
	print ("---")
	print ("Par o Impar:")	
	n = 11
	if n%2 == 0:
		print(n,"es un número par")
	else:
		print(n,"es un número impar")
	print ("---")
	print ("---")
	print ("Sentencia Elif (Sino Si)")
	print ("Se encadena a un if u otro elif para comprobar múltiples condiciones, siempre que las anteriores no se ejecuten.")
	print ("--- Ej if, elif, elif, else:")
	comando = "OTRA COSA"
	if comando == "ENTRAR":
		print("Bienvenido al sistema")
	elif comando == "SALUDAR":
		print("Hola, espero que te lo estés pasando bien aprendiendo Python")
	elif comando == "SALIR":
		print("Saliendo del sistema...")
	else:
		print("Este comando no se reconoce")
	print ("---")
	nota = float(input("Introduce una nota: "))
	if nota >= 9:
		print("Sobresaliente")
	elif nota >= 7:
		print("Notable")
	elif nota >= 6:
		print("Bien")
	elif nota >= 5:
		print("Suficiente")
	else:
		print("Insuficiente")
	print ("---")
	print ("Es posible simular el funcionamiento de elif con if utilizando expresiones condicionales:")
	print ("---")
	nota = float(input("Introduce una nota: "))
	if nota >= 9:
		print("Sobresaliente")
	if nota >= 7 and nota < 9:
		print("Notable")
	if nota >= 6 and nota < 7:
		print("Bien")
	if nota >= 5 and nota < 6:
		print("Suficiente")
	if nota < 5:
		print("Insuficiente")
	print ("---")
	print ("---")
	print ("Instrucción Pass:")
	print ("Sirve para finalizar un bloque, se puede utilizar en un bloque vacío:")
	if True:
		pass
	print ("---")
	print ("---")

if_sent()











