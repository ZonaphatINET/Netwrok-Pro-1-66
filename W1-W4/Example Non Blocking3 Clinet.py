import socket
import select
import errno

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 12345))
sock.setblocking(0)

data = 'foobar\n' * 1024 * 1024
dara_size = len(data)
print('Bytes to send: ', len(data))

total_sent = 0
while len(data):
    try:
        sent = sock.send(data.encode())
        total_sent += sent
        data = data[sent:]
    except socket.error as e:
        if e.errno != errno.EAGAIN:
            raise e
        print('Blocking with', len(data), 'remaining')
        select.select([], [sock], [])  #This blocks until

assert total_sent == dara_size # True