import paramiko

hostname = "192.168.15.130"   
username = "zodoso"
password = "1234"
port = 22

try:
    p = paramiko.Transport((hostname, port))
    p.connect(username=username, password=password)
    print("[*] Connected to " + hostname)
    sftp = paramiko.SFTPClient.from_transport(p)
    print("[*] Starting file download")
    sftp.get("/home/zodoso/test.txt", "/Users/INET USER/Desktop/d.txt")
    print("[*] File downloaded")
    print("[*] Starting file upload")
    sftp.put("/Users/INET USER/Desktop/d.txt", "/home/zodoso/u.txt")
    print("[*] File uploaded")
    p.close()
    print("[*] Closed connection")

except Exception as err:
    print(str(err))