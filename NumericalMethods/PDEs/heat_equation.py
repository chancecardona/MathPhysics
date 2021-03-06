# ASSIGNMENT NAME: HW 8
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 12/2/18
# DESCRIPTION: Heat equations with initial condition u = sin(x(l-x))
# OTHER NOTES: I'm not sure I implemented the init cond correctly as it's kind of odd,
# but it looks good atleast.

import scipy as sp
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import numpy as np
import time

def time_evolve(xfin, tfin, Nx, Nt):

    dx = xfin/(Nx * 1.0)

    dt = tfin/(Nt * 1.0)

    u = np.zeros((Nt + 1, Nx + 1))

    # define inintial tempereatures for both ends of the rod
    u[0][0] = 0
    u[0][-1] = 0

    for ll in range(0, Nx + 1):
        # u[0][ll] = np.sin(np.pi*ll*dx / xfin)
        # u[0][ll] = ll*dx*(xfin - ll*dx)
        u[0][ll] = np.sin(ll*dx * (xfin - ll*dx))
        # define initial temperture distribution over the rod  at t=0

    print("The initial conditions are", u[0,:])

    R = 0.5

    for kk in range(0, Nt):
        for ll in range(1, Nx):
            # discretize heat equation here
            u[kk+1][ll] = u[kk,ll] - R*2*u[kk,ll] + R*u[kk,ll+1] + R*u[kk,ll-1]

    return u


def main_static():

    Nx = 10**1
    Nt = 10**2

    xfin = 1
    tfin = 10

    dx = xfin/(Nx * 1.0)

    dt = tfin/(Nt * 1.0)

    time = np.linspace(0, tfin, Nt + 1)

    space = np.linspace(0, xfin, Nx + 1)

    # call for u
    u = time_evolve(xfin, tfin, Nx, Nt)
    #print("The array of tempereatures is", u)

    plt.plot(time, u[:, 0], 'g-', label='u(x=0)')


    fig = plt.figure()

    for tt in range(0, Nt + 1):

        print("Time is ", tt*dt)

        # plot tmperature vs x

    plt.show()

    return u

main_static()

def main_dynamic():

    Nx = 10**2
    Nt = 10**3

    xfin = np.pi
    tfin = 1000

    dx = xfin/(Nx * 1.0)

    dt = tfin/(Nt * 1.0)

    time = np.linspace(0, tfin, Nt + 1)

    space = np.linspace(0, xfin, Nx + 1)

    # call for u
    u = time_evolve(xfin, tfin, Nx, Nt)

    fig = plt.figure()
    temps = []

    ax = fig.add_subplot(111)

    time_template = 'time = %.01fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    for tt in range(0, Nt):

        p, = plt.plot(u[tt,:], 'r-', label='theta(t)')

        #tm = plt.text(0.05, 0.9, time_template % (tt*dt))

        temps.append([p])



    ani = animation.ArtistAnimation(fig, temps, interval=10, repeat_delay=10)

    plt.show()


# main_dynamic()
