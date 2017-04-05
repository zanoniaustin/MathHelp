#pyUi
from tkinter import *
import tkinter as tk

 
class reepsButtons(tk.Frame):
	def __init__(self,master=None):
		master.minsize(width=400, height=350)
		frame = Frame(master)
		frame.pack()
		#Buttons(self, frame)
		
		self.mainmsg = Message(frame, text="Welcome to Math Help! Please select a level!")
		self.mainmsg.grid(row=1,columnspan=8,sticky=N)
		
		self.L1Button = Button(frame,text="Level 1", command=self.Level)
		self.L1Button.grid(row=2)
		self.L1text= Label(frame, text="Addition")
		self.L1text.grid(row=2,column=5)
		
		self.L2Button = Button(frame,text="Level 2", command=self.Level)
		self.L2Button.grid(row=5)
		self.L2text= Label(frame, text="Subtraction")
		self.L2text.grid(row=5,column=5)
		
		self.L3Button = Button(frame,text="Level 3", command=self.Level)
		self.L3Button.grid(row=8)
		self.L3text= Label(frame, text="Multiplication")
		self.L3text.grid(row=8,column=5)
		
		self.L4Button = Button(frame,text="Level 4", command=self.Level)
		self.L4Button.grid(row=11)
		self.L4text= Label(frame, text="Division")
		self.L4text.grid(row=11,column=5)
		
		self.quitButton = Button(frame, text="Quit", command = master.destroy)
		self.quitButton.grid(sticky=S)
		
	def Level(self):
		level_1 = tk.Toplevel()
		level_1.title("Addition and Subtraction")
		msg = Message(level_1,text="HI")
		msg.pack(side=LEFT)
		button = Button(level_1, text="Quit", command = level_1.destroy)
		button.pack()
		
		
root = Tk()
root.title("Math Help")
#root.geometry('{450}x{500}'.format(<500>,<450>))
b = reepsButtons(root)
root.mainloop()

