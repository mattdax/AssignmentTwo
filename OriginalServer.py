#Import statements
import socket
import _thread

#Setup Variables
IP = "10.10.18.234"
port = 443
Buffer = 1024


#Beginning search for clients
print("Looking for Connections...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,port))
s.listen(5)
conn, addr = s.accept()

#Function for receiving messages from client
def Messages(Buffer):
    #Prints the connecting address, of the client
    print("Connection Address: ",addr)
    while True:
        data = conn.recv(Buffer)
        #Decodes the encrypted data
        message = data.decode('utf-8')
        #If client types "quit" the server shuts down
        if message == "Quit":
            conn.close()
            raise SystemExit
        else:
            print("Data:", message)

#Introduction to threading, still learning about this
_thread.start_new_thread(Messages ,(Buffer, ))

#Runs the program
while 1:
    pass


