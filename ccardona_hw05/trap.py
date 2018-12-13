# ASSIGNMENT NAME: HW 5
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 10/18/18
# DESCRIPTION: Trapezoidal Rule integral approximation.
# OTHER NOTES: (if applicable)

import numpy as np
from functions import *

# a and b are your range. steps for accurancy, fn is function 
# you want to integrate.
def trapezoidal(a, b, steps, fn):
    # Defines our step
    dx = (b - a) / steps
    sum = 0

    # Sums all the trapezoids areas from a to b
    for i in range(1, steps):
        sum += dx * ( fn(a + (i-1)*dx) + fn(a + i*dx) ) / 2
    
    # Hardcoded limit we're calling "infinity". Not sure
    # if there's a better way to do this.
    if sum > 10**9:
        sum = np.inf
    # Rounding.
    return np.around(sum, 3)


if __name__ == "__main__":
    print(trapezoidal(0, np.pi, 100, np.sin))
    print(trapezoidal(0, 2*np.pi, 100, np.sin))
    print(trapezoidal(1, 10, 100, inverse))
    print(trapezoidal(1, 10, 100, inverse2))
    print(trapezoidal(0 + 1/10000, 10, 100, inverse0_5))
    # Sorry if this one seems a bit hardcoded... it's kind of an oddball.
    print(np.around(abs( np.pi - trapezoidal(-10**3, 10**3, 102, sinOverx) ), 3) )
    print(trapezoidal(-10**3, 10**3, 102, cosOverx))
    print(trapezoidal(0, np.pi, 100, cosSquared))
