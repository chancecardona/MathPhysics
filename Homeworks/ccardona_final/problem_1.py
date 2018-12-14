# ASSIGNMENT NAME: FINAL
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/9/18
# DESCRIPTION: Finds the number under d w/ the longest reciprocal cycle (of 1/number)
# OTHER NOTES: (if applicable)

import numpy as np

# Sieve or Erastosthenes for efficient Prime generation
def primes(N):
    size = N
    arr = [True] * (size)
    arr[0] = arr[1] = False

    for i in range(2, int(size**0.5 + 1)):
        if arr[i]:
            for z in range(i*i, size, i):
                arr[z] = False

    primeList = []
    for i in range(N):
        if arr[i]:
            primeList.append(i)

    return primeList




# Finds the d with the longest recurring cycle for the 
# decimal fraction of 1/d.
#d is the max number youd like to find 1/d for.
def Reciprocal_cycle(d):
    #Fermats little theorem: Find highest full Retend Prime below d.
    if d < 7:
        return 3
    #All retend primes are primes. search only primes.
    primeList = primes(d)
    #Checks if retend
    for p in primeList[::-1]:
        j = 1
        while( 10**j % p != 1 ):
            j+=1
        if (p-1 == j):
            return p

if __name__ == "__main__":
    print(Reciprocal_cycle(1000))