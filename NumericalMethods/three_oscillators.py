# ASSIGNMENT NAME: Homework 03 Part 2: Three Oscillators
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 9/17/18
# DESCRIPTION: Numerically solves a system of 3 oscillators using eulers meth
# GRADING NOTES: 
# OTHER NOTES: (if applicable)


import numpy as  np
import matplotlib.pyplot as plt

def time_evolution(steps, finaltime):

    # First we need to define our dt, the time between steps in
    # our simulation. Break the total time (finaltime) into a
    # number of steps
    dt = finaltime/steps

    # here we initialize our variable to track the states of the
    # oscillators. Put this in a terminal and print it if you're
    # unsure of what it looks like
    # The change here is the 3, to make a set of data for each mass
    oscillators = np.zeros((3,2,steps+1))

    # set the initial conditions for the first mass
    # which is accessed by putting 0 into the first index
    # oscillators[0] gets mass 1
    # oscillators[0][0] gets the array of x positions for mass 1
    # oscillators[0][0][0] sets the first x value for mass 1
    oscillators[0][0][0] = 0
    # oscillators[0][1] gets the array of v for mass 1
    # this initial velocity is set in the same manner
    oscillators[0][1][0] = 1

    # now set the initial conditions for the second mass, indexed
    # at 1
    # Set the initial x position
    oscillators[1][0][0] = 0
    # set the initial v
    oscillators[1][1][0] = 1

    # TODO: set the initial conditions for mass 3 yourself. Set the
    # position to -1 and the velocity to 1
    oscillators[2][0][0] = -1
    oscillators[2][1][0] = 1    

    # Set our mass and spring constants
    k = 1
    m = 1

    # do a discretization calculation for every step
    for n in range(0, steps):

        # here goes your discretization code
        # i.e. v[n+1] = f(v[nn],x[nn])
        # along with x[n+1] = g(v[nn],x[nn])

        # first do the x positions. Check against the equation
        # in the instructions to match it up
        # oscillators[0][0][n+1] accesses the first mass,
        # its position array, and the value at timestep n + 1
        # the velocity is multiplied by dt to get the change
        # velocity at step n is accessed by oscillators[0][1][n]
        # and the position before the change is added
        oscillators[0][0][n+1] = oscillators[0][1][n] * dt + oscillators[0][0][n]
        # do the same for mass 2
        oscillators[1][0][n+1] = oscillators[1][1][n] * dt + oscillators[1][0][n]
        # now do this for mass 3
        oscillators[2][0][n+1] = oscillators[2][1][n] * dt + oscillators[2][0][n]
        # now we need to do the discretization for the velocity.
        # check the equations in the instructions, and apply it here
        # the first is done for you
        # backslashes are used to break the equation across
        # multiple lines since it is so long
        # check all of the first indices to understand which mass
        # each term is referring to
        oscillators[0][1][n+1] = (-k/m*oscillators[0][0][n]       \
        + k/m*(oscillators[1][0][n] - oscillators[0][0][n])) * dt \
        + oscillators[0][1][n]
        # now do it for mass 2. There are some hints left here for you
        oscillators[1][1][n+1] = (-k/m*(oscillators[1][0][n] - oscillators[0][0][n]) \
        + k/m*(oscillators[2][0][n] - oscillators[1][0][n])) * dt \
        + oscillators[1][1][n]
        # do it for mass 3 from scratch.
        oscillators[2][1][n+1] = (-k/m*(oscillators[2][0][n] - oscillators[1][0][n]) \
        - k/m*oscillators[2][0][n]) * dt + oscillators[2][1][n]


    return(oscillators)


def oscillator():

    steps = 10**4

    finaltime = 100

    dt = finaltime/steps

    print("Time step is", dt)

    time = np.linspace(0, finaltime, steps + 1.0)

    # call for function time_evolution(steps, finaltime)
    # and plot position of the oscillator as a function of time
    # since the time_evolution function returns everything we need
    # in one variable, lets save this in data
    data = time_evolution(steps, finaltime)

    # with this data, we want to separately plot the position of
    # each mass
    # data[0] gets info for the first mass, and the next index
    # gets either position or velocity. [0] for position
    x1 = data[0][0]
    x2 = data[1][0]
    x3 = data[2][0]

    # each time we call plot, it adds a separate function to our
    # full plot, until we show the image with all the plots
    # the third argument specifies the color and drawing style.
    # check out matplotlib documentation online if you want to see
    # more about this.
    plt.plot(time, x1, 'b-')
    plt.plot(time, x2, 'r-')
    plt.plot(time, x3, 'g-')

    plt.xlabel('t', fontsize = 15)
    plt.ylabel('x(t)', fontsize = 15)
    plt.title("Three oscillators with time step={}".format(dt))

    plt.legend()

    plt.show()

    return




oscillator()
