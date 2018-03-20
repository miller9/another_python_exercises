import pandas as pd

print ("""
	After the import command, we now have access to a large number of pre-built classes and functions. 
	This assumes the library is installed, in our lab environment all the necessary libraries are installed. 
	One way pandas allows you to work with data is a dataframe. Let's go through the process to go 
	from a  comma separated values (**.csv** ) file to a dataframe. This variable **csv_path** stores 
	the path of the  **.csv** , the is  used as an argument to the **read_csv** function. 
	The result is stored in the object ** df**, this is short for dataframe.
""")

csv_path='https://ibm.box.com/shared/static/keo2qz0bvh4iu6gf5qjq4vdrkt67bvvb.csv'
df = pd.read_csv(csv_path)

# we can use the method head() to examine the first five rows of a dataframe:
df.head()

# The process for loading an excel file is similar, 
# we use the path of the excel file and the function read_excel. 
# The result is a data frame as before:

	#dependency  needed to install file 
	# !pip install xlrd

print ()
xlsx_path='https://ibm.box.com/shared/static/mzd4exo31la6m7neva2w45dstxfg5s86.xlsx'
df = pd.read_excel(xlsx_path)
print (df.head())


# We can access the column "Length" and assign it a new dataframe x:
x=df[['Length']]
print ()
print (x)

print ()
print ("""
	Viewing Data and Accessing Data:
""")


# You can also assign the value to a series, 
# you can think of a Pandas series as a 1-D dataframe. Just use one bracket:
x=df['Length']
print ()
print (x)

# You can also assign different columns, for example, we can assign the column 'Artist' :
x=df[['Artist']]
print ()
print (x)


# Assign the variable q to the dataframe that is made up of the column 'Rating':
q=df[['Rating']]
print ()
print (q)

# You can do the same thing for multiple columns; 
# we just put the dataframe name, in this case, 
# df and the name of the multiple column headers enclosed in double brackets. 
# The result is a new dataframe comprised of the specified columns:
y=df[['Artist','Length','Genre']]
print ()
print (y)

print ()
print (df[['Album','Released','Length']])

# Assine the variable q to the dataframe that is made up of the column 'Released' and 'Artist':
q=df[['Released','Artist']]
print ()
print (q)

print (""" One way to access unique elements is the ix method, 
	 you can access the 1st row and first column as follows :""")

print ()
print (df.ix[0,0])


# You can access the 2nd row and first column as follows:
print ()
print (df.ix[1,0])

# you can access the 1st row 3rd column as follows:
print ()
print (df.ix[0,2])

# Access the 2nd row 3rd column:
print ()
print (df.ix[1,2])

# you can access the column using the name as well,the following are the same as above:
print ()
print (df.ix[0,'Artist'])
print (df.ix[1,'Artist'])
print (df.ix[0,'Released'])
print (df.ix[1,'Released'])
print (df.ix[1,2])


# you can perform slicing using both the index and the name of the column:
print ()
print (df.ix[0:2, 0:3])

print (df.ix[0:2, 'Artist':'Released'])

print ()
print ('---')
print ()
































