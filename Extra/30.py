print ('''

	## Higher order functions and list comprehensions:

	30. Represent a small bilingual lexicon as a Python dictionary in the following fashion 
	{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} 
	and use it to translate your Christmas cards from English into Swedish. 
	Use the higher order function `map()` to write a function `translate()` 
	that takes a list of English words and returns a list of Swedish words.

	''')

def translate(english_list):

	print ('hi')
	b_lexicon = { 'merry': 'god', 'christmas': 'jul', 'and': 'och', 'happy': 'gott', 'new': 'nytt', 'year': 'år' }
	for word in b_lexicon:
		print (word)
		swedish_list = list(map(lambda x: english_list in b_lexicon, english_list)
	


c_list = ['merry', 'christmas', 'and', 'happy', 'new', 'year']
translate(c_list)
