import tkinter as tk
from tkinter import messagebox
from tkinter import *
from DBNode import DBNode
class TagReg:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        TagNumber = tk.Label(self.frame, text="Tag Number")
        TagNumber.pack(side= tk.TOP)
        self.TagNumberEntry  = tk.Entry(self.frame, width=10)
        self.TagNumberEntry.pack()
        self.frame.pack()
        ActiveDate = tk.Label(self.frame, text="Active Start (yyyy-mm-dd), CURDate By default")
        ActiveDate.pack(side= tk.TOP)
        self.ActiveDateEntry  = tk.Entry(self.frame, width=10)
        self.ActiveDateEntry.pack()
        self.frame.pack()
        EndDate = tk.Label(self.frame, text="Active End (Optional)")
        EndDate.pack(side= tk.TOP)
        self.EndDateEntry  = tk.Entry(self.frame, width=10)
        self.EndDateEntry.pack()
        self.frame.pack()
        ActiveFlag = tk.Label(self.frame, text="Active Flag ('Y'/'N')")
        ActiveFlag.pack(side= tk.TOP)
        self.ActiveFlagEntry  = tk.Entry(self.frame, width=10)
        self.ActiveFlagEntry.pack()
        self.frame.pack()
        self.Back = tk.Button(self.frame, text = 'Register', width = 25, command = self.Register)
        self.Back.pack()
        self.frame.pack()
        self.ExitButton = tk.Button(self.frame, text = 'Exit', width = 25, command = self.close_windows)
        self.ExitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
    def Register(self):
        TagNumber = self.TagNumberEntry.get()
        Active_start = self.ActiveDateEntry.get()
        Active_end = self.EndDateEntry.get()
        Active_Flag = self.ActiveFlagEntry.get()
        self.TagNumberEntry.delete(0, len(TagNumber))
        self.ActiveDateEntry.delete(0, len(Active_start))
        self.EndDateEntry.delete(0, len(Active_end))
        self.ActiveFlagEntry.delete(0, len(Active_Flag))

        DBObj = DBNode("root", "Ih821hwt", "Test")
        DBObj.InsertToTag(TagNumber, Active_start, Active_end, Active_Flag)
        content = tk.StringVar()
        WELCOME_MSG = TagNumber + ''' Tag has been registered.
        Thank You!'''
        WELCOME_DURATION = 3000
        top = tk.Toplevel()
        top.title('Tag Registration')
        Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
        top.after(WELCOME_DURATION, top.destroy)
