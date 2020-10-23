from tkinter import *    

class Login:
	def __init__(self, contentFrame, screens):
		self.contentFrame = contentFrame
		self.screens = screens	
	
	def loginClear(self): # clear the input text to need to reenter
		self.inputPass.delete(0,END)


	def loginDisplay(self):
		self.labelName = Label(self.contentFrame, text ="Enter Username: ")
		self.labelName.pack()
		self.inputName = Entry(self.contentFrame)
		self.inputName.pack()
		self.labelPass = Label (self.contentFrame, text="Exter Password: ")
		self.labelPass.pack()
		self.inputPass = Entry(self.contentFrame, show="*")
		self.inputPass.pack()
		self.message = Label(self.contentFrame, text="")
		self.message.pack()
		self.loginBtn = Button(self.contentFrame, text ="Login", command = self.loginGo)
		self.loginBtn.pack()
		self.registerBtn = Button(self.contentFrame, text ="Register new user", command = self.registerScreen) ### need to do a registration screen!
		self.registerBtn.pack()
		self.fubar = Label(self.contentFrame, text="for testing use name 'k' and the pass 'j' - anything else will give error")
		self.fubar.pack()


	def loginGo(self):
		#### obviously you need to check with real usernames that you store on file


		if (self.inputName.get() != "k") or (self.inputPass.get()!="j"):
			self.message.configure(text="you entered INVALID login info!")
			self.loginClear() # dont leave pass entered, but we leave the username
		else:
			self.screens.mainScreen()  #This interacts with screens.py in the main.py file @ where .mainScreen() comes from
			

##NEW STUFF NOT DEBUGGED \/

	def registerScreen(self):
		self.registerText = Label(self.contentFrame, text ="Register a new user").pack()
		self.newNameLabel = Label(self.contentFrame, text ="Enter New Username: ").pack()
		self.newNameEntry = Entry(self.contentFrame).pack()  			##Have to save this entry into a text file somehow
		self.newPassLabel = Label(self.contentFrame, text="Enter Password: ").pack()
		self.newPassEntry = Entry(self.contentFrame, show="*").pack()  #have to save this password into a text file too 
		self.newPassLabel2 = Label(self.contentFrame, text="Reenter Password: ").pack()
		self.newPassEntry2 = Entry(self.contentFrame, show="*").pack()  #have to save this password into a text file too 
		self.registerMessage = Label(self.contentFrame, text="").pack()
		self.registerBtn = Button(self.contentFrame, text ="Enter", command = self.registerGo).pack()

	def registerGo(self):
		# file = askopenfile(mode='a+',filetypes=[('Text Files','users.txt')])
		# lines = file.read()
		# rows = 0
        # lineList = lines.split("\n") #makes a list
		if self.newPassEntry.get() == self.newPassEntry2.get():
			self.regMessage.configure(text="Passwords do match")
       	# 	for i in lineList:
        #     	rows += 1

        # 	if (rows < 10): # append the new password and username
        #     	file.write(self.newNameEntry.get() + '\t') #uName and pass split with a tab
        #     	file.write(self.newPassEntry.get() + "\n")
        #     	file.close()

        # 	else: 
        #     	file.close()
		# 		self.registerMessage.configure(text="max number of useres has already been registered")
            #send error message that there is already 10 users ('max number of users has been registered')



		# else:
		# 	self.regMessage.configure(text="Passwords do not match")

	