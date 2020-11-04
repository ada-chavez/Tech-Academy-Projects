
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import gui_main
import gui_func

def load_gui(self):

    #buttons
    self.browseOneButton = Button(self.master,text="Browse...", width=15, height=1, command=lambda: gui_func.browseFiles(self))
    self.browseOneButton.grid(row=1,column=0,padx=(27,0),pady=(40,0),sticky=N+W)

    self.browseTwoButton = Button(self.master,text="Browse...", width=15, height=1)
    self.browseTwoButton.grid(row=2,column=0,padx=(27,0),pady=(20,0),sticky=N+W)

    self.checkFilesButton = Button(self.master,text="Check for files...", width=15, height=2)
    self.checkFilesButton.grid(row=3,column=0,padx=(27,0),pady=(10,2),sticky=N+W)

    self.closeButton = Button(self.master,text="Close Program", width=13, height=2)
    self.closeButton.grid(row=3,column=1,padx=(27,10),pady=(10,2),sticky=S+E)

    #entry boxes
    self.fileOne = Text(self.master, width=50, height=1)
    self.fileOne.grid(row=1,column=1, padx=(20,10),pady=(40,0))

    self.fileTwo = Text(self.master, width=50, height=1)
    self.fileTwo.grid(row=2,column=1, padx=(20,10),pady=(15,0))







if __name__ == "__main__":
    pass
    

