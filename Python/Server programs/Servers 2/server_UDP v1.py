import socket
import ctypes, os
import webbrowser
#Maybe add an excel log?

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 1234
host = socket.gethostbyname_ex(socket.gethostname())

s.bind(("192.168.50.190", port))

while True:
    try:
        data = s.recv(2048).decode('utf-8').lower()

    except KeyboardInterrupt or data == "exit":
        s.close()
        break

    else:
        if data == "conn": # Add list of commands through print statement on clients side
            print("<------------------------------------------->")
            print(f"<System> Connection with {client_ip} successful...")

        elif data.count(".") == 3:
            client_ip = data

        elif data == "discon":
            print(f"<System> {client_ip} has successfully disconnected...")
            print("<------------------------------------------->")

        elif data == "lock":
            print("<System> Lock has been initiated...")
            ctypes.windll.user32.LockWorkStation()

        elif data == "shutdown":
            print("<System> Shutdown has been initiated...")
            os.system("shutdown /s /t 1")

        elif data == "yt":
            print("<Client> Starting YouTube...")
            webbrowser.open("https://youtube.com")

        elif data == "gl":
            print("<Client> Starting Google...")
            webbrowser.open("https://google.com")

        elif data == "ig":
            print("<Client> Starting Instagram...")
            webbrowser.open("https://instagram.com")