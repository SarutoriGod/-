import socket


sock = socket.socket()
sock.bind(('', 5000))
sock.listen()
connection, addr = sock.accept()
saved_message = "До этого у нас ничего не было!"
while True:
	answer = connection.recv(128).decode()
	if answer.upper() == "STOP":
		sock.close()
		break
	connection.send(saved_message.encode())
	saved_message = answer