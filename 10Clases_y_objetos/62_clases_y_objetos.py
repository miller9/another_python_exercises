print ("\nClases y Objetos:")


print ("\nDefinición de clase + Instanciación:")
# Definición de clase
class Galleta:
	pass

# Instanciación
una_galleta = Galleta()
otra_galleta = Galleta()
g1 = Galleta()
g2 = Galleta()
g3 = Galleta()
print ("---")

def hola():
	pass

print ("\n --> Función type(): Sirve para determinar la clase de un objeto.")
print ("Se le pasa como argumento, el objeto del cual se quiere conocer el 'tipo':")

print ("\nuna_galleta 		:",type(una_galleta))
print ("g2			:",type(g2))
print ("10			:",type(10))
print ("[]			:",type([]))
print ("{}			:",type({}))
print ("3.14			:",type(3.14))
print ("saludo			:",type("saludo"))
print ("True			:",type(True))
print ("hola()			:",type(hola()))
print ("---")
print ()