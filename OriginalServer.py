#Import statements
import socket
import _thread

#Setup Variables
IP = "10.10.18.234"
port = 443
Buffer = 1024
applicationName="Assignment 2"
connection=False
passwordVer=False
clientErrorMessage=""
global username
username=""
global password
password=""


#Beginning search for clients
print("Looking for Connections...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP,port))
s.listen(5)
conn, addr = s.accept()
connection=True


#this function will authenticate the username and password of the user
def passwordVerification():

    #waiting for the password to be sent
    while True:
        # waiting for the client to send the username and password
        username, password = conn.recv(Buffer)

        #checking if the string sent by the client starts with '@'. The client attaches an '@' sign to all usernames and
        #password
        if username[0]!="@":
            clientErrorMessage=="notExpectedUsername"

            #sending an error message to the client letting them know why they have been denied access to the chat systems
            conn.send(clientErrorMessage.encode('utf-8'))
            pass

        #checking if a password has been sent by seeing if it has the '@' sign
        if password[0]!='@':
            clientErrorMessage == "notExpectedPassword"

            # sending an error message to the client letting them know why they have been denied access to the chat systems
            conn.send(clientErrorMessage.encode('utf-8'))
            pass

        if username[0]=='@' and password[0]== '@':
            # if both a username and a password has been sent to the server than it will continue with the verification process
            #this will break out of the while loop
            break


        #this is for debugging purposes

        print("The user who is trying to connect:",username)
        print("The password they have entered:",password)


        #we will now call up our username and password dictionairy to verify the users credidentials





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


