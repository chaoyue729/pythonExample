# -*- coding: utf8 -*-

import socketserver
import threading
import sys
from time import ctime
import time
import datetime
import os
import json

dictResult = {}
# testFileDir = '/Users/whitexozu/dev/data/temp1'
# testFileDir = '/Users/whitexozu/dev/data/temp2'
testFileDir = '/Users/whitexozu/dev/data/richandco'

gLoopMaxCount = 5

# 호스트, 포트와 버퍼 사이즈를 지정
HOST = ''
PORT = 9999
# BUFSIZE = 1024
ADDR = (HOST, PORT)
lock = threading.Lock()  # syncronized 동기화 진행하는 스레드 생성

dictResult = {}

def strToJson(type, filename, body, datetime):
    # customer = {
    #     'type': type,
    #     'id': filename,
    #     'body': body,
    #     'date': datetime
    # }

    # JSON 인코딩
    # jsonString = json.dumps(customer)
    # jsonString = json.dumps(customer, indent=4)

    jsonString = "{{'type':'{0}', 'id':'{1}', 'body':'{2}', 'data':'{3}'}}".format(type, filename, body, datetime)

    # 문자열 출력
    # print(jsonString)
    # print(type(jsonString))  # class str

    return jsonString

def searchDirFile(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                searchDirFile(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                basename = os.path.splitext(filename)[0]
                if ext == '.TXT':
                    text = ''
                    f = open(full_filename, 'r', encoding='euc-kr')

                    # 개행유지
                    # text = f.read()
                    # 개행 제거 후 , 로 구분
                    lines = f.readlines()
                    text = ','.join(str(s.strip()) for s in lines)

                    # print(text)

                    dictResult[filename] = strToJson('data', basename, text, datetime.datetime.now().isoformat())
                    f.close()

    except PermissionError:
        pass

class MyTcpHandler(socketserver.BaseRequestHandler):
    status = True
    loopCount = 0
    loopMaxCount = gLoopMaxCount

    def handle(self):  # 클라이언트가 접속시 클라이언트 주소 출력
        print('[%s] 연결됨' % self.client_address[0])

        try:
            numberOfSecond = 1 / float(self.registerNumberOfSecond())
            print('[{0}] numberOfSecond : {1}'.format(self.client_address[0], numberOfSecond))
            while self.status:
                for k in dictResult.keys():
                    # dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    dt = datetime.datetime.now().isoformat()
                    # print('{0} {1}'.format(dt, line))
                    # self.request.send(dictResult[k].encode())
                    self.request.send(dictResult[k].encode('utf-8'))
                    time.sleep(numberOfSecond)

                print('[{0}] loop count : {1}, status : {2}'.format(self.client_address[0], self.loopCount, self.status))

                self.loopCount += 1
                if self.loopCount > 5: self.status = False

        except Exception as e:
            print(e)

        print('[%s] 접속종료' % self.client_address[0])

    def registerNumberOfSecond(self):
        while True:
            self.request.send(strToJson('msg', '', '초당 발생 건수 :', datetime.datetime.now().isoformat()).encode())
            # self.request.send('초당 발생 건수 :'.encode())
            numberOfSecond = self.request.recv(1024)
            return numberOfSecond.decode().strip()

class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def runServer():
    print('+++ STT dict 생성 시작')
    searchDirFile(testFileDir)
    print('+++ STT dict 생성 종료')

    print('+++ STT 서버를 시작')
    print('+++ STT 서버를 끝내려면 Ctrl-C를 누르세요.')

    try:
        server = ChatingServer(ADDR, MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('+++ STT 서버를 종료합니다.')
        server.shutdown()
        server.server_close()

runServer()




