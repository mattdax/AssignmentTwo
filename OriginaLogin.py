#Import Statements
from tkinter import * #Tkinter for GUI
import socket #Sockets used for networking aspect of assignment

#Target location of connection
host = '10.10.18.234'
port = 443
buffer = 1024

#The main Client class
class Client():
    #Init function, ran on start up
    def __init__(self):
        try:
            #Attempts to connect to server and opens login window
            self.connect()
            self.loginScreen()
            #Error window if cannot connect to server
        except ConnectionRefusedError:

            #Creates error window
            self.error = Tk()

            #Error window setups
            self.error.geometry("300x100")
            self.error.title("Assignment 2")

            #Error label
            self.errorMessage = Label(self.error,text = "Could not connect to server\n Please try again later.",font = ('Helvetica', 14))
            self.errorMessage.pack()

            #Error window loop
            self.error.mainloop()

        #Login screen that first asks user if they are new or returning
    def loginScreen(self):
        #Creates window
        self.screenA = Tk()

        #Setup variables
        self.screenA.geometry("250x200")
        self.screenA.title("Assignment 2")

        #Label
        self.account = Label(self.screenA,text = "Do you have an account already?")
        self.account.pack(side = TOP)


        #Yes and No buttons
        self.loginOption = Button(self.screenA,text = "Yes", command = self.login())
        self.loginOption.pack(side = (BOTTOM))
        self.newOption = Button(self.screenA,text = "No",command = self.newAccount())
        self.newOption.pack(side = (BOTTOM))

        #Window loop
        self.screenA.mainloop()

    def login(self):
        print()
    def newAccount(self):
        print()
    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))

Client().__init__()
