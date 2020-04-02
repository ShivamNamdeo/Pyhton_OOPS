class Animal():
	"""docstring for ClassName"""
	def __init__(self):
		print("Animal Printed")

	def who_am_i(self):
		print("I Am An Animal")

	def eat(self):
		print("I Am Eating")



class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Dog Created")

	def who_am_i(self):
		print("I Am A Dog")

	def eat(self):
		print("I Am Eating")

	def bark(self):
		print("Woof !")
		

mydog = Dog()

print(mydog.who_am_i())
print(mydog.eat())
print(mydog.bark())
