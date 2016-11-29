import tkinter as tk
from tkinter import messagebox
from RoomReg import RoomReg
from TagReg import TagReg
from CamperReg import CamperReg
from AssignTag import AssignTag
from PIL import Image, ImageTk
from tkinter import ttk

class Registration:
    def __init__(self, master):
        self.master = master
        self.master.title("Registration")
        self.frame = tk.Frame(self.master)
##        self.FacilityButton = tk.Button(self.frame, text = 'Facility Registration', width = 25, command = self.FacilityReg)
##        self.FacilityButton.pack()
##        self.frame.pack()
        image = Image.open('510611_1994_508071.png')
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.frame, image=photo)
        self.label.pack()
        self.frame.pack()
        style = ttk.Style()
        style.map("C.TButton",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'red')]
            )
        self.RoomButton = ttk.Button(self.frame, text = 'Room Registration', style="C.TButton" ,width = 25, command = self.RegRoom)
        self.RoomButton.pack()
        self.frame.pack()
##        self.CaregiverButton = tk.Button(self.frame, text = 'Caregiver Registration', width = 25, command = self.close_windows)
##        self.CaregiverButton.pack()
##        self.frame.pack()
##        self.CaregiverButton = tk.Button(self.frame, text = 'Caregiver Registration', width = 25, command = self.close_windows)
##        self.CaregiverButton.pack()
##        self.frame.pack()
        self.TagButton = ttk.Button(self.frame, text = 'Tag Registration', style="C.TButton" ,width = 25, command = self.RegTag)
        self.TagButton.pack()
        self.frame.pack()
        self.CamperButton = ttk.Button(self.frame, text = 'Camper Registration', style="C.TButton" ,width = 25, command = self.CamperTag)
        self.CamperButton.pack()
        self.frame.pack()
        self.AssignButton = ttk.Button(self.frame, text = 'Assign A Tag', style="C.TButton" ,width = 25, command = self.AssignTag)
        self.AssignButton.pack()
        self.frame.pack()
##        self.UserButton = tk.Button(self.frame, text = 'User Registration', width = 25, command = self.close_windows)
##        self.UserButton.pack()
##        self.frame.pack()
        self.ExitButton = ttk.Button(self.frame, text = 'Exit', style="C.TButton" ,width = 25, command = self.close_windows)
        self.ExitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
    def RegRoom(self):
        self.newWindow = tk.Toplevel(self.master)
        RoomObj = RoomReg(self.newWindow)
    def RegTag(self):
        self.newWindow = tk.Toplevel(self.master)
        TagObj = TagReg(self.newWindow)
    def CamperTag(self):
        self.newWindow = tk.Toplevel(self.master)
        TagObj = CamperReg(self.newWindow)
    def AssignTag(self):
        self.newWindow = tk.Toplevel(self.master)
        TagObj = AssignTag(self.newWindow)
