#Echo Client program
import socket 
HOST = '10.4.15.99'
PORT = 50009
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello World')
    data = s.recv(1024)
print('Received', repr(data))