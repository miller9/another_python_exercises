print ("""

Provocando errores:

Errores de sintaxis (SyntaxError)
Son los que podemos apreciar repasando el código, por ejemplo al dejarnos de cerrar un paréntesis:
	""")
print ('--> print("Hola"')
print ("SyntaxError: unexpected EOF while parsing")

print ("""\n
Errores de nombre (NameError):
Se producen cuando el sistema interpreta que debe ejecutar alguna función, método... pero no lo encuentra definido:
	""")
print ('--> pint("Hola")')
print ("NameError: name 'pint' is not defined")

print ("""\n
La mayoría de errores sintácticos Python los identifica antes de ejecutar el código 
y nos avisa que debemos arreglarlos.
Sin embargo existen otro tipo de errores que pasan más desapercibidos...
	""")

print ("""\n
Los errores semánticos:
Son muy difíciles de identificar, ya que van ligados al sentido del funcionamiento y dependen de la situación. 
Algunas veces pueden ocurrir y otras no.
Cuanta más experiencia como programador tengas, y más te hayas equivocado, 
más aprenderás a avanzarte a los errores semánticos.
	""")
print ("Ejemplo pop() con lista vacía:")
print ("Tengo una lista con x elementos, ej: l = [1,2,3]")
print ("Si uso la función 'l.pop()' y la lista está vacía, se lanza el error: 'pop from empty list'")
print ("IndexError: pop from empty list")
l = [1,2,3]
# l.pop()
# l.pop()
# l.pop()
print ("\nPara evitar el error, validar antes si la lista tiene por lo menos 1 elemento:")
print ("Prevención utilizando comprobación con len() > 0:")
l = [1,2,3]
if len(l) > 0:
	l.pop()
#l.pop()

print ()
print ("\nEjemplo lectura de cadena por teclado y operación de resultado sin conversión a número:")
print ("lanzaría error porque no se puede operar string con int:")
print ('	n = input("Introduce un número: ")	')
print ('	m = 4')
print ('	print("{}/{}={}".format(n,m,n/m))')

# m=4
# n = input("Introduce un número: ")
# print("{}/{}={}".format(n,m,n/m))
print ("TypeError: unsupported operand type(s) for /: 'str' and 'int'")

print ()
print ("\nPrevención haciendo una conversión a flotante:")
print ("si se ingresa un numero, se realiza la división sin problema")
print ("si se ingresa una cadena, lanzaría error porque no se puede operar string con float")
print ('	ValueError: could not convert string to float: "asd"	')
print ('	n = float(input("Introduce un número: "))	')
print ('	m = 4')
n = float(input("Introduce un número: "))
m = 4
print("{}/{}={}".format(n,m,n/m))

print ()
print ("\nSin embargo en algunas ocasiones no podemos prevenir el error, como cuando se introduce una cadena:")
print ("Para prevenir estos casos existen las excepciones")
print ()
print ()