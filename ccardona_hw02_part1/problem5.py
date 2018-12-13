##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: HW02 Part 1 Euler problem 5
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/28/18
# DESCRIPTION: Finds largest number thats a multiple of all numbers up to N.
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

# Euler Problem 5: Smallest multiple
# grade = 5 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 5 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def smallest_multiple(N): # We want to find the least common multiple of all
    # numbers from 1 to N.
    # We can do this using the proof that lcm(a, b) = |a * b|/(gcd(a,b))
    # And that lcm(a, b, c) = lcm(a, lcm(b, c))
    # Using the Euclidean algorithm to find the gcd.
    
    # If N is 0 or 1 or 2 the LCM of it is just that.
    if(N <= 2):
        return N
    # create an array of the numbers we want to find the LCM of and
    # call the LCM function.
    arr = []
    while N > 1:
        arr.append(N)
        N-=1
    return lcm(arr)

#recursive lcm function that calls the gcd function.
def lcm(arr):
    if len(arr) == 2:
        return (abs(arr[0] * arr[1]) / gcd(arr[0],arr[1]))
    else:
        return lcm([arr[0], lcm(arr[1:])])




# Recursive implementation of Euclids algorithm that takes advantage
# of the fact that the gcd of a equals the gdc of a % b.
def gcd(a, b):
    # when a is divisible by b return a because we have found
    # the gcd. 
    if b == 0:
        return a
    else:
        return gcd(b, a % b)





    # Old code. Took too long.
    # num = N
    # while num <= math.factorial(N):
    #     multOf = True
    #     for i in range(2, N):
    #         if num % i != 0:
    #             multOf = False
    #             break
    #     if multOf:
    #         return num
    #     num += N
    # return -1
		


##############################################################################
# WRITE ALL CODE FOR PROBLEM 5 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
