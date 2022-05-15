import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

s.bind((port, ))