##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: HW01 Part 3 of 3
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/22/2018
# DESCRIPTION: Problems 5 and 6
#              (write about included functions, methods, how to use, etc.)
# GRADING NOTES: (if applicable - I.E. "Couldn't get problem 3 to work,
#                 commented out so program runs")
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



# Problem 5: check if the word or sentence is a palindrome
# (same spelling forwards and backwards e.g. "racecar")
# NOTE: Ignore spaces in multi-word inputs. Assume no punctuation
# grade = 14 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 5 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def palindrome(strIn):
    # Removes all spaces from string
    strIn = strIn.replace(" ","")
    # reverses string using slice notation. [::-1] means start at end :
    # go until the beginning : and count backwards.
    # You start at end since step is -1, otherwise you'd start at beginning
    # and go to the end. (since you didnt specify start or stop)
    strRev = strIn[::-1]
    if strIn == strRev:
        return True
    return False


##############################################################################
# WRITE ALL CODE FOR PROBLEM 5 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# Problem 6: check if a given number is a power of 2
# grade = 6 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 6 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def is_power_of_two(n):
    num = n
    # Takes a number, divides it by 2 until it's not divisible by 2 anymore.
    # If it equals 1, then it can be formed wholely of 2's and is a power of 2.
    # else it is an odd number, and thus not divisible by 2.
    # assuming all numbers are ints. If it's fractions we would do the same
    # but multiply by 2 instead of divide and go up till it was >=1.
    while num % 2 == 0 and num >= 1:
        num /= 2
    if num == 1:
        return True

    return False


##############################################################################
# WRITE ALL CODE FOR PROBLEM 6 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
