#!/usr/bin/env python3

from collections import OrderedDict


def GetCPUInfo():

	CPUInfo = OrderedDict()
	ProcInfo = OrderedDict()
	cpu_num = 0
	
	with open('/proc/cpuinfo') as f:
		for line in f:
			if not line.strip():	
				CPUInfo['{}'.format(cpu_num)] = ProcInfo
				ProcInfo = OrderedDict()
				cpu_num = cpu_num + 1	
			else:
				#get infomation of each CPU
				key = line.split(':')[0].strip()
				if len(line.split(':'))==2:
					value = line.split(':')[1].strip()
					ProcInfo[key] = value
				else:
					ProcInfo[key] = ''
	return CPUInfo


if __name__ == '__main__':
	CPUInfo = GetCPUInfo()
	for cpu in CPUInfo.keys():
		print(CPUInfo[cpu]['model name'])
