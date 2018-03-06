print ("""
	3) Crea un script llamado descomposicion.py que realice las siguientes tareas:

    Debe tomar 1 argumento que será un número entero positivo.
    En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... 
tal que por ejemplo si se introduce el número:

> 3647

El programa deberá devolver una descomposición línea a línea como la siguiente utilizando 
las técnicas de formateo:

> 0007
  0040
  0600
  3000

Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. 
Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, 
números y viceversa

	""")
import sys
if (len(sys.argv)==2):
	print ("\nLos argumentos ingresados son: ",(sys.argv))
	cad1=str(sys.argv[1])
	print ("cad1 es: ",cad1)
	for caracter in cad1:
		ent1=int(cad1)
		last=ent1
		print("{:04d}".format(10))

else:
	print ("""\n Debe ingresar 2 argumentos:
		1. Nombre del script
		2. Un numero entero positivo""")
