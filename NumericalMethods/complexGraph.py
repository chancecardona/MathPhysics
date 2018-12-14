import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import quad

def prob1(theta, eps):
    return 1/(1+ eps*np.sin(theta))

def prob2_a(theta, a, b):
    return 1/(a + b * np.sin(theta))**2

def prob2_b(theta, a, b):
    return np.sin(theta) / (a + b * np.sin(theta))**2

def prob3(x):
    return 1/(1+x**2)**3

def prob4(x, n):
    return 1/(1+x**(2*n))

def prob5_a(x, a):
    return np.cos(x) / (a**2 + x**2)

def prob5_b(x, a):
    return x * np.sin(x) / (a**2 + x**2)

def an1(eps):
    return 2 * np.pi / (1 - eps**2)**0.5

def an2(a, b):
    return 2*a*np.pi / (a**2 - b**2)

def an4(n):
    return np.pi / (2 * n * np.sin( np.pi / (2 * n)))

def an5_a(a):
    return np.exp(-a) * np.pi / a

def an5_b(a):
    return np.exp(-a) * np.pi


def plotIt(x, yAnal, yNum, lab):
    plt.subplot(121)
    plt.plot(x, yAnal, 'b-', label="Analytical")
    plt.plot(x, yNum, 'r-.', label="Numerical")
    plt.title("Numerical vs Analytical Integration")
    plt.xlabel(lab)
    plt.ylabel("I("+ lab +")")
    plt.legend()

    plt.subplot(122)
    plt.plot(x, abs(yNum - yAnal), 'b-')
    plt.title("Difference Between Results")
    plt.xlabel(lab)
    plt.ylabel(u'Δ' + lab)

    plt.show() 

n = 1000

# Analytically
eps1 = np.linspace(-1 + 1/n, 1 - 1/n, n)
# Numerically
num1 = np.zeros(n)
for i in range(n):
    num1[i] = quad(prob1, 0, 2*np.pi, args=(eps1[i]))[0]
plotIt(eps1, an1(eps1), num1, u'ε')


for i in range(n):
    num1[i] = quad(prob2_a, 0, 2*np.pi, args=(1, eps1[i]))[0]
plotIt(eps1, an2(1, eps1), num1, 'b')
for i in range(n):
    num1[i] = quad(prob2_b, 0, 2*np.pi, args=(1, eps1[i]))[0]
plotIt(eps1, -1 * an2(eps1, 1), num1, 'b')


num3 = quad(prob3, 0, 2*np.pi)[0]
plt.axhline(y=num3, color='r', linestyle='-.')
plt.axhline(y=(3*np.pi / 8), color='b')
plt.show()


ns = np.linspace(1, 10, 10)
num4 = np.zeros(10)
for i in range(10):
    num4[i] = quad(prob4, 0, 10**5, args=(ns[i]))[0]
plotIt(ns, an4(ns), num4, "n")


eps5 = np.linspace(0 + 1/n, 10, n)
num5 = np.zeros(n)
for i in range(n):
    num5[i] = quad(prob5_a, -10**5, 10**5, args=(eps5[i]))[0]
plotIt(eps5, an5_a(eps5), num5, "a")
for i in range(n):
    num5[i] = quad(prob5_b, -10**5, 10**5, args=(eps5[i]))[0]
plotIt(eps5, an5_b(eps5), num5, "a")
