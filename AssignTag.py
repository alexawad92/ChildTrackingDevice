import tkinter as tk
from tkinter import messagebox
from tkinter import *
from DBNode import DBNode
class AssignTag:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        TagNumber = tk.Label(self.frame, text="Tag Number")
        TagNumber.pack(side= tk.TOP)
        self.TagNumberEntry  = tk.Entry(self.frame, width=10)
        self.TagNumberEntry.pack()
        self.frame.pack()
        CamperName = tk.Label(self.frame, text="Camper Name")
        CamperName.pack(side= tk.TOP)
        self.CamperNameEntry  = tk.Entry(self.frame, width=10)
        self.CamperNameEntry.pack()
        self.frame.pack()
        self.Assign = tk.Button(self.frame, text = 'Assign', width = 25, command = self.Assign)
        self.Assign.pack()
        self.frame.pack()
        self.ExitButton = tk.Button(self.frame, text = 'Exit', width = 25, command = self.close_windows)
        self.ExitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def Assign(self):
        TagNumber = self.TagNumberEntry.get()
        CamperName = self.CamperNameEntry.get()
        self.TagNumberEntry.delete(0, len(TagNumber))
        self.CamperNameEntry.delete(0, len(CamperName))
        DBObj = DBNode("402DB", "123456", "Test")
        DBObj.AssignTag(TagNumber, CamperName)        
##        def Register(self):
##        TagNumber = self.TagNumberEntry.get()
##        Active_start = self.ActiveDateEntry.get()
##        Active_end = self.EndDateEntry.get()
##        Active_Flag = self.ActiveFlagEntry.get()
##        self.TagNumberEntry.delete(0, len(TagNumber))
##        self.ActiveDateEntry.delete(0, len(Active_start))
##        self.EndDateEntry.delete(0, len(Active_end))
##        self.ActiveFlagEntry.delete(0, len(Active_Flag))
##
##        DBObj = DBNode("root", "Ih821hwt", "Test")
##        DBObj.InsertToTag(TagNumber, Active_start, Active_end, Active_Flag)
##        content = tk.StringVar()
##        WELCOME_MSG = TagNumber + ''' Tag has been registered.
##        Thank You!'''
##        WELCOME_DURATION = 3000
##        top = tk.Toplevel()
##        top.title('Tag Registration')
##        Message(top, text=WELCOME_MSG, padx=20, pady=20).pack()
##        top.after(WELCOME_DURATION, top.destroy)
