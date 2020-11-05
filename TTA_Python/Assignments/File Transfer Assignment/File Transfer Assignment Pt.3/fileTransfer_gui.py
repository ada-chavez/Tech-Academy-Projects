from tkinter import *
from tkinter import filedialog
import shutil
import os
import datetime

import fileTransfer_main
import fileTransfer_func

def load_gui(self):

    #label
    self.lblSource = Label(self.master, text="Please select a folder with files to be copied:")
    self.lblSource.grid(row=0,column=1,columnspan=2,padx=(20,0),pady=(20,0),sticky=W)
    self.lblDest = Label(self.master, text="Please select a folder to receive copied files:")
    self.lblDest.grid(row=2,column=1,columnspan=2,padx=(20,0),pady=(20,0),sticky=W)

    #result label
    
    self.result= StringVar()
    self.lblResult = Label(self.master, textvariable=self.result)
    self.lblResult.config(font=("Georgia",12))
    self.lblResult.grid(row=5, column=1,columnspan=2,pady=(20,0))

    #entry textbox
    self.sourceDir= StringVar()
    self.destDir = StringVar()
    
    self.entrySource = Entry(self.master,width=55,textvariable=self.sourceDir)
    self.entrySource.grid(row=1,column=1,columnspan=2, padx=(20,0))

    self.entryDest = Entry(self.master,width=55,textvariable=self.destDir)
    self.entryDest.grid(row=3,column=1,columnspan=2, padx=(20,0))


    #buttons
    self.btnSelect = Button(self.master, width=10,height=2,text="Browse...",command=lambda:fileTransfer_func.onSelect(self))
    self.btnSelect.grid(row=1,column=3,padx=(20,15),pady=(0,0),sticky=W)

    self.btnCopy = Button(self.master, width=10,height=2,text="Browse...",command=lambda:fileTransfer_func.onCopy(self))
    self.btnCopy.grid(row=3,column=3,padx=(20,15),pady=(0,0),sticky=W)

    self.btnFileCheck = Button(self.master, width=35,height=2,text="Process", command=lambda:fileTransfer_func.fileCheck(self))
    self.btnFileCheck.grid(row=4,column=1,columnspan=2,padx=(5,15),pady=(10,0,))






if __name__ == "__main__":
    pass
    
