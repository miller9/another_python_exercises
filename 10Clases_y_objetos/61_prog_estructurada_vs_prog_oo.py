print ("Ejemplo de implementación con Programación Estructurada:")
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
pritn ("\nMostrar el diccionario Clientes:")
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
	print ("END")

# llamado a la función
mostrar_cliente(clientes, '11111111A')




