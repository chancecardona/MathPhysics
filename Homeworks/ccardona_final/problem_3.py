# ASSIGNMENT NAME: FINAL
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/9/18
# DESCRIPTION: Finds the sum of the diagonals for a number spiral
# OTHER NOTES: (if applicable)

import numpy as np

def spiralDSum(s):
    n = (s+1)/2 -1
    return ring(n)

def ring(n):
    if n == 0:
        return 1
    # formula for each sum of corners in each ring in the spiral
    return int(ring(n-1) + 4*(2*n+1)**2 - 12*n )


if __name__ == "__main__":
    # print(spiralDSum(3))
    # print(spiralDSum(5))
    # print(spiralDSum(7))
    print(spiralDSum(1001))
