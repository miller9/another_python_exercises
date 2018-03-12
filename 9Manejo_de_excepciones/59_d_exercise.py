print ("""
4) Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee
y además explica en un mensaje al usuario la causa y/o solución:

resultado = 15 + "20"
--> El programa se bloquea porque no se puede sumar un entero con una cadena
--> Error que lanza = TypeError: unsupported operand type(s) for +: 'int' and 'str'
	""")

try:
	resultado = 15 + "20"
except TypeError:
	print ("No se puede sumar un entero con una cadena")
	print ("Solo es posible sumar datos del mismo tipo")
	print ("Transforma la cadena a numero --> int(20)")

print ()
print ()