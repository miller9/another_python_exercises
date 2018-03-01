def media():
	print ("""
4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:	
	""")
	index=0
	temp=0
	media=0	
	value=(int(input("Please tell me how many numbers do you want to enter: ")))
	sum_values = [1] * value
	print ()
	while index<value:
			sum_values[index]=input("Please enter the value "+str((index+1))+": ",)
			temp = temp+int(sum_values[index])
			index+=1		
			media=temp/value
	print ()	
	print ("media is: ", media)
	print ()

media()
