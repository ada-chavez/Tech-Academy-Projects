## Version:     Python 3.9.0
##
## Author:      Ada Chavez
##
## Purpose:     Automates copying text files that have been modified/created
##              in the last 24 hours to another folder.


import shutil
import os
import datetime

#set where the source of the files are
source = '/Users/Victoria/Desktop/File Transfer Assignment/folderA/'

#set the destination path to folderB
destination = '/Users/Victoria/Desktop/File Transfer Assignment/folderB/'

# list of the file names in folderA
files = os.listdir(source)

for i in files:

    # create absolute path for each file in folder
    abPath = source+i

    # get last modified date/time and current date/time
    modDate = datetime.datetime.fromtimestamp(os.path.getmtime(abPath))
    currentDate = datetime.datetime.today()

    # date/time 24 hours ago from currentDate
    modDateLimit = modDate + datetime.timedelta(days=1)

    # if file was edited less than 24 hours ago then copy it
    if modDateLimit > currentDate:
        shutil.copy(abPath, destination)
