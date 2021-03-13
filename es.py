########################################################################
### es.py
### This program that reads in a text file and outputs the number of e's it contains
### The program take the filename from an argument on the command line.
### "python es.py moby-dick.txt"
### The arguemnet can also in the path to the file.
### "python es.py C:\Programming\programming2021\pands-problem-sheet\moby-dick.txt"
### Author David
########################################################################
### A copy of the Moby Dick text can be found at the following link
### https://www.gutenberg.org/files/2701/old/moby10b.txt
########################################################################

########################################################################
### import modules
########################################################################
import os
import sys
import re

########################################################################
### https://realpython.com/python-command-line-arguments/
### Command line arguement 
########################################################################
filename = sys.argv[1]

########################################################################
### Set variables to zero
########################################################################
count = 0
totalCount = 0

########################################################################
# https://www.w3schools.com/python/python_file_remove.asp
# Check if File exist:
# To avoid getting an error, you might want to check if the file exists
########################################################################
if os.path.exists(filename):

########################################################################
### https://realpython.com/read-write-files-python/
### The with statement automatically takes care of closing the file 
### once it leaves the with block, even in cases of error. I highly 
### recommend that you use the with statement as much as possible, 
### as it allows for cleaner code and makes handling any unexpected 
### errors easier for you.
########################################################################
  with open(filename, "r") as f:
    for line in f:
        #########################################################
        ### https://www.w3schools.com/python/python_regex.asp#findall
        ### If you wish to count uppercase and lowercase the following 
        ### line can be used
        ### count = len(re.findall("e", line, re.IGNORECASE))
        #########################################################
        count = len(re.findall("e", line)) 
        ### Adding all lowercase e's in string to totalCount
        totalCount = totalCount + count
        ### Test to see totalcount 
        # print("in loop" + str(totalCount))
else:
  print("The file does not exist") 

# Output 
print(totalCount)