import sys								# Importar libreria del sistema
def b42tabla():
	print ("""
		2) Crea un script llamado tabla.py que realice las siguientes tareas:

		Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
		El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
		En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
		El script contendrá un bucle for que itere el número de veces del primer argumento.
		Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
		Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (end='' evita el salto de línea).
		Ejecuta el código y observa el resultado.

		Ahora intenta deducir dónde y cómo añadir otra instruccion print para dibujar una tabla.

		Recordatorio: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento". Para capturar los argumentos debes utilizar el módulo sys y su lista argv:

		import sys
		print(sys.argv) # argumentos enviados

		""")
if (len(sys.argv)==2):			# Si los parametros pasados corresponden a 3, entonces ejecute:
	if (sys.argv[1]>=1 and sys.argv[1]<=9):
		if (sys.argv[2]>=1 and sys.argv[2]<=9):
	texto = sys.argv[1]			# Asigno a texto lo que le pasaré al primer argumento 
	repeticiones = int(sys.argv[2])	#Convertir la cadena a entero y pasarla como argumento
	for r in range(repeticiones):
		print (texto)				#Texto a repetir r veces
	else:
		print ("Los 2 argumentos del sistema deben ser enteros entre 1 y 9, de nuevo por favor:")

# Ejecutar en terminal--> python 40Scripts_b.py "hola" 5	--> Imprimiría "hola" 5 veces
# Si no se pasan los argumentos, lanza error.
else:
	print ("\nError, introduce los argumentos correctamente")
	print ("Ejemplo: nombre_del__script.py 'texto' cantidad")
	print ("Ejemplo: python 40Scripts_b.py 'hola' 5")
	print ()










b42()