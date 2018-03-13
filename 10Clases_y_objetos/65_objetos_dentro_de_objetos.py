print ("Objetos dentro de objetos:")

# Crear clase Pelicula
class Pelicula:
	
	# Constructor de clase
	def __init__(self, titulo, duracion, lanzamiento):
		self.titulo = titulo
		self.duracion = duracion
		self.lanzamiento = lanzamiento
		print('Se ha creado la película:',self.titulo)
	
	def __str__(self):
		return '{} ({})'.format(self.titulo, self.lanzamiento)


print ("---")

print ("\nCreando un catálogo de películas:")
print ("Crear clase 'Catalogo' con métodos constructor, agregar(p) y mostrar():")

# Crear la clase Catalogo
class Catalogo:
	
	peliculas = []  # Esta lista contendrá objetos de la clase Pelicula
	
	def __init__(self,peliculas=[]):
		self.peliculas = peliculas
	
	def agregar(self,p):  # p será un objeto Pelicula
		self.peliculas.append(p)
	
	def mostrar(self):
		for p in self.peliculas:
			print(p)  # Print toma por defecto str(p) --> Redefinido en la clase Pelicula

# Crear objeto 'p' del tipo 'Pelicula'
p = Pelicula("El Padrino",175,1972)
# Crear objeto 'c' del tipo 'Catalogo' pasándole como argumento la 'pelicula' creada
c = Catalogo([p])

print ()
print ("\nAl invocar el método: mostrar():")
c.mostrar()

print ("\nTambién puedo añadir una pelicula directamente:")
print ('Así: c.agregar(Pelicula("El Padrino: Parte 2",202,1974))')
c.agregar(Pelicula("El Padrino: Parte 2",202,1974))  # Añadimos una película directamente

print ("\nLa pelicula se agrega al Catalogo y se puede consultar con el método mostrar():")
c.mostrar()
print ()

