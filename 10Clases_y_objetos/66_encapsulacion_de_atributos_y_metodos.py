print ("Encapsulación:")
print ("""Consiste en denegar el acceso a los atributos y 
	métodos internos de la clase desde el exterior.
	En Python no existe, pero se puede simular precediendo 
	atributos y métodos con dos barras bajas __:
	""")

# 
class Ejemplo:
	__atributo_privado = "Soy un atributo inalcanzable desde fuera"
	
	def __metodo_privado(self):
		print("Soy un método inalcanzable desde fuera")


# Crear objeto del tipo 'Ejemplo'
e = Ejemplo()
# Imprimir el objetosss
print ("El objeto creado es: " ,e)
print ("\nSi llamo el atributo privado --> 'e.__atributo_privado' --> lanza el siguiente error:")
print ("AttributeError: 'Ejemplo' object has no attribute '__atributo_privado'")
print (" ")
print ()

print ("\nSi llamo el método privado --> 'e.__metodo_privado()' --> tambien lanza error:")
print ("AttributeError: 'Ejemplo' object has no attribute '__metodo_privado'")
print (" ")
print ()

print ("---")
print ("Cómo acceder:")
print ("""
	Internamente la clase sí puede acceder a sus atributos 
	y métodos encapsulados, el truco consiste en crear sus equivalentes "publicos":
	""")

class Ejemplo:
	__atributo_privado = "Soy un atributo inalcanzable desde fuera"
	
	def __metodo_privado(self):
		print("Soy un método inalcanzable desde fuera")
	
	def atributo_publico(self):
		return self.__atributo_privado
	
	def metodo_publico(self):
		return self.__metodo_privado()


e = Ejemplo()
print ("Atributo público:")
print(e.atributo_publico())

print ("\nMétodo público:")
# El metodo publico si se puede llamar así:
e.metodo_publico()


print ()
print ("---")
print ()