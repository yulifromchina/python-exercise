#!/usr/bin/env python3

def GetNumber():
	number = float(input("Enter a float number:"))
	return number

if __name__ == "__main__":
	while True:
		try:
			print(GetNumber())
		except ValueError:
			print("You entered a wrong value.")
			
