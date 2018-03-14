print ("""

	1. Crea una clase llamada Punto con sus dos coordenadas X e Y.
	2. Añade un método constructor para crear puntos fácilmente. 
		Si no se reciben una coordenada, su valor será cero.
	3. Sobreescribe el método string, para que al imprimir por 
		pantalla un punto aparezca en formato (X,Y)
	4. Añade un método llamado cuadrante que indique a 
		qué cuadrante pertenece el punto, o si es el origen.
	5. Añade un método llamado vector, que tome otro punto 
		y calcule el vector resultante entre los dos puntos.
	6. (Optativo) Añade un método llamado distancia, que tome otro punto 
		y calcule la distancia entre los dos puntos y la muestre por pantalla.

	""")


import math
class Punto:

	# Constructor que crea por defecto Punto en el origen (0,0)
	def __init__(self, coord_x=0, coord_y=0):
		self.x = coord_x
		self.y = coord_y
	
	def __str__(self):
		# return 'La Coordenada es: ({},{})'.format(self.x, self.y)
		return "({}, {})".format(self.x, self.y)

	def cuadrante(self):
		if (self.x == 0 and self.y == 0):
			return 'El Punto: ({} {})'.format(self.x, self.y),' es el Origen!'
		elif (self.x > 0 and self.y > 0):
			return 'El Punto: ({} {})'.format(self.x, self.y),' pertenece al Primer Cuadrante.'
		elif (self.x < 0 and self.y > 0):
			return 'El Punto: ({} {})'.format(self.x, self.y),' pertenece al Segundo Cuadrante.'
		elif (self.x < 0 and self.y < 0):
			return 'El Punto: ({} {})'.format(self.x, self.y),' pertenece al Tercer Cuadrante.'
		elif (self.x > 0 and self.y < 0):
			return 'El Punto: ({} {})'.format(self.x, self.y),' pertenece al Cuarto Cuadrante.'

	def vector(self, punto):
		print("El vector entre {} y {} es ({}, {})".format(self, punto, punto.x - self.x, punto.y - self.y) )
		print ()

	def distancia(self, punto):
		print ("La distancia entre {} y {} es:".format(self,punto))
		print (math.sqrt( (punto.x-self.x)**2 + (punto.y-self.y)**2 ) )


print ("""

	7. Crea una clase llamada Rectangulo con dos puntos 
		(inicial y final) que formarán la diagonal del rectángulo.
	8. Añade un método constructor para crear ambos puntos fácilmente, 
		si no se envían se crearán dos puntos en el origen por defecto.
	9. Añade al rectángulo un método llamado base que muestre la base.
	10. Añade al rectángulo un método llamado altura que muestre la altura.
	11. Añade al rectángulo un método llamado area que muestre el area.

	""")

class Rectangulo:
	
	def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
		self.pInicial = punto_inicial
		self.pFinal = punto_final

	def base(self):
		self.base = abs(self.pFinal.x - self.pInicial.x)
		print("La base del rectángulo es {}".format( self.base ) )
	
	def altura(self):
		self.altura = abs(self.pFinal.y - self.pInicial.y)
		print("La altura del rectángulo es {}".format( self.altura ) )
	
	def area(self):
		self.base = abs(self.pFinal.x - self.pInicial.x)
		self.altura = abs(self.pFinal.y - self.pInicial.y)
		self.area = self.base * self.altura
		print("El área del rectángulo es {}".format( self.area ) )


print ("""

	12. Crea los puntos A(2,3), B(5,5), C(-3,-1) y D(0,0) e imprimelos por pantalla.
	13. Consulta a que cuadrante pertenecen el punto A, C y D.
	14. Consulta los vectores AB y BA.
	15. (Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
	16. (Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
	17. Crea un rectángulo utilizando los puntos A y B.
	18. Consulta la base, altura y área del rectángulo.

	""")

# Creo los objetos de la clase Punto con sus atributos (x,y)
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

print ("\n---")

# Imprimir los puntos creados, usando el método str que redefiní en la clase Punto
print ( str(A) )
print ( str(B) )
print ( str(C) )
print ( str(D) )

print ("---")
print ("\n---")

# Verificar a qué cuadrante pertenecen los puntos
print ( A.cuadrante() )
print ( B.cuadrante() )
print ( C.cuadrante() )
print ( D.cuadrante() )

print ("---")
print ("\n---")

# Consulta los vectores AB y BA
print ( A.vector(B) )
print ( B.vector(A) )

print ("---")
print ("\n---")

# Consulta la distancia entre los puntos 'A y B' y 'B y A', ByC, CyD
A.distancia(B)
B.distancia(A)
B.distancia(D)
C.distancia(D)

print ("---")
print ("\n---")

# Determinar cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)


A.distancia(D)
B.distancia(D)
C.distancia(D)


print ("---")
print ("\n---")


# Crea un rectángulo utilizando los puntos A y B
r = Rectangulo(A,B)


print ("---")
print ("\n---")


# Consulta la base, altura y área del rectángulo

r.base()
r.altura()
r.area()

print ("---")
print ("\n---")










