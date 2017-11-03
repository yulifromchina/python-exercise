#!/usr/bin/env python3

import os
import sys

def parse_file(path):
	"""
	:arg path:file path
	:return:(blank number, tab number, line number)
	"""
	fd = open(path)
	i = 0
	space = 0
	tab = 0
	for i, line in enumerate(fd):
		space += line.count(' ')
		tab += line.count('\t')
	fd.close()

	return space, tab, i+1


def main(path):
	"""
	:arg path: file path
	:return : true if file exits, or false
	"""
	if os.path.exists(path):
		space, tab, line = parse_file(path)
		print("Space {}, tab {}, line {}.".format(space, tab, line))
		return True
	else:
		return False

if __name__=="__main__":
	if len(sys.argv)>1:
		main(sys.argv[1])
	else:
		sys.exit(-1)
	sys.exit(0)
