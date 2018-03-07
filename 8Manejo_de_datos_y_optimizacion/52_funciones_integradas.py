print ()
print ("Funciones integradas comunes:")

print ("\nint(): Transforma una cadena a un entero (si no es posible da error):")
n = int("10")
n

print ("\nloat(): Transforma una cadena a un flotante (si no es posible da error):")
f = float("10.5")
f

print ("\nstr(): Transforma cualquier valor a una cadena:")
c = "Un texto y un número " + str(10) + " " + str(3.14)
print (c)

print ("\nbin(): Conversión de entero a binario:")
bin(10)
print ("Conversión de 10:",bin(10))

print ("\nhex(): Conversión de entero a hexadecimal:")
hex(10)
print ("Conversión de 10:",hex(10))

print ("\nint() con base: Reconversión de binario a entero (base 10):")
print (int('0b1010',2))

print ("\nint() con base: Reconversión de hexadecimal a entero (base 10):")
print (int('0xa',16))

print ("\nabs(): Valor absoluto de un número (distancia):")
print ("abs(-10):",abs(-10))
print ("abs(10)	:",abs(10))

print ("\nround(): Redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza:")
print ("Redondeo hacia arriba --> ",round(5.5))
print ("Redondeo hacia abajo  --> ",round(5.4))


print ("\neval(): Evalúa una cadena como una expresión, acepta variables si se han definido anteriormente:")
print ("eval('2+5'):",eval('2+5'))
n = 10
print ("\nn=10:")
print ("eval('n*10 - 5') ==> ",eval('n*10 - 5'))

print ("\nlen(): Longitud de una colección o cadena:")
print ('len("Una cadena"):',len("Una cadena"))
print ('len([]):',len([]))

print ("\nhelp(): Invocar el menú de ayuda del intérprete de Python:")
print ("help() --> invocarlo para validar opciones --> con jupyter hay que importarlo....")
print ()





