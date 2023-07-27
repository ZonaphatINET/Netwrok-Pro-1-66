import poplib
from email.message import EmailMessage

server = "192.168.15.129"
user = "inet"
passwd = "1234"

server = poplib.POP3_SSL(server)
server.user(user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i+1)[1]:
        print(msg.decode())