# most of the code is from https://www.youtube.com/watch?v=D0SLpD7JvZI
# This is a chat server. Run this first, and then chatclient.py
# Tested with Python 3.5.2 on Ubuntu.


import socket
import threading
import sys

class Server:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.s.bind(('0.0.0.0', 5000))
        print('Server Running.....')
        self.s.listen(5)


    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            self.con_num = str(self.connections.index(c))
            q = str(data, 'utf-8')
            if q == ('/quit'+ '\n'):
                for connection in self.connections:
                    connection.send(bytes(self.con_num + ' has left the chatroom \n', 'utf8'))
                self.connections.remove(c)
                c.close()
                break
            else:
                for connection in self.connections:
                    connection.send(bytes(self.con_num + ' says: ', 'utf8') + data)
            if not data:
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.s.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c) 
            print(self.connections)
            if (len(self.connections)) > 5:
                c.send(b'/quit')

server = Server()
server.run()

