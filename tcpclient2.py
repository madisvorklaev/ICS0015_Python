import socket
import threading
import sys

class Client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        message = input('=>')
        while self.message != 'q':
            self.s.send(message.encode('utf-8'))
        self.s.close()

    def __init__(self):
        self.s.connect(('127.0.0.1', 5000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.s.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
            
client = Client()
