import fnmatch
import os

def a():
	print ("---")
	images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
	matches = []

	for root, dirnames, filenames in os.walk('C:\"'):
		for extensions in images:
			for filename in fnmatch.filter(filenames, extensions):
				matches.append(os.path.join(root, filename))

	print ("Matches are: ",matches)
	print ("---")

a()
