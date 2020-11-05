## Version:     Python 3.9.0
##
## Author:      Ada Chavez
##
## Purpose:     A GUI to allow user to browse and choose a specific folder that will contain
##              the files to be checked daily, be able to choose folder that will reeive the copied files,
##              and allow user to manually initiate the 'file check' process

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import datetime

import fileTransfer_gui
import fileTransfer_func

# Frame is the Tkinter frem class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define the master frame configuaration
        self.master = master

        # height and width of frame
        self.master.minsize(500, 300)
        self.master.maxsize(500,300)

        # title of frame
        self.master.title("File Transfer System")

        # background color of frame
        self.master.configure(bg="#F0F0F0")

        # Load in the GUI widgets from a separate module
        fileTransfer_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk() # instatiated tkinter and named it root
    App = ParentWindow(root) # attached Tkinter to ParentWindow and attached to App
    root.mainloop() # this allows the window to stay open until the user closes
