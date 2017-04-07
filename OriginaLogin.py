from tk\inter import *
import socket
import time
from _thread import start_new_thread
host = '10.10.18.234'
port = 443
buffer = 1024
class Client():
    def __init__(self):
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server.connect((host,port))
            self.loginScreen()
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

    def loginScreen(self):
        self.screenA = Tk()

        self.screenA.geometry("250x200")
        self.screenA.title("Assignment 2")

        self.account = Button(self.screenA,text = "Do you have an account already?",font = ('Helvetica', 14))
        self.account.pack(side = TOP)




Client()
