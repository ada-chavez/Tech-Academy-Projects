from tkinter import *
import tkinter as tk
import webbrowser
import os

import webpage_generator_main
import webpage_generator_func

def userInput(self):
    userInput = self.txtBody.get()

    # open html file and write over the current content
    # will create a file if the specified file does not exist and write html to file
    
    f = open('webpage_generator.html', 'w')
    message = """<html><body> <h1>""" + userInput + """</h1></body></html>""" # concatenates user's input within body of html

    # writes the html into file
    f.write(message)

    #closes the file
    f.close()

    # open html file in a newtab in a webbrowser
    filename = 'file:///' +os.getcwd() + '/' + 'webpage_generator.html'
    webbrowser.open_new_tab(filename)
