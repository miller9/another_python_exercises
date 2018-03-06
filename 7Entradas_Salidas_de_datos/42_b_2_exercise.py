import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print ("\n*************************************")
        print("Error - Filas o columnas incorrectos")
        print("Ejemplo: tabla.py [1-9] [1-9]")
        print ("*************************************")
    else:
        # Aqui empieza la lógica
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" * ", end='')
    print ()
    print ("\nThis script prints a matrix full of asterix, with 2 arguments entered by you.")
    print ()

else:
    print ("\n******************************************************************")
    print ("Error, introduce los 2 argumentos de tipo entero")
    print ("Ejemplo: nombre_del__script.py   'numero entero1' numero entero2")
    print ("Ejemplo: python 42_b_exercise.py '5'              '3'")
    print ("******************************************************************")
    print ()