from time import localtime, strftime
import socket


sock = socket.socket()
sock.bind(('', 5000))
sock.listen()
connection, addr = sock.accept()

if (connection.recv(128)).decode() == "date time":
	connection.send((strftime("%d.%m.%Y %H:%M:%S", localtime())).encode())
else:
	connection.send("Unknown command".encode())