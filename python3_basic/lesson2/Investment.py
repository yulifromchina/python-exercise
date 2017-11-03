#!/usr/bin/env python3
amount = float(input("Enter amount:"))
rate = float(input("Enter Interest Rate:"))
period = int(input("Enter period:"))
value = 0
year = 1
while year <= period:
	value = amount + (rate * amount)
	print("Year {} Rs.{:.2f}".format(year, value))
	amount = value
	year = year + 1
