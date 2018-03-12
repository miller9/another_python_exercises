print ("\nEjemplo de implementación con Programación Estructurada:")
print ("""
clientes= [
    {'Nombre': 'Hector',  'Apellidos':'Costa Guzman',      'dni':'11111111A'},
    {'Nombre': 'Juan',    'Apellidos':'González Márquez',  'dni':'22222222B'} 
]
	""")
clientes= [
    {'Nombre': 'Hector',  'Apellidos':'Costa Guzman',      'dni':'11111111A'},
    {'Nombre': 'Juan',    'Apellidos':'González Márquez',  'dni':'22222222B'} 
]
print ("\nMostrar el diccionario Clientes:")
print (clientes)
print ()

# Crear función para mostrar cliente
def mostrar_cliente(clientes, dni):
	for c in clientes:
		if (dni == c['dni']):
			print('{} {}'.format(c['Nombre'],c['Apellidos']))
			print ("---")
			return
	print('Cliente no encontrado')
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
			return
	print('Cliente no encontrado')
	print ("---")
	print ()

print ("\nllamar función de borrado:")
print ("--> borrar_cliente(clientes, '31313131')")
borrar_cliente(clientes, '31313131')

print ("\nllamar función de borrado:")
print ("--> borrar_cliente(clientes, '22222222B')")
borrar_cliente(clientes, '22222222B')

