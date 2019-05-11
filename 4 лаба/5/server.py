import socket


def op(matrix):
	return matrix[0] * matrix[3] - matrix[1] * matrix[2] 


sock = socket.socket()
sock.bind(('', 5000))
sock.listen()
connection, addr = sock.accept()
matrix = connection.recv(128).decode().strip().split(' ')
matrix = [int(x) for x in matrix if x.isdigit()]
matrix = [x*op(matrix) for x in matrix]
connection.send(str(matrix).encode())