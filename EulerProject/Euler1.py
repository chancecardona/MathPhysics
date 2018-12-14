# ASSIGNMENT NAME: HW02 Part 1 Euler problem 1
# NAME: Chance Cardona
# EMAIL: ccardona@mymail.mines.edu
# DATE: 8/28/18
# DESCRIPTION: Finds multiples of either 3 or 5 up to number N
# GRADING NOTES: 
# OTHER NOTES: (if applicable)


# Euler Problem 1: Multiples of 3 and 5

def multiples_3_5(N): # Number to go up to.
    # Create an empty list of numbers
    numList = []
    # Go through all numbers up to N
    for i in range(N):
        # If the number is a multiple of 3 or 5 add to the list.
        if i % 3 == 0 or i % 5 == 0:
            numList.append(i)
    return sum(numList)
