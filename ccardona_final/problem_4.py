# ASSIGNMENT NAME: FINAL
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/9/18
# DESCRIPTION: Finds number of lychrel numbers below a number r.
# OTHER NOTES: (if applicable)

import numpy as np


def palindrome(n):
    strIn = str(n)
    strRev = strIn[::-1]
    if strIn == strRev:
        return True
    return False

def rev(n):
    strIn = str(n)
    return int(strIn[::-1])

# checks if number is lychrel.
def lychrel(n):
    for i in range(50):
        n += rev(n)
        if palindrome(n):
            return False
    return True

# r is the number we want to go to.
def numLychrel(r):
    num = 0
    for i in range(r):
        if lychrel(i):
            num+=1
    return num


if __name__ == "__main__":
    print(numLychrel(10000))
