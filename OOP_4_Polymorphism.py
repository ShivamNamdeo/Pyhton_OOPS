class Dog():
	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " Says Woof"


class Cat():
	def __init__(self,name):
		self.name = name

	def speak(self):
		return self.name + " Says Meaw"


niko = Dog("Nikoo")
felix = Cat("Felix")
'''
print(niko.speak())
print(felix.speak())


for pet in [felix,niko]:
	print(pet.speak())

'''

def pet_speak(pet):
	print(pet.speak())

print(pet_speak(niko))
print(pet_speak(felix))
