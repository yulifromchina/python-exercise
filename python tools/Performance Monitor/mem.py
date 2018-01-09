#!/usr/bin/env python3

from collections import OrderedDict

def GetMemInfo():
	memInfo = OrderedDict()
	with open('/proc/meminfo') as f:
		for line in f:
			key = line.split(':')[0].strip()
			value = line.split(':')[1].strip()
			memInfo[key] = value
	return memInfo


if __name__ == "__main__":
	memInfo = GetMemInfo()
	print('Total Memory:{}'.format(memInfo['MemTotal']))
	print('Free Memeory:{}'.format(memInfo['MemFree']))
