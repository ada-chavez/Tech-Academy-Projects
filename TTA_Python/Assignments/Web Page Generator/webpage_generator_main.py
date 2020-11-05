##        Python:     3.9.0
##
##        Author:     Ada Chavez
##
##        Description: GUI that allows user to input text to a body of a web page
##                     and opens the html file in a webbrowser.

from tkinter import *
import tkinter as tk

import webpage_generator_gui
import webpage_generator_func


# Frame is the Tkinter frem class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define the master frame configuaration
        self.master = master

        # height and width of frame
        self.master.minsize(350, 100)
        self.master.maxsize(350,100)

        # title of frame
        self.master.title("Webpage Generator")

        # background color of frame
        self.master.configure(bg="#F0F0F0")

        # Load in the GUI widgets from a separate module
        webpage_generator_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk() # instatiated tkinter and named it root
    App = ParentWindow(root) # attached Tkinter to ParentWindow and attached to App
    root.mainloop() # this allows the window to stay open until the user closes it
