# Cesar Metod to encrypt and decrypt messages


def cesar_encrypt(n,message):
	abc_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']  
	temp = '?'
	msn_to_encrypt = ""
	i = 0
	# j = 0
	while i < len(message):
		if (message[i] in abc_list):
			temp = message[i]
			x = 0
			while x < len(abc_list):
				if (temp == abc_list[x]):
					msn_to_encrypt += abc_list[( x + n ) % 27]
					temp = ''
				else:
					x += 1
		else:
			# j += 1
			msn_to_encrypt += message[i]
		i += 1
	print ("\nThe crypted message is:", msn_to_encrypt)


def cesar_decrypt(n,message):
	abc_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']  
	temp = '?'
	decrypted_msn = ""
	i = 0
#	j = 0
	while i < len(message):
		if (message[i] in abc_list):
			temp = message[i]
			x = 0
			while x < len(abc_list):
				if (temp == abc_list[x]):
					decrypted_msn += abc_list[( x - n ) % 27]
					temp = ''
				else:
					x += 1
		else:
		#	j += 1
			decrypted_msn += message[i]
		i += 1
	print ("\nThe decrypted message is:", decrypted_msn)


while True:
	print ("\n***Cesar Metod***")
	print ("""\nSelect what you want do do:
		1: Encrypt a message
		2: Decrypt a message
		3. Exit
		""")
	option=int(input())
	if option == 1:
		print ("\n---")
		print ("You choose to encrypt:")
		n = int( input("Enter the 'key' value to encrypt --> number between 0 and 27: ") )
		message = str( input("Enter the message to encrypt: ") )
		cesar_encrypt(n,message)
		print ("---")

	elif option == 2:
		print ("\n---")
		print ("You choose to decrypt:")
		n = int( input("Enter the 'key' value to decrypt --> number between 0 and 27: ") )
		message = str( input("Enter the message to encrypt: ") )
		cesar_decrypt(n,message)
		print ("---")

	elif option == 3:
		print ("\n---")
		print ("Bye!")
		break
print ("---")
print ()


