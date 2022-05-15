import socket, threading, time

HEADER = 64
FORMAT = 'utf-8'
port = 1234
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.50.190", port))

def rec():
    data = client.recv(2048).decode(FORMAT)
    print(data)

x1 = threading.Thread(target=rec)
x1.start()
x2 = threading.Thread(target=rec)
x2.start()

def send(msg):
    if msg.lower() == "exit":
        message = msg.lower().encode(FORMAT)
        msg_len = len(message)
        send_len = str(msg_len).encode(FORMAT)
        send_len += b' ' * (HEADER - len(send_len))
        client.send(send_len)
        client.send(message)
        client.close()
        exit()

    else:
        message = msg.encode(FORMAT)
        msg_len = len(message)
        send_len = str(msg_len).encode(FORMAT)
        send_len += b' ' * (HEADER - len(send_len))
        client.send(send_len)
        client.send(message)

        x1 = threading.Thread(target=rec)
        x1.start()

while True:
    time.sleep(0.01)
    send(input("Enter message: "))