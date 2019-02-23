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

def getJsonStr(callNumber, entryNumber, speaker, sTime, eTime, sentence, status, uid):
    jsonStr = '{{"callNumber":"{0}", "entryNumber":"{1}", "speaker":"{2}", "sTime":"{3}", "eTime":"{4}", "sentence":"{5}", "status":"{6}", "uid":"{7}"}}'.format(callNumber, entryNumber, speaker, sTime, eTime, sentence, status, uid)
    return jsonStr

def setCallData(**options):
    callNumbers = options['callNumbers']
    entryNumbers = options['entryNumbers']
    testFileDir = options['testFileDir']
    startTime = options['startTime']

    callDataDict = {}
    for callNumber in callNumbers:
        callDataDict[callNumber] = []

    try:
        fileNames = os.listdir(testFileDir)
        for fileIdx, fileName in enumerate(fileNames):
            fullFileName = os.path.join(testFileDir, fileName)
            if os.path.isdir(fullFileName):
                setCallData(callNumbers, fullFileName)
            else:
                ext = os.path.splitext(fullFileName)[-1]
                # baseName = os.path.splitext(fileName)[0]
                if ext == '.dat':
                    f = open(fullFileName, 'r', encoding='utf-8')
                    if options['rf']:
                        cn = random.choice(callNumbers)
                        en = random.choice(entryNumbers)
                    else:
                        cn = callNumbers[fileIdx % 10]
                        en = entryNumbers[fileIdx % 10]

                    uid = str(startTime) + '_' + cn
                    callDataDict[cn].append(getJsonStr(cn, en, '', '', '', '', 'start', uid))

                    while True:
                        line = f.readline()
                        if not line: break
                        arr = line.replace('\n','').split('|')
                        callDataDict[cn].append(getJsonStr(cn, en, arr[0], arr[1], arr[2], arr[3], 'pending', uid))

                    callDataDict[cn].append(getJsonStr(cn, en, '', '', '', '', 'finish', uid))
                    f.close()

    except PermissionError:
        pass

    return callDataDict

def runServer(**options):

    # addr = options['addr']
    # bufsize = options['bufsize']
    wc = options['wc']
    ac = options['ac']

    # 소켓 객체를 만들고..
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # 서버 정보를 바인딩
    serverSocket.bind(options['addr'])

    # 요청을 기다림(listen)
    serverSocket.listen(10)
    connectionList = [serverSocket]
    print('==============================================')
    print('채팅 서버를 시작합니다. %s 포트로 접속을 기다립니다.' % str(options['addr'][1]))
    print('==============================================')

    # 무한 루프를 시작
    while connectionList:
        try:
            print('[INFO] 요청을 기다립니다...')

            # select 로 요청을 받고, 10초마다 블럭킹을 해제하도록 함
            read_socket, write_socket, error_socket = select(connectionList, [], [], 0.1)

            print('[INFO][{0}] 접속자수 : {1}'.format(ctime(), len(connectionList) - 1))
            # print('[INFO] now : ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")))
            for sock in read_socket:
                # 새로운 접속
                if sock == serverSocket:
                    clientSocket, addr_info = serverSocket.accept()
                    connectionList.append(clientSocket)
                    print('[INFO][{0}] 클라이언트({1})가 새롭게 연결 되었습니다.'.format(ctime(), addr_info[0]))

                # 접속한 사용자(클라이언트)로부터 새로운 데이터 받음
                else:
                    data = sock.recv(options['bufsize'])
                    if data:
                        print('[INFO][{0}] 클라이언트로부터 데이터를 전달 받았습니다.'.format(ctime()))
                        for clientSocket in connectionList:
                            if clientSocket != serverSocket and clientSocket == sock:
                                try:
                                    data = data.decode('utf-8')
                                    data = json.loads(data)
                                    # wc, ac 수정
                                    # ex) {wc:5, ac:10}
                                    # data 정보를 parsing 하여 형식이 일치하면 수정
                                    wc = data['wc']
                                    ac = data['ac']
                                    print('[INFO][{0}] 설정 정보 wc:{1}, ac:{2} 변경합니다.'.format(ctime(), wc, ac))
                                except Exception as e:
                                    print(e)
                                    clientSocket.close()
                                    connectionList.remove(clientSocket)
                                    continue
                    else:
                        connectionList.remove(sock)
                        sock.close()
                        print('[INFO][{0}] 사용자와의 연결이 끊어졌습니다.'.format(ctime()))

            # 접속자에게 데이터 전달, 접속자가 없을경우 전달하지 않고 데이터 손실
            # agents 보다 ac 가 크면 agents 로 초기화
            ac = ac if len(options['agents']) > ac else len(options['agents'])
            slppeSecond = float("{0:.2f}".format(wc / ac - 0.005))    # 내림
            print('[INFO][{0}] slppeSecond : {1}'.format(ctime(), slppeSecond))
            # print('[INFO][{0}] agents len : {1}'.format(ctime(), len(options['agents'])))
            for agent in options['agents'][:ac]:
                sendData = agent.getCallData()
                for clientSocket in connectionList:
                    if clientSocket != serverSocket:
                        try:
                            clientSocket.send(sendData.encode('utf-8'))
                            print('[INFO][{0}] send.'.format(ctime()))
                        except Exception as e:
                            print(e)
                            connectionList.remove(clientSocket)
                            clientSocket.close()
                            print('[INFO][{0}] 사용자와의 연결이 끊어졌습니다.'.format(ctime()))
                time.sleep(slppeSecond)
        except KeyboardInterrupt:
            # 부드럽게 종료하기
            serverSocket.close()
            # sys.exit()

def main():
    # 호스트, 포트와 버퍼 사이즈를 지정
    host = ''
    port = 27029
    bufsize = 1024 * 5
    addr = (host, port)

    # 건당 대기 초
    wc = 3
    # 상담원수
    ac = 10
    # random 여부
    rf = False

    # test data 정보
    testFileDir = 'C:\dev\python\data'
    callNumberFormat='1544-{0}'
    entryNumberFormat='010-1234-{0}'
    numberOfAgents = 10
    callNumbers = []
    entryNumbers = []
    agents = []

    for i in range(1, numberOfAgents+1):
        callNumbers.append(callNumberFormat.format("%04d" % i))
        entryNumbers.append(entryNumberFormat.format("%04d" % i))

    startTime = time.time()
    startTimeApplyFormat = str(datetime.datetime.fromtimestamp(startTime).strftime('%Y%m%d%H%M%S%f'))
    print('+++ call data 생성 시작')
    callDataDict = setCallData(callNumbers=callNumbers, entryNumbers=entryNumbers, testFileDir=testFileDir, rf=rf, startTime=startTimeApplyFormat)
    for k, v in callDataDict.items():
        if v :
            agents.append(agent(k, v))

    print('+++ call data 생성 종료')
    print('+++ call data 생성 시간 : {0}'.format(timeFormat(int(time.time() - startTime))))

    print('+++ agents count : ' + str(len(agents)))

    print('+++ STT 서버를 시작')
    print('+++ STT 서버를 끝내려면 Ctrl-C를 누르세요.')
    runServer(addr=addr, bufsize=bufsize, wc=wc, ac=ac, agents=agents)

main()
