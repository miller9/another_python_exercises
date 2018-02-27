

#	4) A partir del ejercicio anterior, vamos a suponer que cada número es una nota, y lo que queremos es obtener la nota media. El problema #	es que cada nota tiene un valor porcentual:
#
#	La primera nota vale un 15% del total
#	La segunda nota vale un 35% del total
#	La tercera nota vale un 50% del total
#	Desarrolla un programa para calcular perfectamente la nota final.


def media2():

	print ("Please enter the first note: ")
	note_1 = float(input())
	print ("Please enter the second note: ")
	note_2 = float(input())
	print ("Please enter the third note: ")
	note_3 = float(input())

	media = ((note_1*0.15) + (note_2*0.35) + (note_3*0.50))
	print("The average note is: "+str(media))
	print ("--> This is another way to show values without casting:")
	print("--> The average note is: ", media)


media2()


