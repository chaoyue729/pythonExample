# -*- coding: utf8 -*-

# import socketserver
# import threading
from socket import *
from select import *

import sys
from time import ctime
import time
import datetime
import os
import json
import random
from sys import exit

'''
sudo lsof -i tcp:27029
'''

def timeFormat(endTime):
    return '{:02d}:{:02d}:{:02d}'.format(endTime // 3600, (endTime % 3600 // 60), endTime % 60)

class agent():
    def __init__(self, callNumber, callData):
        self.callNumber = callNumber
        self.callDataArray = callData
        self.callDataIndex = 0

    def getCallData(self):
        if self.callDataIndex == len(self.callDataArray):
            self.callDataIndex = 0
        idx = self.callDataIndex
        self.callDataIndex += 1
        return self.callDataArray[idx]

def getJsonStr(callNumber, speaker, sTime, eTime, sentence, status):
    jsonStr = "{{'callNumber':'{0}', 'speaker':'{1}', 'sTime':'{2}', 'eTime':'{3}', 'sentence':'{4}', 'status':'{5}'}}".format(callNumber, speaker, sTime, eTime, sentence, status)
    return jsonStr

def setCallData(callNumbers, testFileDir):
    callDataDict = {}
    for callNumber in callNumbers:
        callDataDict[callNumber] = []

    try:
        fileNames = os.listdir(testFileDir)
        for fileName in fileNames:
            fullFileName = os.path.join(testFileDir, fileName)
            if os.path.isdir(fullFileName):
                setCallData(callNumbers, fullFileName)
            else:
                ext = os.path.splitext(fullFileName)[-1]
                # baseName = os.path.splitext(fileName)[0]
                if ext == '.dat':
                    f = open(fullFileName, 'r', encoding='utf-8')
                    cn = random.choice(callNumbers)
                    callDataDict[cn].append(getJsonStr(cn, '', '', '', '', 'start'))

                    while True:
                        line = f.readline()
                        if not line: break
                        arr = line.replace('\n','').split('|')
                        callDataDict[cn].append(getJsonStr(cn, arr[0], arr[1], arr[2], arr[3], 'pending'))

                    callDataDict[cn].append(getJsonStr(cn, '', '', '', '', 'finish'))
                    f.close()

    except PermissionError:
        pass

    return callDataDict

def runServer(**options):

    addr = options['addr']
    bufsize = options['bufsize']
    nps = options['nps']
    aps = options['aps']

    # 소켓 객체를 만들고..
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # 서버 정보를 바인딩
    serverSocket.bind(addr)

    # 요청을 기다림(listen)
    serverSocket.listen(10)
    connection_list = [serverSocket]
    print('==============================================')
    print('채팅 서버를 시작합니다. %s 포트로 접속을 기다립니다.' % str(addr[1]))
    print('==============================================')

    # 무한 루프를 시작
    while connection_list:
        try:
            print('[INFO] 요청을 기다립니다...')

            # select 로 요청을 받고, 10초마다 블럭킹을 해제하도록 함
            read_socket, write_socket, error_socket = select(connection_list, [], [], 0.1)

            print('connectionList : ' + str(connection_list))
            # print('-->' + str(read_socket) + " : " + str(write_socket) + " : " + str(error_socket))
            print('now : ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))
            for sock in read_socket:
                # 새로운 접속
                if sock == serverSocket:
                    clientSocket, addr_info = serverSocket.accept()
                    connection_list.append(clientSocket)
                    print('[INFO][%s] 클라이언트(%s)가 새롭게 연결 되었습니다.' % (ctime(), addr_info[0]))

                # 접속한 사용자(클라이언트)로부터 새로운 데이터 받음
                else:

                    if data:
                        print('[INFO][%s] 클라이언트로부터 데이터를 전달 받았습니다.' % ctime())
                        try:
                            data = sock.recv(bufsize).decode('utf-8')
                            # nps, aps 수정
                            # ex) {nps:5, aps:10}
                            # data 정보를 parsing 하여 형식이 일치하면 수정
                            # aps 이상의 값은 agents 초기화
                            print('[INFO][%s] 설정 정보를 변경합니다.' % ctime())
                        except Exception as e:
                            print(e)
                            socket_in_list.close()
                            connection_list.remove(socket_in_list)
                            continue
                    else:
                        connection_list.remove(sock)
                        sock.close()
                        print('[INFO][%s] 사용자와의 연결이 끊어졌습니다.' % ctime())

            # 접속자에게 데이터 전달, 접속자가 없을경우 전달하지 않고 데이터 손실
            slppeSecond = float("{0:.2f}".format(nps / aps - 0.005))
            print('slppeSecond : ' + str(slppeSecond))
            print('agents len : ' + str(len(options['agents'])))
            for agent in options['agents'][:( aps if len(options['agents']) > aps else len(options['agents']) )]:
                for clientSocket in connection_list:
                    if clientSocket != serverSocket:
                        try:
                            clientSocket.send((agent.getCallData()).encode('utf-8'))
                        except Exception as e:
                            print(e)
                            socket_in_list.close()
                            connection_list.remove(socket_in_list)
                time.sleep(slppeSecond)
            print('사용자에게 전달 종료')
        except KeyboardInterrupt:
            # 부드럽게 종료하기
            serverSocket.close()
            # sys.exit()

def main():
    # 호스트, 포트와 버퍼 사이즈를 지정
    host = ''
    port = 27029
    bufsize = 1024
    addr = (host, port)

    # 초당 건수
    nps = 5
    # 초당 상담원수
    aps = 3

    # test data 정보
    # testFileDir = '/Users/whitexozu/dev/data/KB/stt/seoul/text/20180219/10'   #6812
    testFileDir = '/Users/whitexozu/dev/data/KB/stt/seoul/text/20180219/1'  #7
    callNumberFormat='1544-{0}'
    numberOfAgents = 10
    callNumbers = []
    agents = []

    for i in range(1, numberOfAgents+1):
        callNumbers.append(callNumberFormat.format("%04d" % i))

    start_time = time.time()
    print('+++ call data 생성 시작')
    callDataDict = setCallData(callNumbers, testFileDir)
    for k, v in callDataDict.items():
        if v :
            agents.append(agent(k, v))

    print('+++ call data 생성 종료')
    print('+++ call data 생성 시간 : {0}'.format(timeFormat(int(time.time() - start_time))))

    print('+++ agents count : ' + str(len(agents)))

    print('+++ STT 서버를 시작')
    print('+++ STT 서버를 끝내려면 Ctrl-C를 누르세요.')
    runServer(addr=addr, bufsize=bufsize, nps=nps, aps=aps, agents=agents)

main()
