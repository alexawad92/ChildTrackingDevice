import tkinter as tk
from tkinter import messagebox
import showl as show
from DBNode import DBNode as node

class Registered:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        DBObj = node("root", "Ih821hwt", "Test")
        rooms = DBObj.Rooms()
        for name in rooms:
            self.add_room(str(name))
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
    def print_t(self, name):
        self.newWindow = tk.Toplevel(self.master)
        self.app = show.Showl(self.newWindow, name)
    def add_room(self, name):
        name = name[2:-3]
        self.name = tk.Button(self.frame, text = name, width = 25, command = lambda: self.print_t(name))
        self.name.pack()
