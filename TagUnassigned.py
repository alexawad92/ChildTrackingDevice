import tkinter as tk
from tkinter import messagebox
from tkinter import *
from DBNode import DBNode
class TagUnassigned:
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
        self.UnAssign = tk.Button(self.frame, text = 'Unassign', width = 25, command = self.Unassign)
        self.UnAssign.pack()
        self.frame.pack()
        self.ExitButton = tk.Button(self.frame, text = 'Exit', width = 25, command = self.close_windows)
        self.ExitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
    def Unassign(self):
        TagNumber = self.TagNumberEntry.get()
        CamperName = self.CamperNameEntry.get()
        self.TagNumberEntry.delete(0, len(TagNumber))
        self.CamperNameEntry.delete(0, len(CamperName))
        DBObj = DBNode("402DB", "123456", "Test")
        DBObj.UnAssignTag(TagNumber, CamperName)        
