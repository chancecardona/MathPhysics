##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: Homework 03 Part 1 Euler Problem 20
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 9/11/18
# DESCRIPTION: Finds sum of digits of n!
# GRADING NOTES: (if applicable - I.E. "Couldn't get problem 3 to work,
#                 commented out so program runs")
# OTHER NOTES: (if applicable)

##############################################################################

##############################################################################


# Euler Problem 20: Sum the digits of n! (factorial)
# Check the hint in the instructions. Casting to a string would let you
# access each digit, then you could cast back to an int..

##############################################################################
# WRITE ALL CODE FOR PROBLEM 20 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def factorial_digit_sum(n): 
    # Finds factorial of n
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    # counts digits of factorial by casting to a string
    strFact = str(fact)
    sum = 0
    for c in strFact:
        sum += int(c)
    return sum

# going back to this indentation level stops defining the function.


##############################################################################
# WRITE ALL CODE FOR PROBLEM 20 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
