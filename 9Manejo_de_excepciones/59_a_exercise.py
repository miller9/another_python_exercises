print ("""
1) Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee y
además explica en un mensaje al usuario la causa y/o solución:
	resultado = 10/0
	--> Se bloquea porque no es posible dividir por '0'
	""")
# resultado = 10/0
try:
	resultado = 10/0
	print ("No es posible dividir por 0")
	print ("Ingrese un valor mayor o igal a 1")
except ZeroDivisionError:
	print("No se puede dividir por cero, prueba otro número")
print ("""
	""")