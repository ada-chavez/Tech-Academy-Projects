##  Python:         3.9.0
##
##  Author:         Ada Chavez
##
##  Description:    Checks for files that end with .txt and
##                  prints out the path of the txt files along
##                  with the time and date of last modification

import os
import time

fPath = 'C:\\A\\'

for fName in os.listdir(fPath):
    if fName.endswith('.txt'): # checks to see if file ends with .txt
        txtFiles = os.path.join(fPath, fName) #concatanates file path with file name
        modTime = ("Last modified: %s" % time.ctime(os.path.getmtime(txtFiles))) # gets last modified time of each file
        print(txtFiles,modTime)
    else:
        continue

