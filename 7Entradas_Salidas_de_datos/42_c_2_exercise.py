import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error - Número es incorrecto")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        # Aqui va la lógica
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print( "{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i ))

else:
    print ("\n***************************************************")
    print ("Error, introduce los 2 argumentos:")
    print ("Ejemplo: nombre_del__script.py     'numero entero1'")
    print ("Ejemplo: python 42_c_2_exercise.py '5'             ")
    print ("***************************************************")
    print ()
