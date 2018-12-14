# ASSIGNMENT NAME: HW01 Part 1 of 3
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/20/2018
# DESCRIPTION: Problems 1 and 2
#              (write about included functions, methods, how to use, etc.)
# GRADING NOTES:
# OTHER NOTES: (if applicable)

from time import sleep

# Problem 1: find factorial of a number

def factorial(n):
    # initalize our answer to 1
    fact = 1
    # calculates the factorial of the input argument
    for i in range(n):
        fact = fact*(n-i)
    return fact


##############################################################################

# Problem 2: find sum of positive integers up to specified number (inclusive)

def sum_nums(n):
    # Using Gauss's famed formula to simply sum the n positive integers.
    sumNum = n*(n+1)//2
    # This is to demonstrate what happens when code takes too long
    # the test cases will hang, then fail after the specified time
    # once you've seen it happen, comment out this sleep call
    # sleep(30)

    # Returns sum calculated above
    return sumNum
