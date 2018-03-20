import matplotlib.pyplot as plt
# %matplotlib inline


class Circle(object):

	def __init__(self, radius=3, color='blue'):
	
		self.radius = radius
		self.color = color
	
	def add_radius(self, r):
	
		self.radius = self.radius + r
		return(self.radius)
	
	def drawCircle(self):
	
		plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
		plt.axis('scaled')
		plt.show()


# create the object RedCircle of type Circle:
RedCircle = Circle(10,'red')

# the dir command to get a list of the object's methods. Many of them are default Python methods:
dir(RedCircle)

# look at the data attributes of the object:
RedCircle.radius

# look at the data attributes of the object:
RedCircle.color

# change the object's data attributes:
RedCircle.radius = 1

RedCircle.radius

# draw the object by using the method drawCircle():
RedCircle.drawCircle()

# increase the radius of the circle by applying the method add_radius(). 
# Let increases the radius by 2 and then by 5:
print('Radius of object: ', RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2): ', RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5): ', RedCircle.radius)

# create a blue circle, as the default colour is blue all we have to do is specify what the radius is:
BlueCircle = Circle(radius=100)

# As before we can access the attributes of the instance of the class by using the dot notation:
BlueCircle.radius
BlueCircle.color

# draw the object by using the method drawCircle():
BlueCircle.drawCircle()

print ('Compare the x and y axis of the figure to the figure for RedCircle they are different...')
print ('---')
print ('---')
print ()


class Rectangle(object):
	
	def __init__(self, width=2, height=3, color='r'):
		self.height = height
		self.width = width
		self.color = color
	
	def drawRectangle(self):
		import matplotlib.pyplot as plt
		plt.gca().add_patch(plt.Rectangle((0, 0),self.width, self.height ,fc=self.color))
		plt.axis('scaled')
		plt.show()


# create the object SkinnyBlueRectangle of type Rectangle, 
# it’s width will be 2 and height will be 3 the color will be blue:
SkinnyBlueRectangle = Rectangle(2, 10, 'blue')

# As before we can access the attributes of the instance of the class by using the dot notation:
SkinnyBlueRectangle.height
SkinnyBlueRectangle.width
SkinnyBlueRectangle.color

# Draw the object:
SkinnyBlueRectangle.drawRectangle()



#  create the object “FatYellowRectangle” of type Rectangle:
FatYellowRectangle = Rectangle(20, 5, 'yellow')


FatYellowRectangle.height
FatYellowRectangle.width
FatYellowRectangle.color

FatYellowRectangle.drawRectangle()



print ('---')
print ('---')
print ()
































































