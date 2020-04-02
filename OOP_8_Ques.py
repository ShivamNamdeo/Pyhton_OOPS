class Simple():
	def __init__(self,value):
		self.value = value

	def add_to_value(self,amount):
		print("{} Added To  Your Account".format(self.value))
		self.value = self.value +amount


myobj = Simple(300)
myobj.value


myobj.add_to_value(300)
print("Your Current Balance Is  : ",myobj.value)
print(myobj.value)