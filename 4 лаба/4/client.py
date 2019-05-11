import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 5000))
while True:
	message = input('Клиент: ')
	sock.send(message.encode())
	if message.upper() == "STOP":
		sock.close()
		break
	print("Сервер: ", (sock.recv(128).decode()))