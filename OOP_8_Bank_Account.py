import os
class Account():
	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance  =balance

	def deposit(self,deposit_amount):
		self.balance = self.balance + deposit_amount
		print(f"You Have Added : {deposit_amount} \n")

	def withdral_Amount(self,with_Amount):
		if self.balance >= with_Amount:
			self.balance = self.balance - with_Amount
			print(f"Your withdralAmount: {with_Amount} \n")
		else:
			print(f"Your Account Have Only : {self.balance}")

	def __str__(self):
		return f"Owner : {self.owner} \n Balance : {self.balance}"




