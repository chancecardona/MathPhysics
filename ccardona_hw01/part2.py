##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: HW01 Part 2 of 3
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/20/2018
# DESCRIPTION: Problems 3 and 4
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



# Problem 3: convert time from seconds into a format
# hours:minutes:seconds
# grade = 12 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 3 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

# !! fewer hints for this one, but use the same process
def time_conversion(sec):
    # Converts time in seconds to the format hours:minutes:seconds
    # the '{:02}'.format essentially says that we want 2 digits (so like 00 rather than 0)
    # while the // is doing integer division.
    hours = '{:02}'.format(sec // 3600)
    # the seconds is first mod 3600'd such that minutes can never be > 60
    minutes = '{:02}'.format((sec % 3600) // 60)
    seconds = '{:02}'.format(sec % 60)
    # here we concantenate the string and output it.
    return hours + ":" + minutes + ":" + seconds


##############################################################################
# WRITE ALL CODE FOR PROBLEM 3 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# Problem 4: count number of vowels in a word or words
# don't worry about the letter y
# grade = 6 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 4 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

# !! use the same process
def count_vowels(strInput):
    # Counts the vowels in a string arguement
    count = 0
    for c in strInput:
        # Checks each character in the str to see if it is also found in a test string
        # (the test string being a list of vowels)
        if c in "aeiou":
            count += 1
    return count

##############################################################################
# WRITE ALL CODE FOR PROBLEM 4 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
