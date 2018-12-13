##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: Homework 03 Part 1 Euler Problem 25
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 9/11/18
# DESCRIPTION: Finds first fibonacci sequence number that has n digits
# GRADING NOTES: 
# OTHER NOTES: 

##############################################################################

##############################################################################


# Euler Problem 25: First Fibonacci number with n digits
# Use your own Fibonacci function, don't use a numpy function to get it
# Don't forget you can get bonus points for implementing this in a way
# that does not just check every Fibonacci number sequentially.

##############################################################################
# WRITE ALL CODE FOR PROBLEM 25 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def nth_digit_fibonacci(n): # TODO: needs to accept an argument
    # initialize variables 
    fibLen = 0
    f = []
    f.append(1)
    f.append(1)
    i = 2
    # calculates next fibonacci number until it has n digits.
    while fibLen < n:
        f.append(f[i-1] + f[i-2])
        fibLen = len(str(f[i]))
        i += 1
    return i

# going back to this indentation level stops defining the function.


##############################################################################
# WRITE ALL CODE FOR PROBLEM 25 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
