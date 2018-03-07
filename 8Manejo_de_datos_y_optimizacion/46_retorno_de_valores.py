print ("""
	Retorno de valores:
	Para comunicarse con el exterior, 
	las funciones pueden devolver valores al proceso principal gracias a la instrucción return.
	En el momento de devolver un valor, la ejecución de la función finalizará:
	""")

def test1():
	return ("\nFUNCIÓN: Una cadena retornada")


test1() # Llamando la función así, trae el retorno de la misma pero no imprime nada

print ("Los valores devueltos se tratan como valores literales directos del tipo de dato retornado:")
print (test1())	# De este modo imprime lo que retorna

c = test1()	# puedo guardar en una variable el valor de retorno de alguna función
print (c)	# imprimir el valor guardado en la variable

print ("\nc = test() + 10	--> No se pueden operar enteros con strings")

def test2():
    print ("\nFUNCIÓN: Éso incluye cualquier tipo de colección:")
    return [1,2,3,4,5]
	
print(test2())

print ("\nImprimir el último elemento de la lista desde la llamada a la función:")
print ("print(test()[-1]): ",(test2()[-1]))

print ("\nO hacerle Slicing al resultado de la función:")
print ("print(test()[1:4]): ",(test2()[1:4]))

print ("""Retorno múltiple:
	Una característica interesante, es la posibilidad de devolver múltiples valores separados por comas.
	""")

def test3():
    return "Una cadena",20,[1,2,3]

test3()

print ("\nÉstos valores se tratan en conjunto como una tupla inmutable y se pueden reasignar a distintas variables:")
print ("c,n,l = test3()	--> De este modo, guardo cada valor del retorno en una variable separada")
c,n,l = test3()
print ("el valor de c:",c)
print ("el valor de n:",n)
print ("el valor de l:",l)
print ()






