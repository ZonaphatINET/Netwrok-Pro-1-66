import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 12345 if len(sys.argv) < 2 else int(sys.argv[1])
sock.bind(('localhost', port))
sock.listen(5)

try:
    while True:
        conn, info = sock.accept()

        data = conn.recv(1024)
        while data:
            conn.send(data)
            data = conn.recv(1024)
except KeyboardInterrupt:
    sock.close()