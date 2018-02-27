def textos():
	'Hola Mundo'	
	print ("Cadenas de caracteres: ")
	print ("Pueden ir en comillas simples o dobles:")
	a='Hola Mundo'
	b="Hola Mundo"
	print ("---")
	print ("En comillas simples: 	"+a)
	print ("En comillas dobles: 	"+b)
	t1 = 'Este texto incluye unas " " '
	print (t1)
	t2 = "Esta 'palabra' se encuentra escrita entre comillas simples"
	print (t2)
	t3 = "Texto que tiene \"comillas dobles\" dentro."
	print (t3)
	t4 = 'Texto que tiene \'comillas simples\' dentro.'
	print (t4)
	print ("---")
	print ("La función: print() Acepta carácteres especiales como las tabulaciones /t o los saltos de línea /n")
	print ("un texto \tuna tabulación")
	print("Un texto\nuna nueva línea")
	print ("---")
	print ("Para evitar los carácteres especiales, debemos indicar que una cadena es cruda (raw)")
	print("C:\nombre\directorio")
	print(r"C:\nombre\directorio")  # r => raw (cruda)
	print("Leer la cadena sin que PYTHON la interprete:")
	print(r"C:\nombre\directorio")	
	print ("---")
	print("Podemos utilizar """ "(triple comillas) para cadenas multilínea")
	print("Mostrar info en distintas líneas usando triple comillas:")
	print("""una línea
otra linea 
otra lineas más \tuna tabulación, 
	y otra línea identada, etc...""")
	print ("---")
	print("Usar las cadenas directamente o con -print-")
	c = "Esto es una cadena \ncon dos líneas (usando barraInvertida+n...)"
	print (c)
	print ("---")
	print ("Operaciones:")
	print ("Una de las operaciones de las cadenas es la concatenación (o suma de cadenas)")
	c + c
	print (c+c)
	print ("---")	
	s = "Una cadena" " compuesta de dos cadenas"
	print(s)
	print ("---")
	c1 = "Una cadena"
	c2 = "otra cadena"
	print("Una cadena " + c2)
	print ("---")	
	print ("También es posible utilizar la multiplicación de cadenas:")
	diez_espacios = " " *10
	print(diez_espacios + "algún texto después de los 10 espacios")
	print ("---")
	print("INDICES:")
	print("Acceder a carácteres específicos dentro de una cadena:")
	palabra = "Python"
	print("Imprimir el primer caracter de la palabra:")
	print (palabra[0]) # carácter en la posición 0
	print ("caracter ubicado en la posición 4: "+palabra[3])
	print ("---")
	print ("El índice negativo -1, hace referencia al carácter de la última posición, el -2 al penúltimo y así sucesivamente")
	print ("Último caracter de la palabra 		==> palabra[-1]: "+palabra[-1])
	print ("Penúltimo caracter de la palabra 	==> palabra[-2]: "+palabra[-2])
	print ("Antepenúltimo caracter de la palabra 	==> palabra[-3]: "+palabra[-3])
	print ("Primer caracter de la palabra 		==> palabra[-0]: "+palabra[-0])
	print ("Primer caracter de la palabra 		==> palabra[-6]: "+palabra[-6])
	print ("---")
	print("SLICING / SLICE en Python: --> Separar segmentos de una cadena:")
	print ("Es una capacidad de las cadenas que devuelve un subconjunto o subcadena utilizando dos índices [inicio:fin]:)")
	print ("El primer índice indica donde empieza la subcadena (se incluye el carácter).")
	print ("El segundo índice indica donde acaba la subcadena (se excluye el carácter).")
	print ("---")
	print("Imprimir los primeros 2 caractéres (el segundo índice no se incluye) ==> palabra[0:2]")
	print (palabra[0:2])
	print("Imprimir los primeros 2 caractéres con índices negativos (el segundo índice no se incluye) ==> palabra[-6:-4]")
	print (palabra[-6:-4])
	print("Imprimir desde el segundo caracter hasta el final --> incluye el final por defecto porque no se especificó: ==> palabra[2:]")
	print (palabra[2:])
	print ("---")
	print ("Concantenación + Slicing:")
	print("Imprimir desde inicio por defecto hasta caracter 3 y luego desde ahí hasta final por defecto: ==> palabra[:3] + palabra[3:]")
	print (palabra[:3] + palabra[3:])
	print ("---")
	print ("Si en el slicing no se indica un índice se toma por defecto el principio y el final (incluídos):")	
	print ("palabra[:]			==> "+palabra[:])
	print ("palabra[-2:] 			==> "+palabra[-2:])
	print ("palabra[:2] + palabra[2:]	==> "+palabra[:2] + palabra[2:])
	print ("palabra[-2:]			==> "+palabra[-2:])
	print ("Si un índice se encuentra fuera del rango de la cadena, dará error:")
	print ( "palabra[99]")
	print ("---")
	print ("Pero con slicing ésto no pasa y simplemente se ignora el espacio hueco:")
	print ("palabra[:99]	==> "+palabra[:99])
	print ("palabra[99:]	==> "+palabra[99:])
	print ("---")
	print ("Inmutabilidad:")
	print ("Las cadenas no se pueden modificar. Si intentamos reasignar un carácter, no nos dejará:")
	# Las cadenas de caractéres son inmutables --> No se puede asignar a una cadena un cambio de la siguiente forma:
	print ('NO SE PUEDE ==> palabra[0] = "N" --> Lanza error')
	print ("Sin embargo, utilizando slicing y concatenación podemos generar nuevas cadenas fácilmente:")
	print ("Concatenación correcta para cambiar un caracter de una cadena:")	
	palabra = "N" + palabra[1:]
	print ('palabra = "N" + palabra[1:] ==> '+palabra)
	print ("---")
	print("Imprime el tamaño de cualquier cadena: ")
	print ("len(palabra) ==> "+str(len(palabra)))


textos()






















