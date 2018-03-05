from collections import deque
def cola_tareas():
	print ("""
	3) Durante la planificación de un proyecto se han acordado una lista de tareas. 
	Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

	Crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden.

	*Para ordenar automáticamente una lista es posible utilizar el método .sort().
	
	tareas = [ 
	[6, 'Distribución'],
	[2, 'Diseño'],
	[1, 'Concepción'],
	[7, 'Mantenimiento'],
	[4, 'Producción'],
	[3, 'Planificación'],
	[5, 'Pruebas']
	]	

	""")
	# Definir lista de sublistas --> En cada posición almacena dos elementos (orden + tarea)
	tareas = [ 
	[6, 'Distribución'],
	[2, 'Diseño'],
	[1, 'Concepción'],
	[7, 'Mantenimiento'],
	[4, 'Producción'],
	[3, 'Planificación'],
	[5, 'Pruebas']
	]
	# Imprimir matriz con Indice + Tarea (vertical)
	print("\n==Tareas desordenadas==")
	for tarea in tareas:
		print(tarea[0], tarea[1])
	
	# print (tareas)	# (horizontal)
		
	
	
	cola = deque(tareas)
#	print ("cola :", cola)
	
#	cola.append(['caray', 3])

#	print (cola)
#	cola.pop()	
	
	# Ordenar la lista de tareas
	tareas.sort()
	
	# Crear cola para añadir elementos	
	cola_t = deque()
	for tarea in tareas:
		cola_t.append(tarea[1])
	
	# Imprimir cola sin Indice, solo la Tarea
	print("\n==Tareas ordenadas==")
	for tarea in cola_t:
		print(tarea)

	print ("\n---")
	print ()

cola_tareas()











