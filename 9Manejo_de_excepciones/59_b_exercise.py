print ("""
2) Localiza el error en el siguiente bloque de código.
Crea una excepción para evitar que el programa se bloquee 
y además explica en un mensaje al usuario la causa y/o solución:
	""")
# lista = [1, 2, 3, 4, 5]
# lista[10]

#solución:
print ('	lista = [1, 2, 3, 4, 5]')
print ('	lista[10]')
print ("	Se bloquea debido a que el array solo tiene 5 posiciones y la petición es para la posición 10")
print ('	Error que lanza = IndexError: list index out of range')
print ()

try:
	lista = [1, 2, 3, 4, 5]
	if (len(lista)>=1 and (len(lista)<=5)):
		x=int( input("Ingrese la posición que desea validar:") )
		print ("La posición '",x,"' almacena el valor:",lista[x])
except IndexError:
	print ("IndexError: list index out of range")
	print ("La posición a validar debe estar entre 0 y 4")

"""
lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error: El índice al que intentas acceder se encuentra fuera del rango, 
    debes utilizar un número mayor o igual que cero y menor que la longitud de la lista.")
"""
print ()
print ()