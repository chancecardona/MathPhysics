##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: HW01 Part 1 of 3
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/20/2018
# DESCRIPTION: Problems 1 and 2
#              (write about included functions, methods, how to use, etc.)
# GRADING NOTES:
# OTHER NOTES: (if applicable)

##############################################################################

##############################################################################
# General notes/requirements:

# Don't forget to follow style guidelines - including writing comments
#    24 pts (about 33%) on this assignment as a whole! (8 points per part)

# Partial credit is possible provided the issues are written in the grading
# notes and any code that causes a crash is commented (failed test cases need
# not be commented). Include comments around code discussing the issue and
# possible causes/solutions for max partial credit

# Write your code between the designated sections. Do NOT change function names
# or test cases. Writing your own additonal functions and using them is ok.

# No outside libraries for this assignment
##############################################################################

from time import sleep

# Problem 1: find factorial of a number
# grade = 5 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 1 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def factorial(n):
    # initalize our answer to 1
    fact = 1
    # calculates the factorial of the input argument
    for i in range(n):
        fact = fact*(n-i)
    return fact

# going back to this indentation level stops defining the function.


##############################################################################
# WRITE ALL CODE FOR PROBLEM 1 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Problem 2: find sum of positive integers up to specified number (inclusive)
# grade = 5 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 2 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def sum_nums(n):
    # Using Gauss's famed formula to simply sum the n positive integers.
    sumNum = n*(n+1)//2
    # This is to demonstrate what happens when code takes too long
    # the test cases will hang, then fail after the specified time
    # once you've seen it happen, comment out this sleep call
    # sleep(30)

    # Returns sum calculated above
    return sumNum


##############################################################################
# WRITE ALL CODE FOR PROBLEM 2 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
