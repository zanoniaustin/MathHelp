from tkinter import *
import tkinter as tk
import tkinter.messagebox
import random
from tkinter.ttk import *
from subprocess import call

TITLE_FONT = ("Courier New", 18, "bold")
SUBTITLE_FONT =("Courier New", 15, "bold")
APP_FONT = ('Courier New', 12)



class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Math Help")
        self.geometry("600x600+250+50")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.config(width=400, height=400)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MathHelp, Level1):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MathHelp")


        btn_exit = tk.Button(self, text = "Exit", fg = "black", bg = "white", command = exit, font=APP_FONT)
        btn_exit.pack()
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MathHelp(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.title = tk.Label(self, text = "Welcome To Math Help", font=TITLE_FONT)
		self.title.pack(side='top', fill='x', pady=10)
		self.select = tk.Label(self, text="Select a Level to Begin", font=SUBTITLE_FONT)
		self.select.pack(side="top", fill="x")
		self.book = tk.Label(self, text="", font=SUBTITLE_FONT)
		self.book.pack(side="top", fill="x")

		self.L1Button = Button(self,text="Level 1",command=lambda: controller.show_frame("Level1"))
		self.L1Button.pack()

		self.L2Button = Button(self,text="Level 2")
		self.L2Button.pack()

		self.L3Button = Button(self,text="Level 3")
		self.L3Button.pack()

		self.L4Button = Button(self,text="Level 4")
		self.L4Button.pack()


class Level1(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
	#	self.geometry("600x600+250+50")
		self.controller = controller
		label = tk.Label(self, text="Addition and Subtraction", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		self.Answer = StringVar()
		e = Entry(self, width=20, textvariable=self.Answer)
		e.pack(side=LEFT)
		b = Button(self, text="Check Answer",command=lambda: self.CheckAnswer())
		b.pack(side=LEFT)
		self.Problem=''
		self.Solution=''

		self.run()

	def CheckAnswer(self):
		print(self.Answer.get())
		print(self.Solution)
		if int(self.Answer.get()) == int(self.Solution):
			right = tkinter.messagebox.showinfo("Your answer was... \n","Correct!")
			self.run()
		else:
			right = tkinter.messagebox.showinfo("Your answer was... \n","Incorrect!")

	def run(self):
		self.SetProblem()
		print(self.Problem)
		print(self.Solution)
		self.PrintProblem()


	def SetProblem(self):
		num1=random.randrange(-51,51,1)
		num2=random.randrange(-51,51,1)
		add_sub = random.randrange(0,2,1)
		if add_sub == 0:
			self.Solution=num1+num2
			self.Problem =  str(num1)+" + "+str(num2)+' = '
		else:
			self.Solution=num1+num2
			self.Problem  =str(num1)+" + "+str(num2)+' = '

	def PrintProblem(self):
		self.p = tk.Label(self, text=self.Problem, font=TITLE_FONT)
		self.p.pack()


class Level2(tk.Frame):
	Problem = ""
	Solution = ""
	UserAnswer=""
	def __init__(self, parent,controller):
		tk.Frame.__init__(self)
		self.controller = controller
		print("HERE")
		self.config(width=400,height=350)
		self.title("Multiplication and Division")

if __name__=="__main__":
	root = App()
	root.mainloop()
