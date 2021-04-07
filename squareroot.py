########################################################################
# squareroot.py
# Author David
# Positive floating-point number as input and 
# outputs an approximation of its square root
# This script requires mymodules.py to function
########################################################################

########################################################################
# The script has been redesgined creating a module called mymodules.py
# This module has two function 
# check_user_input - only a positive floating-point number as input.
# sqrt - calculation of the Newtons Method Function
# https://www.w3schools.com/python/python_modules.asp
########################################################################
from mymodules import check_user_input

########################################################################
# Test float number
# number = 14.5
########################################################################
# Request user input
pfpnumber = input("Please enter a positive floating-point number: ")

########################################################################
# Error detection function for a positive float in mymodule 
########################################################################
check_user_input(pfpnumber)
