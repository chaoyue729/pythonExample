import sys
import json
from socket import *
from select import select
import ast
import requests
import time
import datetime

# tcp server 정보
tcpServerHost = 'localhost'
tcpServerPort = 27029
tcpServerBufsize = 1024
# tcpServerBufsize = 1048576
addr = (tcpServerHost, tcpServerPort)
# 소켓 객체를 만들고
clientSocket = socket(AF_INET, SOCK_STREAM)

# web server 정보
webServerHost = 'localhost'
webServerPort = '8000'
webServerPath = '/adv/rcv/'

# 서버와의 연결을 시도
try:
    clientSocket.connect(addr)
except Exception as e:
    print('채팅 서버(%s:%s)에 연결 할 수 없습니다.' % addr)
    sys.exit()
print('채팅 서버(%s:%s)에 연결 되었습니다.' % addr)


def prompt():
    sys.stdout.write('<나> ')
    sys.stdout.flush()

# 무한 루프를 시작
while True:
    try:
        connection_list = [sys.stdin, clientSocket]

        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            if sock == clientSocket:
                data = sock.recv(tcpServerBufsize)
                if not data:
                    print('채팅 서버(%s:%s)와의 연결이 끊어졌습니다.' % addr)
                    clientSocket.close()
                    sys.exit()
                else:
                    print('%s' % data.decode('utf-8'))  # 메세지 시간은 서버 시간을 따른다
                    webUrl = 'http://{0}:{1}{2}'.format(webServerHost, webServerPort, webServerPath)
                    data = json.loads(data.decode('utf-8'))
                    # print(type(json.loads(data.decode('utf-8'))))
                    res = requests.post(webUrl, data)
                    print(res.status_code)
                    if res.status_code == 200:
                        print(res.text)
    except KeyboardInterrupt:
        clientSocket.close()
        sys.exit()
