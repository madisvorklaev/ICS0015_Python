# most of the code is from https://www.youtube.com/watch?v=D0SLpD7JvZI

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
            q = str(data, 'utf-8')
            if q == ('/quit'+ '\n'):
                self.connections.remove(c)
                c.close()
                break
            else:
                for connection in self.connections:
                    connection.send(data)
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
            if (len(self.connections)) > 2:
                c.send(b'{quit}')
#                self.connections.remove(c)
#                c.close()

server = Server()
server.run()

