class Dog():
	#Class Level Attributes 
	#Same for any Instance of a class
	species  = "Mamel"
	def __init__(self,name,age,branch):
		#Attributes
		#We Take In Arguement
		#Assign it using self.attribute_name
		self.name = name
		self.age = age
		self.branch = branch

	#Operation /Action---------->Methods
	def bark(self):
		print("WOOF! My Name Is {}".format(self.name))


mydog  = Dog(name = "Sundri",branch = "IT",age = "20")

print(mydog.name)
print(mydog.branch)
print(mydog.age)
print(mydog.bark())



class Circle:
	pi = 3.14
	def __init__(self,radius=1):
		self.radius =radius

	def circumference(self):
		return self.radius*self.pi*2

	def set_radius(self,new_radius):
		self.radius = new_radius

	def get_area(self):
		return pi*(radius**2)


c = Circle()

print("Default Radius : ",c.radius)
