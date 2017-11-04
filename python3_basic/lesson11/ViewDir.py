#!/usr/bin/env python3

import os

def ViewDir(path = "."):
	name = os.listdir(path)
	name.sort()
	for x in name:
		print(x, end=" ")
	print()

if __name__ == "__main__":
	ViewDir()
