def a42():
	print ("""
		1) Formatea los siguientes valores para mostrar el resultado indicado:

		"Hola Mundo" → Alineado a la derecha en 20 caracteres
		"Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)
		"Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
		150 → Formateo a 5 números enteros rellenados con ceros
		7887 → Formateo a 7 números enteros rellenados con espacios
		20.02 → Formateo a 3 números enteros y 3 números decimales

		""")
	resultado = "Hola Mundo"
	print ("{:>20}".format(resultado))
	print ("{:.3}".format(resultado))
	print ("{:^20.2}".format(resultado))
	num1 = 150
	num2 = 7887
	num3 = 20.02
	print("\n{:05d}".format(num1))
	print("{:7d}".format(num2))
	print("{:07.3f}".format(num3))
	print ()

a42()