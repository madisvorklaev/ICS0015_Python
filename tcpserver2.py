import socket
import threading

def Main():
	host = '127.0.0.1'
	port = 5000

class Server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print('Server Running.....')
	s.listen(1)
	client, address = s.accept()
	print('Connection from: ', str(address))
	while True:
		data = client.recv(1024).decode('utf-8')
		if not data:
			break
		print('from connected user: ' + data)
		data = data.upper()
		print('sending: ' + data)
		client.send(data.encode('utf-8'))
	client.close()

if __name__ == '__main__':
    Main()
