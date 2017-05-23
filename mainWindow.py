from tkinter import *

def GUI():
    class Window():
        def __init__(self):
            #creating the window and setting its characteristics
            self.Window= Tk()
            self.Window.geometry("400x400")

            #creating a list of people who the client can connect to and letting them pick which one they want to connect to
            self.header = Label(self.Window, bd=0, bg="white", height="1", width="37", font="Arial",text='Connect To A User:')
            self.header.grid(row=0,column=0,columnspan=5)



            self.user1=Label(self.Window, bd=0,font="Arial",text="hey")
            self.user1.grid(row=1, column=1, sticky= W)

            userlist=['riaz','matt']
            userLabelList=[]

            for i in range(0, len(userlist),1):
                userLabelList.append(Label(self.Window, bd=0,font="Arial",text=userlist[i]))
                userLabelList[i].grid(row=i+1,column=1, sticky= W)
                self.connectButton1 = Button(self.Window, text="Connect", command=self.connect(i))
                self.connectButton1.grid(row=i+1, column=4, columnspan=1, sticky=W)

            self.refresh=Button(self.Window, text='Refresh', command= self.refresh())
            self.refresh.grid(row=4, column=4, columnspan=1, sticky=W)

            # looping the window so that it will continue to stay open
            #self.text1.delete(1.0, END)

            self.Window.mainloop()

        def refresh(self):
            print("hi")

        def connect(self, user):
            #open the chat window
            None
    Window()


GUI()
