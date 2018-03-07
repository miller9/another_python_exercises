print ("""
3) Localiza el error en el siguiente bloque de código. 
Crea una excepción para evitar que el programa se bloquee
y además explica en un mensaje al usuario la causa y/o solución:

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
colores['blanco']
--> El programa no tiene una clave 'blanco', por ello se bloquea
--> Error que lanza = KeyError: 'blanco'
	""")

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
	colores['blanco']
except KeyError:
	print ("En el diccionario NO hay clave 'blanco', ingrese una clave válida:")
	print ("Claves válidas: 'rojo', 'verde', 'negro'.")

print ()
print ()