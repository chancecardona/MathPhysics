import numpy as np

def mult35(N):
    sum = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

def lpf(N):
    i = 2
    while i <= N**0.5:
        if N % i == 0:
            N = N / i
        else:
            i += 1
    return N

def smallestmult(N):
    i = N
    n = 1
    while n < N:
        if i % n != 0:
            i += N
            n = 1
        n += 1
    return i

if __name__ == "__main__":
    mult35(10)
    lpf(13195)
    smallestmult(10)

