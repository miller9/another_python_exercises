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
	temp = ''
	ciphred_msn = ''
	for word in message:
		x = message.split()
		if (message[i] != ''):
			# temp = temp + message[i]
			ciphred_msn = ciphred_msn + message[1]
			print ('lista va en : ', ciphred_msn)
		else:
			i += 1
	
	print ('temp is: ', temp)
			# list_1.append()
	print ()
	print ('x is: ', x)

	print ('')




msn = "Apparently neutral’s protest is thoroughly discounted and ignored. \
	Isman hard hit. Blockade issue affects pretext for embargo on by-products, \
	ejecting suets and vegetable oils"
null_desencrypt(msn)
