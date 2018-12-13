##############################################################################
# !!! USE THIS HEADER FOR ALL SUBMISSIONS !!!
##############################################################################
# ASSIGNMENT NAME: HW02 Part 1 Euler problem 3
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/28/18
# DESCRIPTION: Finds largest prime factor of number N.
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

# Euler Problem 3: Largest prime factor of a number
# From 1 to input n
# grade = 5 pts for all test cases

##############################################################################
# WRITE ALL CODE FOR PROBLEM 3 BELOW THIS BLOCK.
# USE THE FUNCTION NAME AS WRITTEN
##############################################################################

def largest_prime_factor(N): #Number to find prime factor of
    # We will now treat N as our trial prime factor.
    # i will be the possible factor.
    # Begin at i=2 and go until sqrt(N) because if N were divisible
    # by p, n = p x q. p or q will be <= i^2, and all we need to check
    # is the smaller factor to see that it's not prime. With no smaller
    # number, there can be no larger, unless they are ==, which this checks.
    # Heavily helped and inspired by
    # http://thetaoishere.blogspot.com/2008/05/largest-prime-factor-of-number.html
    # and https://en.wikipedia.org/wiki/Trial_division
    i = 2
    while i <= int(N**0.5):
        # Smallest factor i that N is divisible by is prime, because if it
        # wasn't there would be still a smaller number to divide it by.
        # We divide N by this smallest prime factor until that factor is
        # fully gone from it or i^2 > N (we're taking advantage of the 
        # sqrt(N) trick for each trial prime factor). Rinse and repeat until
        # i is equal to sqrt(N) so you know there is no factors larger.
        if N % i == 0:
            N = N // i
        # If that didn't find anything, move onto the next factor.
        else:
            i += 1
    return N


    #Below this is past code that did not work for the assignment.
    # TRIAL 1: FAIL. Algorithm was too inneficient

# First find prime numbers in a number
# Next find largest that the number is divisble by
# def maxPrime(N):
#     max = 2
#     for i in range(3, int(N**.5)):
#         isPrime = True
#         for number in range(2,i):
#             if i % number == 0:
#                 isPrime = False
#         if isPrime:
#             if N % i == 0:
#                 max = i
#     return max
#



# TRIAL 2: FAIL. Number was too large for numpy

# Tries to find all primes up to a number. Looks for if they're divisible
# by it and selects the max divisible one
# import numpy as np
#
# def maxPrime(N):
#     N = np.int64(N)
#     # allNums = np.linspace(2, N//2, N//2 - 2, dtype=np.int64)
#     # for i in range(3, int(N**0.5)+1, 2):
#     #     if allNums[i//2] != 0:
#     #         allNums[(i*i)//2::i] = 0
#     #
#     # primes = 2*np.nonzero(allNums)[0][1::]+1
#     # max = primes[0]
#     # for x in np.nditer(primes):
#     #     if N % x == 0:
#     #         print(x)
#     #         max = x
#     #
#     # return max
#     # return primes


##############################################################################
# WRITE ALL CODE FOR PROBLEM 3 ABOVE THIS BLOCK
##############################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
