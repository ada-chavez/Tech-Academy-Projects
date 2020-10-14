##  Python:         3.9.0
##
##  Author:         Ada Chavez
##
##  Description:    A script that creates a db and adds new data into
##                  that db. This script reads from a file list and looks
##                  up files that end with '.txt' and prints the text files
##                  to the console.


# Be able to use the functions available in the sqlite3 module
import sqlite3

# Variable to store query to create a table
create_table = "CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT \
                )"

# Supplied list of file names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Checks fileList for files ending with .txt
# and adds it to txt_files list
txt_files = []
for fName in fileList:
    if fName.endswith('.txt'):
        txt_files.append(fName)
    else:
        continue

"""
Function that connects to the db,
takes each item in the fileList, and adds the data
into the col_fname.
"""

def conn_query():
    conn = sqlite3.connect('test2.db')
    with conn:
        cur = conn.cursor()
        cur.execute(create_table)
        for i in txt_files:
            cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)", \
                        (i,))
        conn.commit()
    conn.close()


# start function
if __name__ == "__main__":
    conn_query()
    



        
        
