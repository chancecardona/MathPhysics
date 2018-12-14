# ASSIGNMENT NAME: Midterm Review
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 10/7/18
# DESCRIPTION: All review problems. Tests at bottom. Just run this file.
# GRADING NOTES: Just run this file and it will output what you want.
# OTHER NOTES: (if applicable)

import numpy as np, math, matplotlib.pyplot as plt

# A
def mult35(N):
    sum = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# B
def lpf(N):
    i = 2
    while i <= N**0.5:
        if N % i == 0:
            N = N // i
        else:
            i += 1
    return N

# C
def smallestmult(N):
    if N <= 2:
        return N
    lcm = N
    N -= 1
    while N > 1:
        lcm = (lcm * N) / gcd(lcm, N)
        N -= 1
    return int(lcm)
    #Euclids algorithm for greatest common denominator
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# D
def primes(N):
    size = int(2 * N * math.log(N))
    arr = [True] * (size)
    arr[0] = arr[1] = False

    for i in range(2, int(size**0.5 + 1)):
        if arr[i]:
            for z in range(i*i, size, i):
                arr[z] = False

    num = 0
    a = 1
    while num < N:
        if arr[a]:
            num += 1
        a += 1
    return a - 1

# E
def pythagtrip(N):
    for i in range(1, N):
        a = i
        for j in range(a, N):
            b = j
            c = (a**2 + b**2)**0.5
            if c % 1 == 0 and a + b + c == N:
                return int(a * b * c)

# F
    #matrix x vector multiplication
def mxv(m, v):
    vector = []
    for i in range(len(m)):
        sum = 0
        for j in range(len(m[i])):
            sum += m[i][j] * v[j]
        vector.append(sum)
    return vector

    #matrix x matrix multiplication (doesnt care if square..)
def mxm(m1, m2):
    matrix = []
    m2Trans = np.transpose(m2)
    # does matrix x vector mult with every column of m2
    for i in range(len(m2Trans)):
        matrix.append(mxv(m1, m2Trans[i]))
    return np.transpose(matrix)

# G

def oscillators(steps):
    finaltime = 100
    dt = finaltime/steps
    time = np.linspace(0, finaltime, steps + 1)

    print("Step size:", dt)

    omega = 1
    gamma = 0.05
    f = 0.5
    m = 1
    epsilon = 0.05

    #Position and velocity arrays for the driven oscillator
    x = np.zeros(steps + 1)
    v = np.zeros(steps + 1)
    #Position and velocity arrays for Mathieu oscillator
    xM = np.zeros(steps + 1)
    vM = np.zeros(steps + 1)
    x[0] = 1
    xM[0] = 1

    # Eulers Method
    for i in range(0, steps):
        x[i+1] = v[i] * dt + x[i]
        v[i+1] = ( ((f / m) * np.sin(omega * i * dt)) + (-omega**2 * x[i]) + (-2 * gamma * v[i]) ) * dt + v[i]

        xM[i+1] = vM[i] * dt + xM[i]
        vM[i+1] = (-(omega**2) * (1 - 2*epsilon*np.cos(2 * omega * dt * i)) * xM[i] ) * dt + vM[i]

    # Plots everything
    plt.plot(time, x, 'b-', label='Driven Oscillator')
    plt.plot(time, xM, 'r-', label='Mathieu Oscillator')
    plt.legend()
    plt.show()


# H
def power_digit_sum(n): 
    # finds 2^n power.
    pow = 2**n
    # counts digits by casting to a string.
    strPow = str(pow)
    sum = 0
    for c in strPow:
        sum += int(c)
    return sum

# I
def factorial_digit_sum(n): 
    # Finds factorial of n
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    # counts digits of factorial by casting to a string
    strFact = str(fact)
    sum = 0
    for c in strFact:
        sum += int(c)
    return sum

# J
def nth_digit_fibonacci(n):
    # initialize variables 
    fibLen = 0
    f = [1, 1]
    i = 2
    # calculates next fibonacci number until it has n digits.
    while fibLen < n:
        f.append(f[i-1] + f[i-2])
        fibLen = len(str(f[i]))
        i += 1
    return i


# K
def CoupledOscillators(steps):
    finaltime = 100
    dt = finaltime/steps
    time = np.linspace(0, finaltime, steps + 1)

    print("Step size:", dt)

    k = 1
    m = 1

    #Position and velocity arrays for the 3 oscillators
    oscillators = np.zeros((3,2,steps+1))

    # First mass
    oscillators[0][0][0] = 0
    oscillators[0][1][0] = 1

    #second Mass
    oscillators[1][0][0] = 0
    oscillators[1][1][0] = 1

    #3rd mass
    oscillators[2][0][0] = -1
    oscillators[2][1][0] = 1

    # Eulers Method
    for n in range(0, steps):
        oscillators[0][0][n+1] = oscillators[0][1][n] * dt + oscillators[0][0][n]
        oscillators[1][0][n+1] = oscillators[1][1][n] * dt + oscillators[1][0][n]
        oscillators[2][0][n+1] = oscillators[2][1][n] * dt + oscillators[2][0][n]

        oscillators[0][1][n+1] = (-k/m*oscillators[0][0][n]       \
        + k/m*(oscillators[1][0][n] - oscillators[0][0][n])) * dt \
        + oscillators[0][1][n]

        oscillators[1][1][n+1] = (-k/m*(oscillators[1][0][n] - oscillators[0][0][n]) \
        + k/m*(oscillators[2][0][n] - oscillators[1][0][n])) * dt \
        + oscillators[1][1][n]

        oscillators[2][1][n+1] = (-k/m*(oscillators[2][0][n] - oscillators[1][0][n]) \
        - k/m*oscillators[2][0][n]) * dt + oscillators[2][1][n]

    # Plots everything
    plt.plot(time, oscillators[0][0], 'b-', label='M1')
    plt.plot(time, oscillators[1][0], 'r-', label='M2')
    plt.plot(time, oscillators[2][0], 'g-', label='M3')
    plt.legend()
    plt.show()

# Test / Output
if __name__ == "__main__":
    print('A:', mult35(1000))
    print('B:', lpf(600851475143))
    print('C:', smallestmult(20))
    print('D:', primes(10001))
    print('E:', pythagtrip(1000))

    print('F: \nMatrix Vector:', mxv([[2,1,2],[3,3,2],[1,1,2]], [2,3,2]))
    A = [[1,2,3],[4,3,1]]
    B = [[2,3,2,2],[1,4,2,6],[8,1,4,6]]
    print('Matrix Matrix \n', mxm(A, B))
    print('Square Matrix Matrix \n', mxm(B,np.transpose(B)))

    print("G: 2 Different Harmonic Oscillators:")
    oscillators(1000)
    oscillators(10000)
    oscillators(100000)
    oscillators(1000000)
    
    print('H:', power_digit_sum(1000))
    print('I:', factorial_digit_sum(100))
    print('J:', nth_digit_fibonacci(1000))

    print('K: 3 Coupled Oscillators')
    CoupledOscillators(100000)