import socket

HOST='127.0.0.1'
PORT=9999

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST,PORT))

message = input('-->')
client_socket.sendall(message.encode())

data=client_socket.recv(1024)
print('[ECHO_SERVER]: ', repr(data.decode()))

client_socket.close()