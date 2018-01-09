#!/usr/bin/env python3

import os
from collections import OrderedDict

def load_stat():
	loadavg = OrderedDict()
	with open('/proc/loadavg') as f:
		content = f.read().split()
	loadavg['lavg_1'] = content[0]
	loadavg['lavg_5'] = content[1]
	loadavg['lavg_15'] = content[2]
	loadavg['running processes'] = content[3].split('/')[0]
	loadavg['sum of processes'] = content[3].split('/')[1]
	loadavg['recently running pid'] = content[4]
	return loadavg

if __name__ == '__main__':
	loadavg = load_stat()
	for key in loadavg.keys():
		print('{}:{}'.format(key, loadavg[key]))
