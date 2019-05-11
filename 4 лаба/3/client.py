import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 5000))
matrix = ''
for i in range(1,4):
	print("Введите ", i, " строчку: ")
	matrix += input() + ';'


sock.send(matrix.encode())
print((sock.recv(128).decode()))