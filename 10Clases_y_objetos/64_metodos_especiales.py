print ("\nMétodos especiales de clase")
print ("Constructor y destructor:")
print ("Redefinición de los métodos str() y len():")


# Crear la clase con constructor, destructor, 
# redefiniendo los métodos string y len
class Pelicula:
	# Constructor de clase (se ejecuta al crear la instancia/el objeto)
	def __init__(self,titulo,duracion,lanzamiento):
		self.titulo = titulo
		self.duracion = duracion
		self.lanzamiento = lanzamiento
		print("Se ha creado la película",self.titulo)
	
	# Destructor de clase (al borrar la instancia/el objeto)
	# Este método se ejecuta automáticamente para borrar la instancia creada, 
	# en éste caso imprimiría un aviso en pantalla cada vez que sea creado un objeto.
	def __del__(self):
		print("Se está borrando la película", self.titulo)
	
	# Redefinimos el método string
	def __str__(self):
		return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)
	
	# Redefinimos el método length
	def __len__(self):
		return self.duracion

# Crear la instancia 'p' con sus 3 atributos	
# Al crearla se llama automáticamente el método 'init'    
p = Pelicula("El Padrino",175,1972)
len(p)



# Al reinstanciar la misma variable se crea de nuevo y se borra la anterior
print ("\nAl reinstanciar la misma variable se crea de nuevo y se borra la anterior:")
p = Pelicula("El Padrino",175,1972)


print ("\nMétodo String:")
print ("Ahora el método String se redefinió para retornar la duración, titulo y fecha de una película:")
print ("Al llamarlo --> str(p) obtengo:")
print (str(p))
print ()


print ("\nMétodo Length:")
print ("Para devolver un número que simula la longitud del objeto len(objeto):")
print ("Si llamo el método así --> len(p) lanza error porque el objeto de tipo 'Pelicula' no tiene dicho método:")
print ("--> len(p) --> arrojaría TypeError")
print ("Despues de redefinirlo para que devuelva la duración de una película si funciona:")
print ("La duración de la película es:" ,len(p))
print ()