# ASSIGNMENT NAME: HW02 Part 2
# NAME: Chance Cardona
# EMAIL: ccardona@mines.edu
# DATE: 9/3/2018
# DESCRIPTION: Euler Problem 9. Finds the product of the pyythagorean triplet
#   for a given input number.
# GRADING NOTES:
# OTHER NOTES: 

def triplet(N):
    # a < b < c
    # important to start from 1, not 0 as a pythag triplet is a set of 3
    #  natural nums.
    for i in range(1, N):
        a = i
        for k in range(a, N):
            b = k
            # definition of c is based on pythagorean theorem.
            c = (a**2 + b**2)**0.5
            # returns only if correct pythagorean triplet
            # also made sure the c was an int, since we're evaluating 
            # natural numbers.
            if a + b + c == N and c % 1 == 0: 
                return a*b*c
    #returns none if no pythagorean triplet exists for the number.
    return None

# while True:
#     n1 = int(input("Enter number now: "))
#     print("Answer: ",triplet(n1))