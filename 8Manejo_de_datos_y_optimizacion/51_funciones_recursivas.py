print ("""
Funciones recursivas:

Se trata de funciones que se llaman a sí mismas durante su propia ejecución. 
Funcionan de forma similar a las iteraciones, y debemos encargarnos de planificar 
el momento en que una función recursiva deja de llamarse o tendremos una función rescursiva infinita.

Suele utilizarse para dividir una tarea en subtareas más simples de forma que sea más fácil 
abordar el problema y solucionarlo.
	""")
print ("""\n
Ejemplo sencillo sin retorno:
Cuenta regresiva hasta cero a partir de un número:
	""")
def cuenta_atras(num):				# crear la función recursiva, que recibirá un parametro
	num -= 1						# el parametro recibido irá disminuyendo su valor en 1, por cada iteración/recursión
	if num > 0:						# condición a validar para que realice la recursión
		print(num)					# imprime el valor que se va almacenando en el parametro ingresado
		cuenta_atras(num)			# la función se llama a sí misma
	else:							# si el valor es == 0, terminó la cuenta atras y con ello, la recursión
		print("Boooooooom!")		# imprime un msn
	print("Fin de la función", num)	# imprime el valor que tiene cuando ha terminado la ejecución de toda la función

cuenta_atras(5)						# llamado de la función
print ()


print ("""\n
Ejemplo con retorno (factorial de un número):
El factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número:
    3! = 1 x 2 x 3 = 6
    5! = 1 x 2 x 3 x 4 x 5 = 120
	""")

def factorial(num):						# función recursiva que recibirá un parámetro
	print("Valor inicial ->",num)		# imprime el valor inicial del parámetro ingresado
	if num > 1:							# si el num es mayor a 1, hace el llamado recursivo
		num = num * factorial(num -1)	# va disminuyendo el valor de num en 1
	print("valor final ->",num)			# imprime el valor final de num, despues de ejecutar la función
	return num							# retorna el factorial del parámetro ingresado

factorial(5)
print ()
print ()
