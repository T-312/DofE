import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostbyname_ex(socket.gethostname())
host = ''.join(host[-1])

port = 1234

client.connect(("192.168.50.190", port))
client.send(host.encode('utf-8'))
client.send("conn".encode('utf-8'))

while True:
    try:
        client_data = input("Enter command: ").lower()
        if client_data == "exit":
            client.send("discon".encode('utf-8'))
            exit()
        
        else:
            client.send(client_data.encode('utf-8'))

    except KeyboardInterrupt:
        client.send("discon".encode('utf-8'))
        exit()