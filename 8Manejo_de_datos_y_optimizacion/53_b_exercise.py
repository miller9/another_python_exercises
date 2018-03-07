import math

print ("""
2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
Calcula el área de un círculo de 5 de radio:
areaCirculo=(radio**2)*pi

Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:

import math
print(math.pi)
> 3.1415...
	""")

def area_circulo(radio):
	return ((radio**2)*math.pi)

res=area_circulo(5)
print ("El área de un circulo con radio '5' es:",res)
print ()
