from tkinter import *
import tkinter as tk

import webpage_generator_main
import webpage_generator_func

def load_gui(self):

    #button
    self.btn = Button(self.master, text="Generate Webpage", command=lambda: webpage_generator_func.userInput(self))
    self.btn.grid(row=4,column=2, pady=(10,0), sticky = E)

    #entry
    v = StringVar()
    v.set("Type here to change text body of a html file...")
    
    self.txtBody = Entry(self.master,textvariable = v , width=50)
    self.txtBody.grid(row=1,rowspan=3, column=1, columnspan =4, padx=(20,0), pady=(20,0))



if __name__ == "__main__":
    pass
    
