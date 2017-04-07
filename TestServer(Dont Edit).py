import socket
IP = "10.10.18.234"
port = 443
Buffer = 1024
print("Looking for Connections...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,port))
s.listen(5)
conn, addr = s.accept()

while True:
    data = conn.recv(Buffer)
    # Decodes the encrypted data
    message = data.decode('utf-8')
    # If client types "quit" the server shuts down
    if message == "Quit":
        conn.close()
        raise SystemExit
    else:
        print("Data:", message)