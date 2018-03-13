print ("\nEjemplo de implementación con Programación Estructurada:")
print ("""
clientes= [
    {'Nombre': 'Hector',  'Apellidos':'Costa Guzman',      'dni':'11111111A'},
    {'Nombre': 'Juan',    'Apellidos':'González Márquez',  'dni':'22222222B'},
    {'Nombre': 'Manuel',  'Apellidos':'Garcia Perez',	   'dni':'33333333C'},
    {'Nombre': 'Ricardo', 'Apellidos':'Aparicio',		   'dni':'44444444D'} 
]
	""")
clientes= [
    {'Nombre': 'Hector',  'Apellidos':'Costa Guzman',      'dni':'11111111A'},
    {'Nombre': 'Juan',    'Apellidos':'González Márquez',  'dni':'22222222B'},
    {'Nombre': 'Manuel',  'Apellidos':'Garcia Perez',	   'dni':'33333333C'},
    {'Nombre': 'Ricardo', 'Apellidos':'Aparicio',		   'dni':'44444444D'} 
]
print ("\nMostrar el diccionario Clientes:")
print (clientes)
print ()

# Crear función para mostrar cliente
def mostrar_cliente(clientes, dni):
	for c in clientes:											# Recorra cada cliente en 'clientes'
		if (dni == c['dni']):									# Si el dni ingresado está en el diccionario
			print('{} {}'.format(c['Nombre'],c['Apellidos']))	# Mostrar nombres y apellidos del cliente
			print ("---")
			return												# Acaba la función con 'return' vacío
	print ('Cliente no encontrado')
	print ("-END of function mostrar_cliente(clientes,dni)-")
	print ("---")

# llamado a la función
print ("\nMostrar el diccionario Clientes llamando la función: mostrar_cliente(clientes,dni)")
print ("--> mostrar_cliente(clientes, '11111111A')")
mostrar_cliente(clientes, '11111111A')

print ()
print ("Crear función: borrar_cliente(clientes, dni):")

def borrar_cliente(clientes, dni):
	for i,c in enumerate(clientes):				# Por cada indice y valor en clientes:
		if (dni == c['dni']):					# Si el dni ingresado es igual al de algún cliente guardado
			del( clientes[i] )					# elimine el indice asociado en el diccionario 'clientes'
			print(str(c),"> BORRADO")			# Imprima el nombre del cliente que fue borrado
			print ()
			return								# Acaba la función con 'return' vacío
	print('Cliente no encontrado')
	print ("---")
	print ()

print ("\nllamar función de borrado:")
print ("--> borrar_cliente(clientes, '31313131')")
borrar_cliente(clientes, '31313131')

print ("\nllamar función de borrado:")
print ("--> borrar_cliente(clientes, '22222222B')")
borrar_cliente(clientes, '22222222B')

print ()
print ("Mostar los clientes guardados:")
print (clientes)
print ()

print ("""

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	""")


print ("\nEjemplo de implementación con Programación Orientada a Objetos:")
print ("Crear clase Cliente con su constructor, clase Empresa con su constructor y métodos:")

class Cliente:													# Crear clase 'Cliente'

	def __init__(self, dni, nombre, apellidos):					# Crear constructor con atributos para cada 'cliente'
		self.dni = dni
		self.nombre = nombre
		self.apellidos = apellidos
	
	def __str__(self):											# Redefinir la función String
		return '{} {}'.format(self.nombre,self.apellidos)		# return con nombre y apellidos del cliente
	

class Empresa:										# Crear clase 'Empresa'
	
	def __init__(self, clientes=[]):				# Crear constructor, donde se pasa una lista de clientes
		self.clientes = clientes 					# 
	
	def mostrar_cliente(self, dni=None):			# función para mostrar algún cliente
		for c in self.clientes:						# itera sobre los clientes guardados
			if c.dni == dni:						# si el 'dni' ingresado coincide con el guardado
				print(c)							# lo muestra
				return								# si lo encontró, return vacío para salir de la función
		print("Cliente no encontrado")				# indicar si el cliente no está guardado
	
	def borrar_cliente(self, dni=None):				# función para borrar alǵun 'cliente'
		for i,c in enumerate(self.clientes):		# recorre por indice/cliente en clientes
			if c.dni == dni:						# si el dni buscado coincide con alguno guardado
				del(self.clientes[i])				# elimina el cliente en mención
				print(str(c),"> BORRADO")			# mostrar nombre del cliente eliminado
				return
		print("Cliente no encontrado")

# Crear objetos de tipo 'Cliente' llamando la clase 'Cliente'
# Se puede indicar o no el atributo que se está ingresando:
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
pedro  = Cliente(nombre="Pedro",  apellidos="Garcia Lopez", dni="22222222B")
carlos = Cliente(nombre="Carlos", apellidos="Zea Ramirez",  dni="33333333C")

print ("\nMostrar clientes con: print(hector)...")
print (hector)
print (pedro)
print (carlos)
print ()

print ("\nCrear otro cliente:")
# Se puede indicar o no el atributo que se está ingresando:
juan = Cliente("44444444D", "Juan", "Gonzalez Marquez")

print (juan)
print ()

# Puedo crear la lista de clientes para pasarla como argumento durante la creación de los objetos de tipo Empresa:
clientes=[hector, pedro, carlos, juan]
# De este modo se crea el objeto 'empresa' del tipo 'Empresa', pasando como argumento la lista de clientes:
empresa = Empresa(clientes)

# O pasar la lista creandola a la vez
# De este modo se crea el objeto 'empresa' del tipo 'Empresa', pasando como argumento la lista de clientes:
# empresa = Empresa(clientes=[hector, juan])


# empresa = Empresa(clientes=[hector, juan])

print ("\nSi llamo el objeto creado llamado 'empresa' --> print (empresa.clientes): Lanza error:")
print (empresa.clientes)
print ()

print ("\nPara mostrar el objeto 'empresa' y un cliente específico, pasar el dni:")
print ('--> empresa.mostrar_cliente("11111111A")')
print (empresa.mostrar_cliente("11111111A"))
print ()

print ("\nPara borrar un objeto de tipo 'cliente', llamar el método pasándole el dni:")
print ('---> empresa.borrar_cliente("22222222B")')
empresa.borrar_cliente("22222222B")
print ()

print ("--> print (empresa.clientes)")
print (empresa.clientes)
print ()
