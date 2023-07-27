import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 1239))

data = 'foodbar\n' * 10 * 1024 * 1024 # 70 MB of data
assert sock.send(data) == len(data) # true