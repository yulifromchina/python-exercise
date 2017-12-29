#!/usr/bin/python3

import sys
from socket import *

#scanPort.py <host> <start_port>-<end-port>
host = sys.argv[1]
portstrs = sys.argv[2].split('-')

start_port=int(portstrs[0])
end_port=int(portstrs[1])

opened_ports = []
target_ip =gethostbyname(host)
opened_ports = []
for port in range(start_port, end_port+1):
	sock = socket(AF_INET,SOCK_STREAM)
	sock.settimeout(10)
	result = sock.connect_ex((target_ip, port))
	if result==0:
		opened_ports.append(port)

print("Opened ports:")
for i in opened_ports:
	print(i)

