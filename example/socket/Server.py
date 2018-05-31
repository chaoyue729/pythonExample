import socket

s = socket.socket()
host = socket.gethostname()
host = '192.168.30.157'
print( 'host : {0}'.format(host))
port = 12222
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Halts
       print( '[Waiting for connection...]')
       c, addr = s.accept() #  (socket object, address info) return
       print('addr {0}'.format(addr))
       print('port {0}'.format(port))
       print('c {0}'.format(c))
   else:
       # Halts
       print( '[Waiting for response...]')
       print((c.recv(1024)).decode('utf-8'))
       q = input("Enter something to this client: ")
       c.send(q.encode('utf-8'))
