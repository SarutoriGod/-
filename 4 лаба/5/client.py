import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 5000))
matrix = ''
for i in range(0,2):
	print("Введите ", i+1, " строку: ")
	matrix += input() + ' '
sock.send(matrix.encode())
print(sock.recv(128).decode())