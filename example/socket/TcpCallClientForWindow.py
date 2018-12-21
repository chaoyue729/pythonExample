#!/usr/bin/python
#*-* coding: utf-8 *-*
import sys
import json
from socket import *
from select import select
import ast
import requests
import time
import datetime

# tcp server 정보
tcpServerHost = '118.218.215.211'
# tcpServerHost = 'localhost'
tcpServerPort = 27029
tcpServerBufsize = 1024
# 소켓 객체를 만들고
clientSocket = socket(AF_INET, SOCK_STREAM)

# web server 정보
webServerHost = '192.168.0.2'
webServerPort = '8000'
webServerPath = '/adv/rcv/'


print('connecting....')
clientSocket.connect((tcpServerHost, tcpServerPort))
print('ok')
while 1:
	try:
		data = {}
		if clientSocket.recv(1024).decode('utf-8') != '':
			data = json.loads(clientSocket.recv(1024).decode('utf-8'))
		print('recive_data : ' + str(data))
		try:
			webUrl = 'http://{0}:{1}{2}'.format(webServerHost, webServerPort, webServerPath)
			res = requests.post(webUrl, data)
			print(res.status_code)
			if res.status_code == 200:
				print(res.text)
		except requests.exceptions.ConnectionError as err:
			print('WebSocket connection error: {0}'.format(err))
			pass
		except:
			print("Unexpected error:", sys.exc_info()[0])
			pass
	except KeyboardInterrupt:
		clientSocket.close()
		sys.exit()
