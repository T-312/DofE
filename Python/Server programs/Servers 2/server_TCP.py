import socket, threading, random, string

HEADER = 64
FORMAT = 'utf-8' 
welcome_msg = "Welcome on Tim's server!"
instructions = "\nPlease choose from the following:\n 1) Calculate a maths problem\n 2) Generate a password\n 3) IDK\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
host = socket.gethostbyname(socket.gethostname())

def handle_client(client_socket, client_addr):
    print(f"<System> Client {client_addr} has successfuly connected to the server!")
    connected = True
    client_socket.send(welcome_msg.encode(FORMAT))
    client_socket.send(instructions.encode(FORMAT))
    
    while connected:
        msg_len = client_socket.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = client_socket.recv(msg_len).decode(FORMAT)

            if msg == "exit":
                connected = False
                print(f"<System> Client {client_addr} has successfully disconnected!")
                
            elif msg == "1" or '+' in [i for i in msg] or '-' in [i for i in msg] or '*' in [i for i in msg] or '/' in [i for i in msg]:
                if msg == "1":
# Fix SyntaxError - if it occurs, tell the user to rewrite the question
                    client_socket.send("Send a math question".encode(FORMAT))
                if len(msg) > 1:
                    ans = str("Answer: " + str(eval(msg)) + "\n")
                    client_socket.send(ans.encode(FORMAT))
                    client_socket.send(instructions.encode(FORMAT))
            
            elif msg == "2":
                letters = list(string.ascii_letters)
                nums = list(range(0, 10))
                for i in nums: letters.append(str(i))
                passwd = []
                while len(passwd) < 8:
                    passwd.append(random.choice(letters))

                passwd = ''.join(passwd)
                client_socket.send(passwd.encode(FORMAT))

            elif msg == "3":
                pass

            else:    
                print(f"<{client_addr}> {msg}")
        
    client_socket.close()

def start():
    s.bind((host, port))
    print(f"<System> Starting server on {host}...")
    s.listen()
    while True:
        client_socket, client_addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
        thread.start()
        print(f"<System> Clients on server: {threading.activeCount() - 1}")

start()