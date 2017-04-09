#Import Statements
from tkinter import * #Tkinter for GUI
import socket #Sockets used for networking aspect of assignment
import _thread
# Setup Variables
programName = "Assignment 2"

#Target location of connection
host = '10.0.1.19'
port = 80
buffer = 1024
#The main Client class
class Client():
    #Init function, ran on start up
    def __init__(self):
        try:
            #Attempts to connect to server and opens login window

            #_thread.start_new_thread(Client.loadingMessages(self), self)

            self.connect()
            self.loginScreen()

            #Error window if cannot connect to server
        except ConnectionRefusedError:

            #Creates error window
            self.error = Tk()

            #Error window setups
            self.error.geometry("300x100")
            self.error.title(programName)

            #Error label
            self.errorMessage = Label(self.error,text = "Could not connect to server\n Please try again later.",font = ('Helvetica', 14))
            self.errorMessage.pack()

            #Error window loop
            self.error.mainloop()
            exit()
        #Login screen that first asks user if they are new or returning
    def loginScreen(self):
        #Creates window
        self.screenA = Tk()

        #Setup variables
        self.screenA.geometry("250x200")
        self.screenA.title(programName)

        #Label
        self.account = Label(self.screenA,text = "Do you have an account already?")
        self.account.pack(side = TOP)


        #Yes and No buttons
        self.loginOption = Button(self.screenA,text = "Yes", command = self.login)
        self.loginOption.pack(side = BOTTOM)
        self.newOption = Button(self.screenA,text = "No",command = self.newAccount)
        self.newOption.pack(side = BOTTOM)

        #Window loop
        self.screenA.mainloop()
        exit()
        #self.screenA.destroy()
    def login(self):
        #Creates the login screen for usernames and password input
        self.screenB = Tk()
        self.screenA.destroy()

        #Usual setup variables
        self.screenB.geometry("250x200")
        self.screenB.title(programName)

        #Intro Label
        self.credentials = Label(self.screenB,text = "Enter your username and password")
        self.credentials.pack(side = TOP,pady = 10)

        #Username Information
        self.usernameLabel = Label(self.screenB,text = "Username:")
        self.usernameLabel.pack(side = TOP, pady= 3)
        self.usernameEntry = Entry(self.screenB)
        self.usernameEntry.pack(side = TOP, pady = 3)

        # Password Information
        self.passwordLabel = Label(self.screenB,text = "Password:")
        self.passwordLabel.pack(side = TOP, pady= 3,)
        self.passwordEntry = Entry(self.screenB,show = '*')
        self.passwordEntry.pack(side = TOP, pady = 3)

        # Login Button
        self.loginButton = Button(self.screenB,text = "Login",command = self.sendinfo)
        self.loginButton.pack(side = TOP,pady = 3)

        #Window loop
        self.screenB.mainloop()
        exit()

    def newAccount(self):
        #Creates the window
        self.screenC = Tk()
        self.screenA.destroy()
        self.screenC.geometry("300x400")
        self.screenC.title(programName)


        self.screenC.mainloop()
        exit()

    #Function the begins connection with the server
    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))
       # client = self.server.accept()

    def sendinfo(self):
        self.username = "@"+self.usernameEntry.get()
        self.password = "@"+self.passwordEntry.get()
        print(self.username,self.password)
    """def loadingMessages(self):
        print("started")
        data = ""
        while data == "":
            try:
                data = self.server.recv(buffer)
                print(data.decode('utf-8'))
            except AttributeError:
                print("did not work")
                break
                """""
Client().__init__()

