
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import gui_gui
import gui_func

# Frame is the Tkinter fram class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        
        # Define our master frame configuration
        self.master = master
        
        self.master.minsize(600,200) #(Height, Width)
        self.master.maxsize(600,200)

    
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")


        # Load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        gui_gui.load_gui(self)







if __name__ == "__main__":
    root = tk.Tk() # instatiated tkinter and named it root
    App = ParentWindow(root) # attached Tkinter to ParentWindow and attached to App
    root.mainloop() # this allows the window to stay open until the user closes it

