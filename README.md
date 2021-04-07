# pands-problem-sheet

## README.md 
### Notes
In the module of Programming And Scripting a weekly problem is provided to students. The students are to provide a solution that will be worked on throughout the semester. 


## Weekly Tasks 02
### [bmi.py](https://github.com/DPR-droid/pands-problem-sheet/blob/main/bmi.py) 
This script calculates the users BMI
The first iteration of the script the integer had been set to test the calculation for the BMI and its output.  After a few iterations I was satisfied with the output to 2 two decimal places. 

Description of the script
1.	The user is requested to input the required variables of **weight** in kilograms and **height** in centimetres.
2.	The calculation divides the **weight** by **height** squared.
3.	This is then divided by 10000.
4.	The **round()** function returns a floating point number that is a rounded version of the specified number, with the specified number 2 decimals.
5.	The output is a concatenated string  which includes the calculated BMI


### Citation/Reference
The following location had the calculation for the BMI

    https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
The round function

    https://www.w3schools.com/python/ref_func_round.asp


## Weekly Tasks 03
### [secondstring.py](https://github.com/DPR-droid/pands-problem-sheet/blob/main/secondstring.py)
The script asks a user to input a string and outputs in reverse order then selects every second character.

The first iteration of the script the input had been set to test output.  Using Python ability to slicing strings, the first iteration reversed the input string, the second iteration slicing was used again to select every second character from the reversed string. It was noted that the string could be slicied using one [] and after some research this was possible.

Description of the script
1.	The user is requested to input a **string**
2.	Python slice syntax is used to reverse order and select every second letter.
3.	The output is printed to the screen

### Citation/Reference
Slicing notation

    https://www.w3schools.com/python/python_strings_slicing.asp

    https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/#Slice_Notation


## Weekly Tasks 04
### [collatz.py](https://github.com/DPR-droid/pands-problem-sheet/blob/main/collatz.py)
The script is designed to request a positive integer and at each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. With the script ending if the current value is one. 

Description of the script

1.	The user is requested to input a **positive integer**.
2.	A lists is used to store multiple items in a single variable for output at the end of the script.
3.	The append() method appends an element the output to the end of the list.
4.	The script uses an if statement as a sanity check, if the number is zero or negative it outputs a message to the screen and finishes .
5.	The script then uses a while statement to check if the number is not 1.
6.	The if statement is used to verify if the number is odd or even and then carries out the required calculation.
7.	The output of the calculation in part 6 is added to the list using the append method as seen in part 2.
8.	This is repeated until the output is equal to 1 set in part 5 while statement.
9.	The final part prints out the list using the parameter **sep**.

### Citation/Reference Material
List

    https://www.w3schools.com/python/python_lists.asp

Append

    https://www.w3schools.com/python/ref_list_append.asp
    
Python Conditions and If statements

    https://www.w3schools.com/python/python_conditions.asp

While Loops

    https://www.w3schools.com/python/python_while_loops.asp

Prints numbers list with spaces separating

    https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/


## Weekly Tasks 05
### [weekday.py](https://github.com/DPR-droid/pands-problem-sheet/blob/main/weekday.py)
The program outputs whether or not today is a weekday
### Citation/Reference Material
The program that outputs whether or not today is a weekday

    https://www.w3schools.com/python/python_datetime.asp


## Weekly Tasks 06
### [squareroot.py](https://github.com/DPR-droid/pands-problem-sheet/blob/main/squareroot.py)
The program that takes a positive floating-point number as input and outputs an approximation of its square root
### Citation/Reference Material
Function for newtons-method from 

    https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
Function to test users input is a positive floating-point number from 
    
    https://pynative.com/python-check-user-input-is-number-or-string/


## Weekly Tasks 07
### [es.py](https://github.com/DPR-droid/pands-problem-sheet/blob/main/es.py)
This program that reads in a text file and outputs the number of e's it contains
The program takes the filename from an argument on the command line.
"python es.py moby-dick.txt"
The argument can also use path to the file.
"python es.py C:\Programming\programming2021\pands-problem-sheet\moby-dick.txt"

### Citation/Reference Material
A copy of the Moby Dick text can be found at the following link 

    https://www.gutenberg.org/files/2701/old/moby10b.txt
Command line arguement

    https://realpython.com/python-command-line-arguments/
Check if File exist 

    https://www.w3schools.com/python/python_file_remove.asp
Statement automatically takes care of closing the file after reading link

    https://realpython.com/read-write-files-python/
Regex findall link

    https://www.w3schools.com/python/python_regex.asp#findall


## Weekly Tasks 08
### [plottask.py](https://github.com/DPR-droid/pands-problem-sheet/blob/main/plottask.py)
This displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
in the range [0, 4] on the one set of axes.
### Citation/Reference Material

    https://numpy.org/doc/stable/reference/generated/numpy.power.html

    https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-5.php

