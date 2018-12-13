##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: Homework 03 Part 1 Euler Problem 16
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 9/11/18
# DESCRIPTION: Sums the digits of some power. eg 2^4 = 1 + 6 = 7
# GRADING NOTES: 
# OTHER NOTES: (if applicable)

##############################################################################

##############################################################################


# Euler Problem 16: Sum the digits of 2**n
# Check the hint in the instructions. Casting to a string would let you
# access each digit, then you could cast back to an int..

##############################################################################
# WRITE ALL CODE FOR PROBLEM 16 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def power_digit_sum(n): 
    # finds 2^n power.
    pow = 2**n
    # counts digits by casting to a string.
    strPow = str(pow)
    sum = 0
    for c in strPow:
        sum += int(c)
    return sum

# going back to this indentation level stops defining the function.


##############################################################################
# WRITE ALL CODE FOR PROBLEM 16 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
