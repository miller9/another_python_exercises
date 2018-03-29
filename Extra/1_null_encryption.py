print ('''

	--> Original message written during WW1:
	"Apparently neutral’s protest is thoroughly discounted and ignored. 
	Isman hard hit. Blockade issue affects pretext for embargo on by-products, 
	ejecting suets and vegetable oils"
	
	Extrayendo la segunda letra de cada palabra obtenemos el mensaje
	“Pershing sails from NY June 1”, Pershing, en referencia al comandante 
	en jefe de las fuerzas estadounidenses durante la Primera Guerra Mundial, 
	navega desde Nueva York el 1 de junio.

''')

def null_desencrypt(message):


	int_list = [ message[1] for x in message ]

	i = 0
	j = 0
	temp = ''
	ciphred_msn = ''
	x = message.split()
	for word in x:
		if (x[i] != ','):
			temp = temp + x[i][1]
		else: # (message[i] == ','):
			temp = temp + ' '
			a = ''
			a = temp[1]
			ciphred_msn = ciphred_msn + a
			temp = ''
			a = ''
		i += 1
	j += 1

	
	print ('temp is: ', temp)
			# list_1.append()
	print ()
	print ('x is: ', x)

	print ('')




msn = "Apparently neutral’s protest is thoroughly discounted and ignored. \
	Isman hard hit. Blockade issue affects pretext for embargo on by-products, \
	ejecting suets and vegetable oils"
null_desencrypt(msn)
