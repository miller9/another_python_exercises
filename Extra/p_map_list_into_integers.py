print ('''

	## Higher order functions and list comprehensions:

	27. Write a program that maps a list of words into a list of integers 
	representing the lengths of the corresponding words. 
	Write it in three different ways: 1) using a for-loop, 2) 
	using the higher order function `map()`, and 3) using list comprehensions.

	''')

def map_list_into_integers(list):

	print ('1rst way --> Using a \'for-loop\':')
	int_list = []
	i = 0
	for x in list:
		temp = list
		int_list[i] = len(temp)
		temp = ''
		i += 1
		# int_list += int ( len(list[k]) )

	print ('The list of integers is: ', int_list)


words_list = ['milena', 'ana', 'caro', 'lucy', 'adriana', 'carmen', 'fernanda']
map_list_into_integers(words_list)
