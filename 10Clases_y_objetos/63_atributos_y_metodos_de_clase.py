print ("""
	Atributos y métodos de clase:

	Atributos: Hacen referencia a las variables internas de la clase.
	Métodos:   Hacen referencia a las funciones internas de la clase.


	""")

# Crear Clase 'Galleta'
class Galleta:
	pass

# Crear objeto 'una_galleta' del tipo: 'Galleta'
una_galleta = Galleta()


# Definición de atributos dinámicos en los objetos:
una_galleta.sabor = "Salado"
una_galleta.color = "Roja"
una_galleta.forma = "Redonda"
print ("\nEl sabor de ésta galleta es:" , una_galleta.sabor)
print ("El color de ésta galleta es:" , una_galleta.color)


# Definición de atributos en la clase:
# Creo la clase 'Galleta' y defino que el atributo 'chocolate' por defecto está en falso
print ("\nDefinir y cambiar los atributos de clase:")
class Galleta:
	chocolate = False

g = Galleta()
print ("La galleta tiene chocolate?" ,g.chocolate)

# Puedo cambiar los valores de los atributos para cada objeto por separado
g.chocolate = True
print ("La galleta tiene chocolate?" ,g.chocolate)
print ()


print ("\nMétodo init()")
print ("Se llama automáticamente al crear una instancia de clase:")
# Crear clase Galleta, atributo chocolate y método '__init__()'
class Galleta():
	chocolate = False
	def __init__(self):
		# Cada vez que se crea un objeto del tipo 'Galleta' imprime:
		print("Se acaba de crear una galleta.")
g = Galleta()
print ()


print("\nMétodos y la palabra self")
print ("""Self sirve para hacer referencia a los métodos y atributos base 
	de una clase dentro de sus propios métodos:""")
print ()

# Crear clase 'Galleta'
class Galleta():
	chocolate = False									# atributo de la clase
	
	def __init__(self):									# método init
		print("Se acaba de crear una galleta.")
	
	def chocolatear(self):								# método para los objetos de la clase 'Galleta'
		self.chocolate = True							# se puede cambiar el valor de un atributo
	
	def tiene_chocolate(self):							# método de la clase
		if (self.chocolate):							# imprime si el objeto tiene chocolate o no
			print("Soy una galleta chocolateada :-D")
		else:
			print("Soy una galleta sin chocolate :-(")
    
g = Galleta()				# crear objeto 'g'
g.tiene_chocolate()			# g no tiene chocolate
g.chocolatear()				# se modifica el atributo 'chocoalate' de 'g' y ahora si tiene chocolate
g.tiene_chocolate()			# g ahora tiene chocolate
print ()


print ("\nParámetros en el init (argumentos al instanciar):")
class Galleta():
	chocolate = False
	
	def __init__(self, sabor, forma):		# Se solicitan 2 argumentos para asignar a cada objeto que sea creado
		self.sabor = sabor					# atributo sabor
		self.forma = forma 					# atributo forma
		print("Se acaba de crear una galleta {} y {}".format(sabor,forma))
	
	def chocolatear(self):
		self.chocolate = True
	
	def tiene_chocolate(self):
		if (self.chocolate):
			print("Soy una galleta chocolateada :-D")
		else:
			print("Soy una galleta sin chocolate :-(")

# Se crea un objeto del tipo 'Galleta' llamado 'g' con 2 atributos: salada + cuadrada
g = Galleta("salada","cuadrada")

print (g)	# muestra la posición exacta que ocupa en la memoria
print ()



print ("\nParámetros con valores por defecto en el __init__():")
print ("No se puede crear un objeto sin pasarle los argumentos necesarios:")
print ("--> g = Galleta() --> Lanza error porque va sin los 2 args")

class Galleta():
	chocolate = False
	
	# Se le asigna por defecto 'None' a los 2 atributos de las galletas
	def __init__(self, sabor=None, forma=None):
		self.sabor = sabor
		self.forma = forma
		# Si las galletas tienen forma y sabor, las imprime
		if sabor is not None and forma is not None:
			print("Se acaba de crear una galleta {} y {}".format(sabor,forma))
	
	def chocolatear(self):
		self.chocolate = True
	
	def tiene_chocolate(self):
		if (self.chocolate):
			print("Soy una galleta chocolateada :-D")
		else:
			print("Soy una galleta sin chocolate :-(")


print ()
# Se crea un objeto del tipo 'Galleta' llamado 'g1' sin atributos
g1 = Galleta()

# Se crea un objeto del tipo 'Galleta' llamado 'g2' con 2 atributos: salada + cuadrada
g2 = Galleta("salada","cuadrada")
print()





