print ("""
Las excepciones:

Son bloques de código excepcionales que nos permiten continuar con la ejecución 
de un programa pese a que ocurra un error.

Siguiendo con el ejemplo de la lección anterior
Teníamos el caso en que leíamos un número por teclado, pero el usuario no introducía un número:

	""")


print ("\nSi se ingresa un numero, se realiza la división sin problema")
print ("si se ingresa una cadena, lanzaría error porque no se puede operar string con float")
print ('	ValueError: could not convert string to float: "asd"	')
print ('	n = float(input("Introduce un número: "))	')
print ('	m = 4')
print ('	print("{}/{}={}".format(n,m,n/m))')

# n = float(input("Introduce un número: "))
# m = 4
# print("{}/{}={}".format(n,m,n/m))


print ()
print ("""\nCreando la excepción - Bloques try y except:
Para prevenir el error, debemos poner el código propenso a error dentro de un bloque try 
y luego encadenaremos un bloque except para tratar la excepción:
	""")
try:
	n = float(input("Introduce un número: "))
	m = 4
	print("{}/{}={}".format(n,m,n/m))
	print ()
except:
	print("Ha ocurrido un error, introduce bien el número")


print ()
print ("""\n
Utilizando un while(true), podemos asegurárnos de que el usuario introduce bien el valor
Repitiendo la lectura por teclado hasta que lo haga bien, y entonces rompemos el bucle con un break:
	""")
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
        print ()
        break  # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")


print ()
print ("""\n
Bloque else en excepciones:
Es posible encadenar un bloque else después del except para comprobar el caso en que todo funcione correctamente (no se ejecuta la excepción).
El bloque else es un buen momento para romper la iteración con break si todo funciona correctamente:
	""")
while(True):
	try:
		n = float(input("Introduce un número: "))
		m = 4
		print("{}/{}={}".format(n,m,n/m))
	except:
		print("Ha ocurrido un error, introduce bien el número")
	else:
		print("Todo ha funcionado correctamente")
		break  # Importante romper la iteración si todo ha salido bien


print ()
print ("""
Bloque finally en excepciones:
Por último es posible utilizar un bloque finally que se ejecute al final del código, ocurra o no ocurra un error:
	""")
while(True):
	try:
		n = float(input("Introduce un número: "))
		m = 4
		print("{}/{}={}".format(n,m,n/m))
	except:
		print("Ha ocurrido un error, introduce bien el número")
	else:
		print("Todo ha funcionado correctamente")
		break  # Importante romper la iteración si todo ha salido bien
	finally:
		print("Fin de la iteración") # Siempre se ejecuta

print ()
print ()






