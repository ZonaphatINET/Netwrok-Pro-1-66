import socket

try:
    print("Fully qualifen doain name: " + socket.getfqdn("8.8.8.8"))
    print("Host name to IP address: " + socket.gethostbyname("www.python.org"))
    print("Host name to IP address, extended" + str(socket.gethostbyname_ex("www.python.org")))
    print("Get host name of local machine: " + socket.gethostbyname())
except Exception as err:
    print("Errer: " + str(err))