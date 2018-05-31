import sys
import json
import socket
import ast
from threading import Thread

HOST = 'localhost'
PORT = 9999
BUFSIZE = 1048576
ADDR = (HOST, PORT)

def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(BUFSIZE)
            if not data:
                break

            msg = data.decode('utf-8')

            # json 형식으로 넘어오는 경우
            # msg = json.loads(msg)
            # string 으로 넘어오는 경오 dict 로 변경
            msg = ast.literal_eval(msg)

            # print(msg['type'])
            # print(msg['body'])

            if msg['type'] == 'msg':
                print(msg['body'])
            else:
                print(msg)

        except OSError as e:
            pass
        # except json.decoder.JSONDecodeError as e:
        #     pass
        except:
            print(sys.exc_info()[0])
            # pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(ADDR)
        t = Thread(target=rcvMsg, args=(sock,))
        t.daemon = True
        t.start()

        while True:
            msg = input()
            sock.send(msg.encode())

runChat()