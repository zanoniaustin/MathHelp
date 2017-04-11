#pyUi
from tkinter import *
import tkinter as tk
import tkinter.messagebox
 
class reepsButtons(tk.Frame):
	def __init__(self,master=None):
		Frame.__init__(self)
		self.master.minsize(width=400, height=350)
		self.master.title("Math Help")
		self.grid()
		self.math_dict=dict()
		#Buttons(self, frame)
		
		self.mainmsg = Message(self, text="Welcome to Math Help! Please select a level!")
		self.mainmsg.grid(row=1,columnspan=8,sticky=N)
		
		self.L1Button = Button(self,text="Level 1", command=self.Level)
		self.L1Button.grid(row=2)
		self.L1text= Label(self, text="Addition and Subtraction")
		self.L1text.grid(row=2,column=5)
		
		self.L2Button = Button(self,text="Level 2", command=self.Level)
		self.L2Button.grid(row=10)
		self.L2text= Label(self, text="Multiplication and Division")
		self.L2text.grid(row=10,column=5)
		
		self.L3Button = Button(self,text="Level 3", command=self.Level)
		self.L3Button.grid(row=15)
		self.L3text= Label(self, text="Multiplication")
		self.L3text.grid(row=15,column=5)
		
		self.L4Button = Button(self,text="Level 4", command=self.Level)
		self.L4Button.grid(row=70)
		self.L4text= Label(self, text="Exponents")
		self.L4text.grid(row=11,column=5)
		
		self.quitButton = Button(self, text="Quit", command = master.destroy)
		self.quitButton.grid(sticky=S)
	def Level(self):
		
		L1 = tk.Toplevel()
		L1.minsize(height=200, width=200)
		L1.maxsize(height=800, width = 600)
		L1.title("Addition and Subtraction")		
		
		L1.prob = ''
		L1.prob = self.PrintProblem(0)
		L1.Problem = Label(L1, text=L1.prob)
		L1.Problem.pack()
		L1.Answer = StringVar()
		
		L1.e = Entry(L1, width=20, textvariable=L1.Answer)
		L1.e.pack(side=LEFT)		
	
		L1.b = Button(L1, text="Check Answer", width=10, command=lambda: self.CheckAnswer(L1))
		L1.b.pack(side=LEFT)
		
		L1.button = Button(L1, text="Quit", command = L1.destroy)
		L1.button.pack(side=BOTTOM)
	def CheckAnswer(self, L1):
		ans = eval(L1.prob)
		print(ans)
		print(L1.Answer.get())
		if str(ans) == L1.Answer.get():
			right = tkinter.messagebox.showinfo("Your answer was... ","Correct!")
			#right.minsize(width=200, height =200)
		else:
			wrong = tkinter.messagebox.showinfo("Your answer was...","Incorrect!")
			#wrong.minsize(width=200,height=200)
	def PrintProblem(self,num):
		if num == 0:
			return "9 + 7"
		elif num == 1:
			pass
		elif num == 2:
			pass
		else:
			pass
root = Tk()
root.title("Math Help")
#root.geometry('{450}x{500}'.format(<500>,<450>))
b = reepsButtons(root)
root.mainloop()

