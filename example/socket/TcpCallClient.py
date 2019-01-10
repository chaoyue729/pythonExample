import sys
import json
from socket import *
from select import select
import ast
import requests
import time
import datetime
import threading
import re

# tcp server 정보
tcpServerHost = '118.218.215.211'
# tcpServerHost = 'localhost'
tcpServerPort = 27029
tcpServerBufsize = 1024 * 5
# tcpServerBufsize = 1048576
addr = (tcpServerHost, tcpServerPort)
# 소켓 객체를 만들고
clientSocket = socket(AF_INET, SOCK_STREAM)

# web server 정보
# webServerHost = '192.168.0.2'
webServerHost = '127.0.0.1'
webServerPort = '8000'
webServerPath = '/adv/rcv/'

# 서버와의 연결을 시도
try:
    clientSocket.connect(addr)
except Exception as e:
    print('채팅 서버(%s:%s)에 연결 할 수 없습니다.' % addr)
    sys.exit()
print('채팅 서버(%s:%s)에 연결 되었습니다.' % addr)

# 한번에 여러게의 데이터가 동시에 들어오는 경우 확인을 위해 정규식 사용
regex = re.compile('\{.*?\}')

def prompt():
    sys.stdout.write('<나> ')
    sys.stdout.flush()

class htmlPost (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), ' chars')

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
                    # print('%s' % data.decode('utf-8'))  # 메세지 시간은 서버 시간을 따른다
                    try:
                        webUrl = 'http://{0}:{1}{2}'.format(webServerHost, webServerPort, webServerPath)
                        datas = regex.findall(data.decode('utf-8'))
                        # print(len(datas))
                        for d in datas:
                            jd = json.loads(d)
                            print(jd)
                            res = requests.post(webUrl, jd)

                        # data = json.loads(data.decode('utf-8'))
                        # print(type(json.loads(data.decode('utf-8'))))
                        # res = requests.post(webUrl, data)
                        # print(res.status_code)
                        # if res.status_code == 200:
                            # print(res.text)
                    except requests.exceptions.ConnectionError as err:
                        print('WebSocket connection error: {0}'.format(err))
                        pass
                    except:
                        print("Unexpected error:", sys.exc_info()[0])
                        pass
    except KeyboardInterrupt:
        clientSocket.close()
        sys.exit()
