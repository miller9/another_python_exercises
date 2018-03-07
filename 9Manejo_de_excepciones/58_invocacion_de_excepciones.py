print ("""
Invocación de excepciones:
En algunas ocasiones quizá nos interesa llamar un error manualmente,
ya que un print común no es muy elegante:

	""")
def mi_funcion(algo=None):
    if algo is None:
        print("Error! No se permite un valor nulo (con un print)")

print ("si lanzo la función con argumento: 'mi_funcion('algo')' corre bien, pero...")        
mi_funcion("algo")
print ("si lanzo la función así, sin argumento: 'mi_funcion()' arroja un error:")
mi_funcion()


print ("""\n
La instrucción raise:
Gracias a raise podemos lanzar un error manual pasándole el identificador.
Luego simplemente podemos añadir un except para tratar esta excepción que hemos lanzado:
	""")
def mi_funcion(algo=None):
	try:
		if algo is None:
			raise ValueError("Error! No se permite un valor nulo")
	except ValueError:
		print("Error! No se permite un valor nulo (desde la excepción)")

# mi_funcion('asdas')	# de este modo, se ejecuta bien el programa
mi_funcion()			# de este modo, hay error por que no está el argumento, y lanza el error desde 'except'
print ()
print ()







