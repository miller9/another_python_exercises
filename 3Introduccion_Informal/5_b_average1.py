
def media():
	
	print ("Please enter the first note: ")
	note_1 = int(input())
	print ("Please enter the second note: ")
	note_2 = int(input())
	print ("Please enter the third note: ")
	note_3 = int(input())

	average = (note_1 + note_2 + note_3)/3
	print("The average score is :", average)

print ("---")
print ("This function shows the average score: ")
print ("---")

media()
