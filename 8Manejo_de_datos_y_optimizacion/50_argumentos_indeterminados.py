print ("""
Argumentos y parámetros indeterminados:

Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar a una función. 
En estos casos podemos utilizar los parámetros indeterminados por posición y por nombre.
	""")
print ("""
\nPor posición:
Para recibir un número indeterminado de parámetros por posición, 
debemos crear una lista dinámica de argumentos (una tupla en realidad):
	""")
def indeterminados_posicion(*args):				# *args ==> equivale a varios argumentos
	for arg in args:							# recorre cada argumento
		print(arg)								# imprime cada argumento de los que se pasaron a la funcion
    
indeterminados_posicion(5,"Hola",[1,2,3,4,5])
print ()

print ("""
Por nombre:
Para recibir un número indeterminado de parámetros por nombre (clave-valor),
debemos crear un diccionario dinámico de argumentos:
	""")
print ("\n# imprime un diccionario creado a partir de los argumentos pasados:")
def indeterminados_nombre(**kwargs):			# **kwargs ==> keyword args ==> equivale a pasar parametros clave/valor
	print(kwargs)

indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5]) # imprime un diccionario creado a partir de los argumentos pasados
print ()



print ("# imprime cada clave del diccionario:")
def indeterminados_nombre(**kwargs):			# **kwargs ==> keyword args ==> equivale a pasar parametros clave/valor
	for kwarg in kwargs:						# recorre cada kw=clave de los kwargs pasados
		print(kwarg)							# imprime cada clave del diccionario

indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5]) 
print ()



print ("# imprime cada clave  con su valor correspondiente:")
def indeterminados_nombre(**kwargs):			# **kwargs ==> keyword args ==> equivale a pasar parametros clave/valor
	for kwarg in kwargs:						# recorre cada kw=clave de los kwargs pasados
		print(kwarg," ", kwargs[kwarg])			# imprime cada clave  con su valor correspondiente 

indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])   
print ()

print ("""
Por posición y nombre a la vez:
Si queremos aceptar ambos tipos de parámetros simultáneamente, entonces debemos crear ambas colecciones dinámicas:
	""")
print ("Imprime los argumentos simples y los argumentos compuestos:")
def super_funcion(*args,**kwargs):		# recibe varios arg simples=*args y varios args compuestos=**kwargs==>clave/valor
	t = 0								# variable 'total', para hacer suma de los argumentos simples
	for arg in args:					# recorre cada argumento de los argumentos simples
		t+=arg 							# va sumando en t el valor de cada argumento simple
	print("Sumatorio indeterminado es",t)	#imprime el total de la suma de los argumentos simples
	for kwarg in kwargs:				# recorre cada argumento clave/valor de los kwargs=argumentos compuestos
		print(kwarg," ", kwargs[kwarg])	# imprime cada clave y su valor 

super_funcion(10,50,-1,1.56,10,20,300,nombre="Hector",edad=27)
print ()




