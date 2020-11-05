
from tkinter import *
from tkinter import filedialog



import gui_main
import gui_gui


def browseFiles(self):
    folder_path = filedialog.askdirectory() #gets the path to chosen directory
    self.path_var.set(folder_path) #sets path to variable in gui back end
    print(folder_path)


    


    



if __name__ == "__main__":
    pass
    
