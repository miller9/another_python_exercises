print ("""
5) Realiza una función llamada recortar() que reciba tres parámetros. 
El primero es el número a recortar, 
el segundo es el límite inferior y 
el tercero el límite superior. 

La función tendrá que cumplir lo siguiente:
    Devolver el límite inferior si el número es menor que éste
    Devolver el límite superior si el número es mayor que éste.
    Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10

	""")

def recortar(a,b,c):
# a=numero a recortar
# b=limite inferior
# c=limite superior
	if a<b: return b
	if a>c: return c
	else: return a



print ("resultado:",recortar(15,0,10))
print ()



