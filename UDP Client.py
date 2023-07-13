import socket

host = "127.0.0.1"
port = 8086

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Hello, world"
client_socket.sendto(message.encode(), (host, port))
data, server_address = client_socket.recvfrom(1024)
print("Received response: " + data.decode())

client_socket.close()