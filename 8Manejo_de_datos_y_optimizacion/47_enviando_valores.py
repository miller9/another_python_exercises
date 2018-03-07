print ("""
Envío de valores:
Para comunicarse con el exterior, las funciones no sólo pueden devolver valores, también pueden recibir información:
	""")

def suma(a,b): # valores que se reciben
	return a+b

print ("\nAhora podemos enviar dos valores a la función: 2 y 5")
r = suma(2,5)  # valores que se envían
print ("el valor de r es:",r)
print ("""\nParámetros y argumentos:
En la definición de una función, los valores que se reciben se denominan parámetros,
y en la llamada se denominan argumentos.""")