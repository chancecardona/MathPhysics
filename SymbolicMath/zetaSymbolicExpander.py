# ASSIGNMENT NAME: HW 8
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/2/18
# DESCRIPTION: Sympy proof from Problem 3 of HW 8.
# OTHER NOTES:

from sympy import Symbol, cos, series, exp, diff

x = Symbol('x')

def func(x):
    return -1/(1 - exp(-x))

def main(k, terms):
    d = diff(func(x), x, k)
    print(d)
    a = series(d, x, n=terms)
    print("The derivative of the order {} with first  {} terms in the Taylor series is \n{}".format(k, terms, a))

    return a

num = 3
order = 3
main(order, num)
