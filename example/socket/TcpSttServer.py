# -*- coding: utf8 -*-

from socket import *
from select import *
import sys
from time import ctime
import time
import datetime


f = open("SampleBigData.csv", 'r')
lines = f.readlines()

# 호스트, 포트와 버퍼 사이즈를 지정
HOST = ''
PORT = 56789
BUFSIZE = 1024
ADDR = (HOST, PORT)
# 소켓 객체를 만들고..
serverSocket = socket(AF_INET, SOCK_STREAM)
# 서버 정보를 바인딩
serverSocket.bind(ADDR)
# 요청을 기다림(listen)
serverSocket.listen(10)

status = True
loopCount = 0
loopMaxCount = 5
connection_list = [serverSocket]
print('==============================================')
print('채팅 서버를 시작합니다. %s 포트로 접속을 기다립니다.' % str(PORT))
print('==============================================')

# 무한 루프를 시작
while connection_list:
    try:

    except KeyboardInterrupt:
        # 부드럽게 종료하기
        serverSocket.close()
        sys.exit()

while status:
    for line in lines:
        # if not line: break
        # if not line:

        # dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        dt = datetime.datetime.now().isoformat()
        print('{} {}'.format(dt, line))
        time.sleep(0.5)


    print('loop count : {}, status : {}'.format(loopCount, status))

    loopCount += 1
    if loopCount > 5 : status = False

f.close()