##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: HW02 Part 1 Euler problem 1
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/28/18
# DESCRIPTION: Finds multiples of either 3 or 5 up to number N
# GRADING NOTES: 
# OTHER NOTES: (if applicable)

##############################################################################

##############################################################################
# General notes/requirements:

# Don't forget to follow style guidelines - including writing comments
# For comments: Explain your process! Why does a loop stop where it does,
# what are you tracking, why do you set if statements as they are?

# Lines should not exceed 79 characters (the length of the ####### lines).
# continue code onto the next line when necessary, with spacing to keep
# readable

# Partial credit is possible provided the issues are written in the grading
# notes and any code that causes a crash is commented (failed test cases need
# not be commented). Include comments around code discussing the issue and
# possible causes/solutions for max partial credit

# Write your code between the designated sections. Do NOT change function names
# or test cases. Writing your own additonal functions and using them is ok.

# You may use basic functions of numpy, but you should not use anything that
# clearly does the work for you, i.e. using numpy's prime numbers etc..
##############################################################################

# Euler Problem 1: Multiples of 3 and 5
# grade = 5 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 1 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def multiples_3_5(N): # Number to go up to.
    # Create an empty list of numbers
    numList = []
    # Go through all numbers up to N
    for i in range(N):
        # If the number is a multiple of 3 or 5 add to the list.
        if i % 3 == 0 or i % 5 == 0:
            numList.append(i)
    return sum(numList)

##############################################################################
# WRITE ALL CODE FOR PROBLEM 1 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
