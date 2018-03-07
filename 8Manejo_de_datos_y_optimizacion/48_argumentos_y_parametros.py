print ("\nTrabajando con argumentos y parámetros:")

print ("\nArgumentos por posición:")
def resta(a,b):
	return a-b

resta(1,2)   # posición índice 0 valor 1, posición índice 1 valor 2
print ("Función resta: 1-2 =", resta(1,2))

print ("\nArgumentos por nombre:")
print ("resta(b=2,a=1)")
resta(b=2,a=1)
print ("La resta es: 1-2 =",resta(b=2,a=1))

print ("\nLlamada sin argumentos:")
print ("Al llamar una función que tiene definidos unos parámetros, si no pasamos los argumentos correctamente provocará un error:")
print ("resta() --> Lanzaría error porque no están los 2 parámetros requeridos")

print ("\nParámetros por defecto:")
print ("Para solucionarlo podemos asignar unos valores por defecto nulos a los parámetros, y de ésa forma podríamos hacer una comprobación antes de ejecutar el código de la función:")
def resta(a=None,b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b

resta(1,5)
print ("la resta es: 1-5 =", resta(1,5))
print ()