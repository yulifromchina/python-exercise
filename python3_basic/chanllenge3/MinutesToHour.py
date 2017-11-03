#!/usr/bin/env python3

import sys

def GetMinitesToH(minites):
	if minites < 0:
		raise ValueError("Input number cannot be negative.")
		sys.exit(-1)
	return divmod(minites, 60)

if __name__ == "__main__":
	if(len(sys.argv) < 2):
		print("Usage: \n ./MinitesToHours.py minites")
		sys.exit(-1)

	h, m = GetMinitesToH(int(sys.argv[1]))
	print("{} H, {} M".format(h, m))
	
