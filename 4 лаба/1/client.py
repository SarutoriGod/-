import socket


sock = socket.socket()
sock.connect(('127.0.0.1', 5000))
message = input('')
sock.send(message.encode())
print((sock.recv(128)).decode())
sock.close()
