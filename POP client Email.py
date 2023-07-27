import poplib
from email.message import EmailMessage

server = "127.0.0.1"
username = "inet"
password = "1234"

server = poplib.POP3_SSL(server)
server.user(username)
server.pass_(password)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i+1)[1]:
        print(msg)