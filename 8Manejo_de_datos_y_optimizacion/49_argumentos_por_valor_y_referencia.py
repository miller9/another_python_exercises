print ("""
Paso por valor y paso por referencia:

	Paso por valor:		Se crea una copia local de la variable dentro de la función.
	Paso por referencia:	Se maneja directamente la variable, los cambios realizados dentro le afectarán también fuera.

Tradicionalmente, los tipos simples se pasan automáticamente por valor y los compuestos por referencia.

	Simples:	Enteros, flotantes, cadenas, lógicos...
	Compuestos:	Listas, diccionarios, conjuntos...
	""")

print("\nEjemplo paso por valor:")
def doblar_valor(numero):
    numero*=2
    
n = 10
print ("llamando la función: doblar_valor(n):	",doblar_valor(n))
print ("imprimiendo el valor de n:		",n)
print ()

print ("\nEjemplo paso por referencia:")
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
print ("imprimiendo la lista 'ns' antes de pasarlo como referencia:		",ns)
print ("llamando la función: doblar_valores(ns):				",doblar_valores(ns))
print ("imprimiendo el valor de 'ns' despues de pasarlo como referencia:	",ns)
print ()


print ("\nTrucos:")
print ("Para modificar los tipos simples podemos devolverlos modificados y reasignarlos:")
print ("Inicialmente 'n' vale 10, antes de llamar a la función doblar_valor(numero):",n)
def doblar_valor(numero):
    return numero*2
n = 10
n = doblar_valor(n)
print ("\nAsigno a 'n' el retorno de la función doblar_valor(numero):",n)
print ()

print ("\nY en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia:")
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2


ns = [10,50,100]
print ("valor de 'ns' antes de pasarlo:",ns)
print ("paso a 'ns' como parametro, para crear una copia y usando slicing --> doblar_valores(ns[:])")
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print ("valor de 'ns' despues de pasarlo:",ns)
print ()



