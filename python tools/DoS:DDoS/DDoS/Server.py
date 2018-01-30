# -*- coding:utf-8 -*-
#!/usr/bin/env python3

import socket
import argparse
from threading import Thread
import logging
import logging.config
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("serverLogger")

socketList = []#成功建立连接的socket实例列表

def sendCmd(cmd):
	print('Send command...')
	for sock in socketList:
		sock.send(bytes(cmd,encoding='utf-8'))


def waitConnect(s):
	while True:
		sock,addr = s.accept() #sock是已经建立连接的socket 实例
		if sock not in socketList:
			socketList.append(sock)


def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind(('0.0.0.0',58868))
	s.listen(1024)
	t = Thread(target=waitConnect,args=(s,))#开辟线程来建立连接
	t.start()

	print('Wait at least a client connection')
	while not len(socketList):
		pass

	print('It has been a client connection')
	
	while True:
		print('='*50)
		print('The command format:"#-H xxx.xxx.xxx.xxx -p xxxx -c <start|stop>"')
		cmd_str = input('Please input cmd:')
		if len(cmd_str):
			if cmd_str[0]=='#':
				sendCmd(cmd_str)
			else:
				logging.error('error format!')
				logging.error(cmd_str)


if __name__=='__main__':
	main()
