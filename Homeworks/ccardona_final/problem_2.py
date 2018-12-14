# ASSIGNMENT NAME: FINAL
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/9/18
# DESCRIPTION: Returns a*b where n^2 + an + b is prime for n = 0 to n-2
# OTHER NOTES: (if applicable)

import numpy as np
from problem_1 import primes

def is_prime(n):
    # negative numbers not included in this.
    if n < 0:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


def quad_primes(L):
# b is always prime. a is odd.
    primeList = primes(L+1)
    consMax = 0 # Highest consecutive primes found
    consProd = 0 
    for b in primeList:
        for a in range(-b + 2, 0, 2):
            n = 1
            while is_prime(n*n + a*n + b):
                n+=1
            if n > consMax:
                consMax = n
                consProd = a * b
    
    return consProd


if __name__ == "__main__":
    print(quad_primes(1000))
