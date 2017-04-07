from tkinter import *
import socket
import time
from _thread import start_new_thread
host = '10.10.18.234'
port = 443
buffer = 1024
class Client():
    def __init__(self):
        self.bootup = Tk()

        # Setup variables
        self.bootup.geometry("500x100")
        self.bootup.title("Assignment 2")

        # Connecting Label
        self.firstText = Label(self.bootup,text = "Connecting To Server...\nPlease Wait",font = ('Helvetica', 28))
        self.firstText.pack()
        time.sleep(2)
        try:
            self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server.connect((host,port))
        except ConnectionRefusedError:
            #Destroys other window, may not even popup
            self.bootup.destroy()
            #Creates error window
            self.error = Tk()
            #Error window setups
            self.error.geometry("300x100")
            self.error.title("Assignment 2")

            #Error label
            self.errorMessage = Label(self.error,text = "Could not connect to server\n Please try again later.",font = ('Helvetica', 14))
            self.errorMessage.pack()

            self.quitbutton = Button(self.error,text = "Ok",font = ('Helvetica', 10))
            self.quitbutton.pack(side = BOTTOM)

            #Error window loop
            self.error.mainloop()

        #Main Loop
        self.bootup.mainloop()

    def connecting(self):
        time.sleep(2)




Client().connecting()
