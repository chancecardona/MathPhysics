# ASSIGNMENT NAME: HW02 Part 2
# NAME: Chance Cardona
# EMAIL: ccardona@mines.edu
# DATE: 9/3/2018
# DESCRIPTION: Euler Problem 7. Finds the nth prime number.
#   uses the sieve of erastosthenes generated to 
#   2n*log(n) (see prime number theorem on wikipedia) and returns the nth
#   index of this sieve of erastosthenes array.
# GRADING NOTES:
# OTHER NOTES: 

##############################################################################

##############################################################################

import math

def primes(N):
    # Sieve of Erastosthenes algorithm.
    # Heavily helped by the algorithm on wikipedia  at
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    arr = [True] * (N)
    arr[0] = arr[1] = False
    sqrtN = int(N**0.5)+1

    for i in range(2, sqrtN):
        if arr[i]:
            for j in range(i*i, N, i):
                arr[j] = False

    # Takes all true values in the bool array from the sieve and turns them
    # into an array of actual numbers
    primeList = []
    for k in range(N):
        if arr[k]:
            primeList.append(k)
    return primeList

# Finds the N'th prime from the primeList array. Can be tricky seeing how many
# Numbers we must find the sieve to, to find the Nth prime. Used the simple
# approximation for the nth prime number from the prime number theorem
# as seen at https://en.wikipedia.org/wiki/Prime_number_theorem
def nth_prime(N):
    return (primes(int(2*N*math.log(N)))[N-1])
