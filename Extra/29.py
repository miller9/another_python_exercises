print ('''

	## Higher order functions and list comprehensions:

	29. Using the higher order function `filter()`, define a function `filter_long_words()` 
	that takes a list of words and an integer n and returns the list of words that are longer than n.

	''')

import functools

def filter_long_words(list_1, n):

	ans = list(filter(lambda x: len(x) > n, list_1))
	print(ans)



words_list = ['milena', 'ana', 'caro', 'lucy', 'adriana', 'carmen', 'fernanda', 'maria']
filter_long_words(words_list, 5	)
