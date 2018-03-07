print ("""
	Las funciones:
	Son fragmentos de código que se pueden ejecutar múltiples veces. 
	Pueden recibir y devolver información para comunicarse con el proceso principal.
	Definición y llamada
	""")


def saludar():
    print("\nFUNCIÓN: Hola! Este print se llama desde la función saludar()")


def dibujar_tabla_del_5():
	print ("\nDentro de una función podemos utilizar variables y sentencias de control:")
	print ("FUNCIÓN: Dibujar tabla del 5 usando format():")
	for i in range(10):
		print("5 * {} = {}".format(i,i*5))


def test():
	n = 10
	print ("\nÁmbito de las variables: Una variable declarada en una función no existe en la función principal:")
	print("FUNCIÓN: Si intento imprimir 'n' por fuera de la función, no lo hace porque la variable fue creada dentro")


m = 10
def test2():
	print ("\nSin embargo, una variable declarada fuera de la función (al mismo nivel), sí que es accesible desde la función:")
	print("FUNCIÓN: Valor de m:",m)

def test3():
	print ("\nSiempre que declaremos la variable antes de la ejecución, podemos acceder a ella desde dentro:")
	print("FUNCIÓN: Valor de l:",l)
#test()
l = 10


def test4():
	print ("""\nEn el caso que declaremos de nuevo una variable en la función, 
		se creará un copia de la misma que sólo funcionará dentro de la función.
		Por tanto no podemos modificar una variable externa dentro de una función:
		""")
	o = 5 # variable que sólo existe dentro de la función
	print("FUNCIÓN: Valor de o:",o)


def test5():
	print("""\nLa instrucción global: 
		Para poder modificar una variable externa en la función,
		debemos indicar que es global de la siguiente forma:
		""")
	global x # variable que hace referencia a la x externa
	x = 5
	print("FUNCIÓN: Valor de 'x' dentro de la función:",x)



saludar()
dibujar_tabla_del_5()
test()
test2()
test3()

#test4() # Este llamado lanzaría error porque la función
o=10 # variable externa, no modificable
test4()
print("\nValor de 'o' fuera de la función ==> Otra variable nombrada igual:",o)

test5()
x=10	# Asigno valor a x fuera de la función
test5()
print("\nValor de 'x' fuera de la función <==> Variable Global:",x)
print ()
