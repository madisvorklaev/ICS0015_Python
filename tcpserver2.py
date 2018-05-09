import socket
import threading

class Server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.s.bind(('127.0.0.1', 5000))
        print('Server Running.....')
        self.s.listen(1)
        
    def handler(self, client, address):
        while True:
            data = client.recv(1024).decode('utf-8')
            for connection in connections:
                connection.send(data)
            if not data:
                break

    def run(self):
        client, address = self.s.accept()
        cThread = threading.Thread(target=self.handler, args=(client, address))
        cThread.daemon = True
        cThread.start()
        self.connections.append(client)
        print(self.connections)

server = Server()
server.run()
