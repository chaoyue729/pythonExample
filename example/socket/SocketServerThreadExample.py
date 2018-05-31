#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
import socketserver


class SocksHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('> {0}'.format(self))
        self.data = self.rfile.readline().strip()

        if self.data:
            print("%s" % str(self.client_address[0]))
            print(self.data)
            self.request.send(self.data.upper())
        else:
            self.request.close()

class SocksServer(socketserver.ThreadingTCPServer):
    def __init__(self, listen_addr):
        socketserver.ThreadingTCPServer.__init__(self, listen_addr, SocksHandler)
        self.allow_reuse_address = True
        self.daemon_threads = True
        self.request_queue_size = 50

    def start(self):
        self.serve_forever()

if __name__ == '__main__':
    HOST, PORT = '', 9999
    obj = SocksServer((HOST, PORT))
    obj.start()