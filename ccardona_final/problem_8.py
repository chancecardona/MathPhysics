# ASSIGNMENT NAME: FINAL
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/0/18
# DESCRIPTION: Sympy for Summation of Divergent Series
# OTHER NOTES: (if applicable)

from sympy import Symbol, cos, series, exp, diff

x = Symbol('x')

def func(x):
    return -1/(1 - exp(-x))

def main(k, terms):
    d = diff(func(x), x, k)
    # print(d)
    a = series(d, x, n=terms)
    print("The derivative of order {} with the first {} terms in the Taylor series is \n{}\n".format(k, terms, a))

    return a


#Enter in form of main(derivative order, number of terms)
main(2, 2)
main(4, 2)
main(5, 3)
