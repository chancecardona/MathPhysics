# ASSIGNMENT NAME: FINAL
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/10/18
# DESCRIPTION: Numerical Wave Equation with Animation
# OTHER NOTES: (if applicable)

import scipy as sp, numpy as np, matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial condition of u
def f(x, L):
    return np.exp(-(x)**2) * (x)*(L - x)

# Initial condition of u'(t)
def g(x):
    return np.cos(2*x)


def time_evolve(xfin, tfin, Nx, Nt):
    dx = xfin/(Nx * 1.0)
    dt = tfin/(Nt * 1.0)
    u = np.zeros((Nt + 1, Nx + 1))

    c = 0.5
    r = c*dt/dx 
    # r = 0.5

    # Define boundary conditions of the string
    u[0][0] = 0
    u[0][-1] = 0

    # We will be using n as our time increment, m as our x.
    # Need to define first 2 rows before we can start.
    for m in range(0, Nx + 1):
        # our f(x) (initial condition of u)
        u[0][m] = f(dx*m, xfin)
        # our g(x) (initial condition of u'(t))
        u[1][m] = 0.5*(r**2)*(f(dx*(m+1), xfin) + f(dx*(m-1), xfin)) + (1 - r**2)*f(dx*m, xfin) + dt*g(dx*m)


    print("The initial conditions are", u[0,:])

    for n in range(1, Nt):
        for m in range(1, Nx):
            #numerical discretization of wave equation.
            u[n+1][m] = (r**2)*(u[n][m+1] - 2*u[n][m] + u[n][m-1]) + 2*u[n][m] - u[n-1][m]

    return u


def main_dynamic():
    Nx = 10**2
    Nt = 10**2
    xfin = 10
    tfin = 10
    dx = xfin/(Nx * 1.0)
    dt = tfin/(Nt * 1.0)
    space = np.linspace(0, xfin, Nx+1)

    # call for u
    u = time_evolve(xfin, tfin, Nx, Nt)

    fig = plt.figure()
    amps = []
    ax = fig.add_subplot(111)

    for tt in range(0, Nt):
        p, = plt.plot(space, u[tt,:], 'r-', label='theta(t)')
        # tm = plt.text(0.05, 0.9, time_template % (tt*dt))
        amps.append([p])
        # plt.plot(space, u[tt, :], 'r-')
        # plt.show()

    ani = animation.ArtistAnimation(fig, amps, interval=10, repeat_delay=10)
    plt.show()

main_dynamic()

