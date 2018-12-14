# ASSIGNMENT NAME: Project 1: Damped Oscillators
# NAME: Chance Cardona, Cason Cropp
# EMAIL: ccardona@mymail.mines.edu ccropp@mymail.mines.edu
# DATE: 9/21/18
# DESCRIPTION: Numerically solves a damped oscillator equation using Euler's
#   method, RK4, and some error.
# GRADING NOTES: 
# OTHER NOTES: (if applicable)

import numpy as  np
import matplotlib.pyplot as plt

def f(x, v, w, y):
    return -w**2 * x - 2*y * v


def damped_euler(steps, finaltime, omega, gamma):
    # dt is time between steps
    dt = finaltime / steps

    # create arrays for the position and velocity of the equation
    x = np.zeros(steps + 1)
    v = np.zeros(steps + 1)

    # set initial conditions. Change to whatever is appropriate.
    # may add ability to set these when calling the function.
    x[0] = 1
    v[0] = 0

    # do a discretization calculation for every step
    for n in range(0, steps):
        # Discretization code of form
        # v[n+1] = f(v[n],x[n], omega, gamma)
        # x[n+1] = g(v[n],x[n])

        # do position first.
        x[n+1] = v[n] * dt + x[n]
        # now velocity.
        v[n+1] = f(x[n], v[n], omega, gamma) * dt + v[n]

    return([x,v])


def damped_rk4(steps, finaltime, omega, gamma):
    # dt is time between steps
    dt = finaltime / steps

    # create arrays for the position and velocity of the equation
    x = np.zeros(steps + 1)
    v = np.zeros(steps + 1)

    # set initial conditions. Change to whatever is appropriate.
    # may add ability to set these when calling the function.
    x[0] = 1
    v[0] = 0

    # do a discretization calculation for every step
    for n in range(0, steps):
        # Discretization code of form
        # v[n+1] = dt * f(v[n],x[n], omega, gamma) + v[n]
        # x[n+1] = dt * g(v[n],x[n]) + x[n] where g is velocity(t)
        xk1 = dt * v[n]
        vk1 = dt * f(x[n],v[n],omega,gamma)
        xk2 = dt * (v[n] + vk1 / 2)
        vk2 = dt * f(x[n] + xk1/2,v[n] + vk1/2,omega,gamma)
        xk3 = dt * (v[n] + vk2 / 2)
        vk3 = dt * f(x[n] + xk2/2,v[n] + vk2/2,omega,gamma)
        xk4 = dt * v[n+1]
        vk4 = dt * f(x[n+1],v[n+1],omega,gamma)
        
        x[n+1] = x[n] + (xk1 + 2*xk2 + 2*xk3 + xk4)/6
        v[n+1] = v[n] + (vk1 + 2*vk2 + 2*vk3 + vk4)/6
    return([x,v])



def main():

    steps = 10**3

    finaltime = 100

    dt = finaltime/steps

    print("Time step is", dt)

    time = np.linspace(0, finaltime, steps + 1)

    # Call the damped oscillator numerical solver function
    w = 1
    lamba = 0.05
    x1 = damped_euler(steps, finaltime, w, lamba)[0]
    rk4 = damped_rk4(steps, finaltime, w, lamba)[0]

    # plot this with the time array
    plt.plot(time, x1, 'b-', label = 'Euler Method')
    plt.plot(time, rk4, 'r-', label = 'Runge Kutta 4')

    plt.xlabel('t', fontsize = 15)
    plt.ylabel('x(t)', fontsize = 15)
    plt.title("Damped oscillator with time step = {}s".format(dt))
    plt.legend(loc = 'upper right')

    plt.show()

    return

main()
