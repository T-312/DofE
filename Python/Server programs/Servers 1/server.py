import socket, threading, datetime

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

def handle_client():
    pass

running = True
while running:
    client_addr, client_ip = server.accept()