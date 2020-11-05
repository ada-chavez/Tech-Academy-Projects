## Version:     Python 3.9.0
##
## Author:      Ada Chavez
##
## Purpose:     Copy files from one folder to another
##          


import shutil
import os

#set where the source of the files are
source = '/Users/Victoria/Desktop/File Transfer Assignment/folderA/'

#set the destination path to folderB
destination = '/Users/Victoria/Desktop/File Transfer Assignment/folderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
