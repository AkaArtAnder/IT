import socket

if __name__ == "__main__":
	clientSocket = socket.socket()
	clientSocket.connect(('', 9999))
	clientSocket.send("Hello server!".encode())
	
	data = clientSocket.recv(1024).decode()  # receive response

	print('Received from server: ' + data)  # show in terminal

	clientSocket.close()  # close the connection