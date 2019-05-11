import socket


def op(new_matrix):
	return (new_matrix[0][0] * (new_matrix[1][1] * new_matrix[2][2] - new_matrix[2][1] * new_matrix[1][2]) -
		   new_matrix[0][1] * (new_matrix[1][0] * new_matrix[2][2] - new_matrix[2][0] * new_matrix[1][2]) +
		   new_matrix[0][2] * (new_matrix[1][0] * new_matrix[2][1] - new_matrix[2][0] * new_matrix[1][1]))


new_matrix = []
sock = socket.socket()
sock.bind(('', 5000))
sock.listen()
connectrion, addr = sock.accept()
matrix = (connectrion.recv(128)).decode().strip()
matrix = [int(x) for x in matrix if x.isdigit()]
for i in range(0,3):
	new_matrix.append(matrix[i*3:i*3+3:1])
print(new_matrix)
connectrion.send(str((op(new_matrix))).encode())