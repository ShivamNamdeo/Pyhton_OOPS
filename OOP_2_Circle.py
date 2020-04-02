import os

class Circle:
	pi = 3.14
	def __init__(self,radius=1):
		self.radius =radius

	def circumference(self):
		return (self.radius*Circle.pi*2)

	def set_radius(self,new_radius):
		self.radius = new_radius

	def get_area(self):
		return Circle.pi*(self.radius**2)


os.system("clear")
print("Operation On Circle")
c = Circle()

print("Default Radius : ",c.radius)
print("Default Area : ",c.get_area())
print("Default Circumference  : ",c.circumference())
radius = int(input("Enter New Radius : "))
c.set_radius(radius)

print("New Radius : ",c.radius)
print("New Area : ",c.get_area())
print("New Circumference  : {:.3f}".format(c.circumference()))

