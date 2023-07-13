import socket

host = "127.0.0.1"
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(5)
    print("Server is listening on port " + str(port))
    conn, addr = s.accept()
    with conn:
        print("Connected by: " + str(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)