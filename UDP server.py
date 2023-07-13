import socket

host = "127.0.0.1"
port = 8086

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))
print("Server is listening on port " + str(port))

while True:
    data, client_address = server_socket.recvfrom(1024)
    print("Received data from", client_address, ":", data.decode())