# ASSIGNMENT NAME: HW 5
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 10/18/18
# DESCRIPTION: Simpsons Rule integral approximation.
# OTHER NOTES: (if applicable)

import numpy as np
from functions import *

# Steps must be an EVEN number due to nature of this algorithm
def simpsons(a, b, steps, fn):
    # Define step. Same as for trap.
    dx = (b - a) / steps
    sum = 0

    # Sum area under all parabolas created
    for i in range(1, steps, 2):
        sum += dx/3 * ( fn(a + (i-1)*dx) + 4*fn(a + i*dx) + fn(a + (i+1)*dx) )

    if sum > 10**9:
        sum = np.inf
    return np.around(sum, 3)


if __name__ == "__main__":
    print(simpsons(0, np.pi, 100, np.sin))
    print(simpsons(0, 2*np.pi, 100, np.sin))
    print(simpsons(1, 10, 100, inverse))
    print(simpsons(1, 10, 100, inverse2))
    print(simpsons(0 + 1/10000, 10, 100, inverse0_5))
    print( np.around(abs( np.pi - simpsons(-10**3, 10**3, 102, sinOverx) ), 3))
    print(simpsons(-10**3, 10**3, 102, cosOverx))
    print(simpsons(0, np.pi, 100, cosSquared))