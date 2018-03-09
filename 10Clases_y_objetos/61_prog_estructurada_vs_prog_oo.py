print ("Ejemplo de implementación con Programación Estructurada")
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
print (clientes)
print ()

def mostrar_cliente(clientes, dni):
	for c in clientes:
		if (dni == c['dni']):
			print('{} {}'.format(c['Nombre'],c['Apellidos']))
			print ("---")
			return
        
	print('Cliente no encontrado')
	print ("END")

mostrar_cliente(clientes, '11111111A')
