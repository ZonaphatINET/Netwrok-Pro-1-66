import socket
import threading

def handle_client(conn, addr):
    print("Connected by: " + str(addr))
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

def start_server():
    host = "127.0.0.1"
    port = 8066

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server is listening on port " + str(port))

    while True:
        conn, addr = server_socket.accept()
        # สร้างเธรดสำหรับแต่ละการเชื่อมต่อ
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
