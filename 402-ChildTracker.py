import tkinter as tk
from tkinter import messagebox
from Registration import Registration
import registered as regd
import checkInOut as cIO
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.ttk import *
#import Aboutus as aboutus
from tkinter import Menu 

def notdone():  
    showerror('Not implemented', 'Not yet available') 
class Demo1:
    def __init__(self, master):
        self.master = master
        top = Menu(self.master)       
        self.master.config(menu=top)
        
        file = Menu(top)
        file.add_command(label='New...',  command=notdone,  underline=0)
        file.add_command(label='Open...', command=notdone,  underline=0)
        file.add_command(label='Quit',    command=self.master.quit, underline=0)
        top.add_cascade(label='File',     menu=file,        underline=0)

        edit = Menu(top, tearoff=0)
        edit.add_command(label='Cut',     command=notdone,  underline=0)
        edit.add_command(label='Paste',   command=notdone,  underline=0)
        edit.add_separator()
        top.add_cascade(label='Edit',     menu=edit,        underline=0)

   
        self.frame = tk.Frame(self.master)
        image = Image.open('ch1.png')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image=photo)
        label.image = photo # keep a reference!
        label.pack()
        style = ttk.Style()
        style.map("C.TButton",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'red')]
            )
        self.button1 = ttk.Button(self.frame, text = 'Register',style="C.TButton" , width = 25,command = self.Register)
        self.button2 = ttk.Button(self.frame, text = 'Room Tracking',style="C.TButton" ,width = 25, command = self.Registered)
        #self.button3 = ttk.Button(self.frame, text = 'About us',style="C.TButton" ,width = 25, command = self.Registered)
        self.button4 = ttk.Radiobutton(self.frame, text = 'Check In / Check Out', style = "C.TButton", width = 25, command = self.checkInOut)
        self.button1.pack()
        self.button2.pack()
       # self.button3.pack()
        self.button4.pack()
        self.frame.pack()
    def Register(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Registration(self.newWindow)
    def Registered(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = regd.Registered(self.newWindow)
    def aboutus(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = aboutus.Registrated(self.newWindow)
    def checkInOut(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = cIO.checkInOut(self.newWindow)

def main(): 
    root = tk.Tk()
    root.title("ChildTracker")
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
