# ASSIGNMENT NAME: HW02 Part 1 Euler problem 5
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/28/18
# DESCRIPTION: Finds largest number thats a multiple of all numbers up to N.
# GRADING NOTES: 
# OTHER NOTES: (if applicable)


# Euler Problem 5: Smallest multiple

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
