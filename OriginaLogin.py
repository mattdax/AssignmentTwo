#Import Statements
from tkinter import * #Tkinter for GUI
import socket #Sockets used for networking aspect of assignment
import base64
import _thread
# Setup Variables
programName = "Project Mercury"

#Target location of connection
host = '10.10.1.19'
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

        #Screen settings
        self.screenC.geometry("300x400")
        self.screenC.title(programName)

        #Top Label
        self.creationLabel = Label(self.screenC,text = "Complete the fields below to create an account")
        self.creationLabel.pack(side = TOP,pady = 5)

        #Username Creation
        self.usernameCreation = Label(self.screenC,text = "Enter your username:")
        self.usernameCreation.pack(side = TOP,pady = 5)

        self.usernameCreationEntry = Entry(self.screenC)
        self.usernameCreationEntry.pack(side = TOP, pady = 3)

        # Email Creation
        self.email = Label(self.screenC,text = "Enter your email: ")
        self.email.pack(side = TOP, pady = 3)

        self.email = Entry(self.screenC)
        self.email.pack(side = TOP,pady = 3)


        # Password Creation
        self.passwordCreation = Label(self.screenC,text = "Enter your password: ")
        self.passwordCreation.pack(side = TOP, pady = 3)

        self.passwordCreationEntry = Entry(self.screenC)
        self.passwordCreationEntry.pack(side = TOP,pady = 3)

        #Re-enter password
        self.repassword = Label(self.screenC, text = "Re-enter your password: ")
        self.repassword.pack(side = TOP,pady = 3)

        self.repasswordEntry = Entry(self.screenC)
        self.repasswordEntry.pack(side = TOP, pady = 3)

        # Create Button
        signup = Button(self.screenC,text = "Create",command = self.getCreation)
        signup.pack(side = TOP,pady = 3)

        #Window Loop
        self.screenC.mainloop()
        exit()

    def getCreation(self):
        username = self.usernameCreationEntry.get()
        password = self.passwordCreationEntry.get()
        email = self.email.get()
        repassword = self.repasswordEntry.get()
        # If re-entering the password does not work
        if password != repassword:
            #Creates error window
            self.passwordMatch = Tk()
            self.screenC.destroy()
            #Setup variables
            self.passwordMatch.geometry("300x200")
            self.passwordMatch.title(programName)
            # Error label
            self.match = Label(self.passwordMatch,text = "Passwords do not match")
            self.match.pack(side = TOP)

            #Window loop
            self.passwordMatch.mainloop()
            self.newAccount()

        if username == "" or password == "" or email == "":
            # Creates error window
            self.usernameMatch = Tk()
            self.screenC.destroy()
            # Setup variables
            self.usernameMatch.geometry("300x200")
            self.usernameMatch.title(programName)
            # Error label
            self.match = Label(self.usernameMatch, text="One of the fields has been left empty")
            self.match.pack(side=TOP)

            # Window loop
            self.usernameMatch.mainloop()
            self.newAccount()

    #Function the begins connection with the server

    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))
       # client = self.server.accept()

    def sendinfo(self):
        self.username = "@"+self.usernameEntry.get()
        self.password = "@"+self.passwordEntry.get()
        print(self.username,self.password)

    """"def loadingMessages(self):
        print("started")
        data = ""
        while data == "":
            try:
                data = self.server.recv(buffer)
                print(data.decode('utf-8'))
            except AttributeError:
                print("did not work")
                break
                """

Client().__init__()

