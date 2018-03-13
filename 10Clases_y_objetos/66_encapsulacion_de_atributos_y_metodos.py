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
print ("Porque ")
print ()