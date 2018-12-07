import sys
import json
from socket import *
from select import select
import ast

host = 'localhost'
port = 27029
bufsize = 1024
# BUFSIZE = 1048576
addr = (host, port)
# 소켓 객체를 만들고
clientSocket = socket(AF_INET, SOCK_STREAM)

# 서버와의 연결을 시도
try:
    clientSocket.connect(addr)
except Exception as e:
    print('채팅 서버(%s:%s)에 연결 할 수 없습니다.' % addr)
    sys.exit()
print('채팅 서버(%s:%s)에 연결 되었습니다.' % addr)


def prompt():
    sys.stdout.write('설정 정보\n')
    sys.stdout.write('ex) {"wc":10, "ac":10}\n')
    sys.stdout.write(':')
    sys.stdout.flush()

# 무한 루프를 시작
prompt()
while True:
    try:
        connection_list = [sys.stdin, clientSocket]

        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)



        for sock in read_socket:
            if sock == clientSocket:
                data = sock.recv(bufsize)
                if not data:
                    print('채팅 서버(%s:%s)와의 연결이 끊어졌습니다.' % addr)
                    clientSocket.close()
                    sys.exit()
                else:
                    pass
            else:
                message = sys.stdin.readline()
                clientSocket.send(message.encode('utf-8'))
                prompt()
    except KeyboardInterrupt:
        clientSocket.close()
        sys.exit()
