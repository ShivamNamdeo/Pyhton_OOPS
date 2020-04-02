class Animal():
	def __init__(self,name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Sublclass Must Implemented This Abstract Class")


class Dog(Animal):
	def speak(self):
		return self.name + "Says Woofs"


class Cat(Animal):
	def speak(self):
		return self.name + "Says Mews"


fido = Dog("fido")
isis = Cat("isis")

print(fido.speak())
print(isis.speak())