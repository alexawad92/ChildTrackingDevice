import tkinter as tk
from tkinter import *
from DBNode import DBNode as node

class Showl():
    def __init__(self, master, ROOM_ID):
        self.master = master
        self.frame = tk.Frame(self.master)
        #self.name = id
        listbox = Listbox(master)
        listbox.pack()
        DBObj = node("root", "Ih821hwt", "Test")
        ppl = DBObj.Present(ROOM_ID)
        print(ppl)
        for item in ppl: 
            listbox.insert(END, item)
            
    def close_windows(self):
        self.master.destroy()
