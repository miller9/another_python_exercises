def b():
	print ("""
	2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. 
	Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

	El caballero tiene el doble de vida y defensa que un guerrero.
	El guerrero tiene el doble de ataque y alcance que un caballero.
	El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
	Muestra como quedan las propiedades de los tres personajes.
	
		caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
		guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
		arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }

	""")
	print ("---")
	print ()
	# Creo los diccionarios para cada tipo de personaje
	p_caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
	p_guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
	p_arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }
	# Lista para almacenar los diccionarios con cada tipo de personaje
	personajes = []
	personajes.append(p_caballero)
	personajes.append(p_guerrero)
	personajes.append(p_arquero)
	print ("Los personajes	:", personajes)
	# Ajustar los personajes
	print ()
	p_caballero['vida']	= ( p_guerrero['vida']*2 )
	p_caballero['defensa']	= ( p_guerrero['defensa']*2 )
	p_guerrero['ataque']	= ( p_caballero['ataque']*2)
	p_guerrero['alcance']	= ( p_caballero['alcance']*2)
	p_arquero['vida']	= ( p_guerrero['vida'] )
	p_arquero['ataque']	= ( p_guerrero['ataque'] )
	p_arquero['defensa']	= ( p_guerrero['defensa']/2 )
	p_arquero['alcance']	= ( p_guerrero['alcance']*2 )
	print ("Los personajes	:", personajes)
	print ()
# 	Ciclo para recorrer y ajustar los personajes
#	for c,v in personajes:
#		if (c==p_caballero and ):
#			print (c,v)

b()



