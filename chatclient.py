# The network part is from https://www.youtube.com/watch?v=D0SLpD7JvZI

import socket
import threading
import sys

class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            self.s.send(bytes(input(""), 'utf-8'))

    def __init__(self, a):
        self.s.connect((a, 5000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.s.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))

client = Client(sys.argv[1])
