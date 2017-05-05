import socket
IP = "10.10.19.162"
port = 30000
buffer = 1024
applicationName = "Project Mercury"
	
class Server():
	def __init__(self): 
		print("Trying to Connect...")
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((IP,port))
		self.s.listen(5)
		self.conn, self.addr = self.s.accept()
		print("Connection has been made.")
		self.waitForLogin()



	def waitForLogin(self):
		self.loginstuff = self.conn.recv(buffer).decode('utf-8')
		if self.loginstuff[0] == "#":
			self.createNewLogin()
		else:
			self.verifyLogin()

	def verifyLogin(self):
		print("trying")
		for i in range(0,len(self.loginstuff),1):
			if self.loginstuff[i] == "$":
				self.atpoint = i
		self.username = self.loginstuff[1:self.atpoint]
		self.password = self.loginstuff[self.atpoint+1:]
		self.tocheck = self.username+self.password
		with open("accounts.txt","r") as openfile:
			for line in openfile:
				if self.tocheck in line:
					self.conn.send("LoginIsGood".encode('utf-8'))
				else:
					self.conn.send("LoginIsBad".encode('utf-8'))


	def createNewLogin(self):
		for i in range(0,len(self.loginstuff),1):
			if self.loginstuff[i] == "|":
				self.passwordpoint = i
			if self.loginstuff[i] == ">":
				self.emailpoint = i
		self.usernameCreate = self.loginstuff[1:self.passwordpoint]
		self.passwordCreate = self.loginstuff[self.passwordpoint+1:self.emailpoint]
		self.emailCreate = self.loginstuff[self.emailpoint+1:]
		print(self.usernameCreate,self.passwordCreate,self.emailCreate)
		with open ("accounts.txt","a") as openfile:
			openfile.write(self.usernameCreate+self.passwordCreate)
			openfile.close()
			print("Created new account")

Server().__init__()