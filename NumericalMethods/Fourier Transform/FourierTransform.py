# ASSIGNMENT NAME: HW 7
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 11/19/18
# DESCRIPTION: Defining Fourier Transform functions.
# OTHER NOTES: Listed are a few different methods I tried. 2D dft works in matrix
# form now.
# At the bottom I have a function that just tests that my output is consistent
# with np's implementation over higher and higher N values.


import numpy as np, matplotlib.pyplot as plt, time

# Original slow method used to implement a bare bones DFT.
# def dft1(arr):
#     N = len(arr)
#     F_arr = np.zeros(N, dtype=np.complex_)
#     for k in range(N):
#         F_k = 0
#         for n in range(N):
#             F_k += arr[n] * np.exp(-2 * np.pi * 1j * k * n / N)
#         F_arr[k] = F_k
#     return F_arr

# This is a MUCH faster method, but I get memory errors on the meshgrid
# that is used to create a fourier matrix when k is too large. I think
# I could make this recursive like in a FFT, but that seems overkill
# for this assignment. But let it be known that this is my favored way of
# doing this. I would be really interested to see how you/gavriil did it
# tho in the future.

# def dft(arr):
#     N = len(arr)
#     F_arr = np.zeros(N, dtype=np.complex)
#     k = np.linspace(0,N-1,N)
#     h, v = np.meshgrid(k, k, sparse=True)
#     F_arr = np.dot(np.exp(-2j * np.pi * h*v / N), arr)
#     return F_arr

#My chosen method. It's not as fast as the one but it always works.
def dft(arr):
    N = len(arr)
    F_arr = np.zeros(N, dtype=np.complex)
    n = np.linspace(0,N-1,N)
    for k in range(N):
        F_arr[k] = np.dot(arr, np.exp(-2j * np.pi * k * n / N))
    return F_arr



def idft(F_arr):
    N = len(F_arr)
    arr = np.zeros(N, dtype=np.complex)
    k = np.linspace(0,N-1,N)
    for n in range(N):
        arr[n] = np.dot(F_arr, np.exp(2 * np.pi * 1j * k * n / N)) / N
    return arr


# This is just a bare bones 2D DFT. I could have done it using a similar method
# to the meshgrid one above, but it didn't work for high k so this one wouldn't 
# either.
def dft2(arr): #Accepts 2D array
    N = len(arr)
    F_arr = np.zeros(np.shape(arr), dtype=np.complex)
    for k in range(N):
        for l in range(N):
            F_kl = 0
            for m in range(N):
                for n in range(N):
                    F_kl += arr[m][n] * np.exp(-2j*np.pi * (k*m + l*n) / N)
            F_arr[k][l] = F_kl
    return F_arr


# Matrix form of 2D dft. Much faster.
def Fdft2(arr):
    N = len(arr)
    F_arr = np.zeros(N, dtype=np.complex)
    k = np.linspace(0,N-1,N)
    h, v = np.meshgrid(k, k, sparse=True)
    W = np.exp(-2j * np.pi * h*v / N)
    F_arr = np.matmul(np.matmul(W, arr), W)
    return F_arr


def idft2(F_arr):
    N = len(F_arr)
    arr = np.zeros(np.shape(F_arr), dtype=np.complex64)
    for m in range(N):
        for n in range(N):
            F_mn = 0
            for k in range(N):
                for l in range(N):
                    F_mn += F_arr[k][l] * np.exp(2j*np.pi * (k*m + l*n) / N) 
            arr[m][n] = F_mn / N**2
    return arr

#Matrix form of idft2. Much faster.
def Fidft2(arr):
    N = len(arr)
    F_arr = np.zeros(N, dtype=np.complex)
    k = np.linspace(0,N-1,N)
    h, v = np.meshgrid(k, k, sparse=True)
    W = np.exp(2j * np.pi * h*v / N)
    F_arr = np.matmul(np.matmul(W, arr), W) / N**2
    return F_arr




def f(x):
    return np.sin(50*2*np.pi*x) + np.sin(100*2*np.pi*x)

if __name__ == '__main__':
    for k in range(1, 4):
        print("N =", 10**k)
        y = np.random.randn(10**k)
        F_y = dft(y)
        y2 = np.random.randn(10**k,10**k)
        F_y2 = Fdft2(y2)

        # tick = time.time()
        # dft1(y)
        # tock = time.time()
        # dft(y)
        # tock1 = time.time()
        # F_y = np.fft.fft(y)
        # tock2 = time.time()

        # idft(F_y)
        # tock3 = time.time()
        # np.fft.ifft(F_y)
        # tock4 = time.time()

        # print("TIMES:", tock1 - tock, tock2 - tock1)
        # print("Inverse:", tock3 - tock2, tock4 - tock3) 

        print('Fourier Transform Test: ', np.allclose(F_y, np.fft.fft(y)))
        print('Inverse F Transform Test: ', np.allclose(idft(F_y), np.fft.ifft(F_y)))

        print('2D F Transform Test: ', np.allclose(F_y2, np.fft.fft2(y2)))
        print('2D Inverse F T Test: ', np.allclose(Fidft2(F_y2), np.fft.ifft2(F_y2)))

x = np.linspace(0,10,1001)
plt.plot(f(x))
plt.show()
plt.plot(-1j*dft(f(x)))
plt.show()