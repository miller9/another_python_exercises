print ("""

	18. A pangram is a sentence that contains all the letters 
	of the English alphabet at least once, for example: 
	"The quick brown fox jumps over the lazy dog". 
	Your task here is to write a function to check a sentence to see if it is a pangram or not.
	
	Examples of pangrams:


	""")

def is_pangram():

	abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	new_abc=[]
	sentence = str(input("Please enter the sentence to find if it's a pangram or not: "))
	for c in sentence:
		if c in abc and c not in new_abc:
			new_abc.append(c)

	if len(abc) == len(new_abc):
		print ("\nIts a pangram! :)")
		print ()
	else:
		print ("\nIt's not a pangram :(")
		print ()


is_pangram()