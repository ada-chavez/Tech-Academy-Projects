##Python Version:     3.9.0
##
##Author:             Ada Chavez
##
##Description:        Student Tracking System demonstrating Tkinter, SQLite3,
##                    and OOP


from tkinter import *
import tkinter as tk
from tkinter import messagebox

import student_tracking_gui
import student_tracking_func

# Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        
        # Define our master frame configuration
        self.master = master
        
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)

        
        # This CenterWindow method will center the app on the user's screen
        student_tracking_func.center_window(self,500,300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        student_tracking_gui.load_gui(self)

        

if __name__ == "__main__":
    root = tk.Tk() # instatiated tkinter and named it root
    App = ParentWindow() # attached Tkinter to ParentWindow and attached to App
    root.mainloop() # this allows the window to stay open until the user closes it
