import socket


def ur(arr):
	a, b, c, k = int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3])
	if b == 0 or a == 0 or (a + b + c * (k - a / b**3)) == 0:
		return "Деление на ноль невозможно :("
	else:
		return str(abs((a**2 / b**2 + c**2 * a**2)/(a + b + c * (k - a / b**3)) + c + c * (k/b - k/a))).encode()


sock = socket.socket()
sock.bind(('', 5000))
sock.listen()
conn, addr = sock.accept()
arr = conn.recv(128).decode().split(' ')
conn.send(ur(arr))
sock.close()