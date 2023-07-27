import logging
import socket

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

#Blocking
def create_blocking(host,ip):
    logging.info('Blocking - creating socket')
    s = scoket.socket(socket.AF_INET, socket.SOCK_STREAM)

    logging.info('Blocking - connecting')
    s.connect((host,ip))

    logging.info('Blocking - connected')
    logging.info('Blocking - sending...')
    s.sendall(b'Hello, world')

    logging.info('Blocking - waiting...')
    data = s.recv(1024)
    logging.info('Blocking - data= : {len(data)}')
    logging.info('Blocking - closing')
    s.close()

def main():
    create_blocking('voldrealms.com')

    if __name__ == '__main__':
        main()