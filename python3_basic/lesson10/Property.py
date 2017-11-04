#!/usr/bin/env python3

# @property : make a function become an attrbute

class Account(object):
	"""
	account class
	"""
	def __init__(self, rate):
		self._amount = 0
		self.rate = rate

	@property
	def amount(self):
		return self._amount

	@property
	def renmingbi(self):
		return self._amount * self.rate

	@amount.setter
	def amount(self, value):
		if value < 0:
			print("Sorry, no negative amount in account.")
			return
		self._amount = value

if __name__ == "__main__":
	acc = Account(rate = 6.6)
	acc.amount = 120
	print("Dollar amount:", acc.amount)
	print("Renmingbi:", acc.renmingbi)
	acc.amount-=100
	print("Dollar amount:", acc.amount)

