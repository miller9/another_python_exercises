import sys						# Importar libreria del sistema
if (len(sys.argv)==3):			# Si los parametros pasados corresponden a 3, entonces ejecute:
	texto = sys.argv[1]			# Asigno a texto lo que le pasaré al primer argumento 
	repeticiones = int(sys.argv[2])	#Convertir la cadena a entero y pasarla como argumento
	for r in range(repeticiones):
		print (texto)				#Texto a repetir r veces
# Ejecutar en terminal--> python 40Scripts_b.py "hola" 5	--> Imprimiría "hola" 5 veces
# Si no se pasan los argumentos, lanza error.
else:
	print ("\nError, introduce los argumentos correctamente")
	print ("Ejemplo: nombre_del__script.py 'texto' cantidad")
	print ("Ejemplo: python 40Scripts_b.py 'hola' 5")
	print ()