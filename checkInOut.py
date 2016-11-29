import tkinter as tk
from tkinter import ttk
from DBNode import DBNode

class checkInOut:
   def __init__(self, master):
      self.master = master
      self.frame = tk.Frame(self.master)
      self.frame.pack() 
      style = ttk.Style()
      style.map("C.TButton",
          foreground=[('pressed', 'red'), ('active', 'blue')],
          background=[('pressed', '!disabled', 'black'), ('active', 'red')]
          )

      #Menu features
      CheckInButton = ttk.Button(self.frame, text='Camper Check In', style="C.TButton", width = 25, command=self.CheckIn)
      CheckInButton.pack()
      CheckOutButton = ttk.Button(self.frame, text='Camper Check Out', style="C.TButton", width = 25, command=self.CheckOut)
      CheckOutButton.pack()
      self.DBObj = DBNode("402DB", "123456", "Test")

 
   def CheckIn(self):
      def performSearch():
         name = searchBox.get()
         self.DBObj.CheckIn(name)
      self.newWindow = tk.Toplevel(self.master)

      #Menu features
      CamperName = tk.Label(self.newWindow, text="Camper Name", width=25)
      CamperName.pack()
      searchBox = tk.Entry(self.newWindow)
      searchBox.pack()
      searchBox.focus_set()
      eb = ttk.Button(self.newWindow, text='Check In', style="C.TButton", width=25, command=performSearch)
      eb.pack()

   def CheckOut(self):
      def performSearch():
         name = searchBox.get()
         self.DBObj.CheckOut(name)
      self.newWindow = tk.Toplevel(self.master)

      #Menu features
      CamperName = tk.Label(self.newWindow, text="Camper Name", width=25)
      CamperName.pack()
      searchBox = tk.Entry(self.newWindow)
      searchBox.pack()
      searchBox.focus_set()
      eb = ttk.Button(self.newWindow, text='Check Out', style="C.TButton", width=25, command=performSearch)
      eb.pack()
