"""
Expresiones anidadas

Se pueden solucionar empleando las reglas de precedencia:

    Primero los paréntesis porque tienen prioridad
    Segundo, las expresiones aritméticas por sus propias reglas
    Tercero, las expresiones relacionales
    Cuarto, las expresiones lógicas
"""
def exp_anid():
	print ("Variables a=10, b = 5")
	a=10
	b=5
	print ("Resultado de la expresión:")
	print ("a*b - 2**b >= 20 and not (a%b)!=0")
	print (a * b - 2**b >= 20 and not (a % b) != 0)
	print ("( ((a*b)-(2**b)>=20) and (not((a%b)!=0)) )")




exp_anid()




















