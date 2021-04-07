########################################################################
# mymodules.py
# Author David
# This module is required for squareroot.py script
########################################################################

########################################################################
# Newtons Method Function
########################################################################

def sqrt(val):
    l = 0.00001
    # Assuming the sqrt of n as n only  
    x = val    
    # To count the number of iterations  
    count = 0   
    while (1) : 
        count += 1 
        # Calculate more closed x  
        root = 0.5 * (x + (val / x))  
        # Check for closeness  
        if (abs(root - x) < l) : 
            break 
        # Update root  
        x = root 
    # Test output
    # print(root)
    # Round to the nearest 2 decimal point.
    ans = round(root,1)
    print("The square root of {} is approx. {}. ".format(val, ans))
    return


########################################################################
# Error detection function for a positive floating-point number
########################################################################
def check_user_input(input):
    try:
        # Convert it into integer 
        val = int(input)
        print("Input is an integer. Number = " + str(val))
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print(val)
            ########################################################################
            # Check that the float is positive
            ########################################################################
            if val <= 0:
                print("No negative floats allowed")
            else:
                ########################################################################
                # Go to newtons method function squareRoot()   
                ########################################################################
                sqrt(val)
            # Test output            
            # print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a float. It's a string")
            