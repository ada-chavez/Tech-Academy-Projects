from tkinter import *
from tkinter import filedialog
import shutil
import os
import datetime

import fileTransfer_main
import fileTransfer_func

def onSelect(self):
    #global variable so that fileCheck can use it
    global folder_path_source

    # askdirectory method opens the system directory
    folder_path_source = filedialog.askdirectory()

    # update sourceDir variable with file1 to show up in entry textbox
    self.sourceDir.set(folder_path_source)

def onCopy(self):
    global folder_path_dest
    # askdirectory method opens the system directory
    folder_path_dest = filedialog.askdirectory()

    # update sourceDir variable with file1 to show up in entry textbox
    self.destDir.set(folder_path_dest)

def fileCheck(self):
    # list of the file names in source folder
    files = os.listdir(folder_path_source)

    for i in files:
        # checks for txt files
        if i.endswith('.txt'):
            
            # create absolute path for each file in folder
            abPath = folder_path_source+"/"+i

            # get last modified date/time and current date/time
            modDate = datetime.datetime.fromtimestamp(os.path.getmtime(abPath))
            currentDate = datetime.datetime.today()

            # date/time 24 hours ago from currentDate
            modDateLimit = modDate + datetime.timedelta(days=1)

            # if file was edited less than 24 hours ago then copy it
            if modDateLimit > currentDate:
                shutil.copy(abPath, folder_path_dest)

            self.result.set("Success! \nFiles have been copied over to destination folder!")

            




if __name__ == "__main__":
    pass
    
