import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 12345))
sock.setblocking(0)

data = 'foobar\n' * 10 * 1024 * 1024 # 70 MB of data
sent = sock.send(data.encode())
assert sent == len(data), '%s != %s' % (sent, len(data))