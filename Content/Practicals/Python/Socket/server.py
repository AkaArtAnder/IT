import socket

if __name__ == "__main__":
	serverSocket = socket.socket()
	serverSocket.bind(('', 9999))
	serverSocket.listen()

	print("Server listen port: " + "9999")


	while(True):
		clientSocket,addr = serverSocket.accept()

		print("Client connected: {0}".format(addr))
		
		while(True):
			data = clientSocket.recv(1024).decode()
			if not data:
				break
			print("Client data: " + data)
			clientSocket.send("Hello client".encode())
