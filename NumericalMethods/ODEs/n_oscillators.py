# ASSIGNMENT NAME: Homework 03 Part 2: N Oscillators
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 9/17/18
# DESCRIPTION: Numerically solves a system of n oscillators using eulers meth
# GRADING NOTES: 
# OTHER NOTES: (if applicable)

import numpy as  np
import matplotlib.pyplot as plt

# NOTE: This function now has an input for n
def time_evolution(steps, finaltime, n):

    # First we need to define our dt, the time between steps in
    # our simulation. Break the total time (finaltime) into a
    # number of steps
    dt = finaltime / steps

    # here we initialize our variable to track the states of the
    # oscillators. Put this in a terminal and print it if you're
    # unsure of what it looks like
    # This time, you will define this yourself. Keep in mind the first
    # dimension is the number of oscillators
    oscillators = np.zeros((n, 2, steps+1))

    # NOTE: setting the initial conditions is required for each mass.
    # This is done for you, and the initial position increases by 0.5
    # for each mass. All have the same initial velocity
    x = 0
    for i in range(n):
        # set the initial position for each, and increase for the next
        oscillators[i][0][0] = x
        x += 0.5

        # set the initial velocity of each to 1
        oscillators[i][1][0] = 1


    # Set our mass and spring constants
    k = 1
    m = 1

    # do a discretization calculation for every step
    # NOTE: we are using nn since n is already defined
    for nn in range(0, steps):

        # here goes your discretization code
        # i.e. v[n+1] = f(v[nn],x[nn])
        # along with x[n+1] = g(v[nn],x[nn])

        # first do the x positions. Check against the equation
        # in the instructions to match it up
        # oscillators[0][0][n+1] accesses the first mass,
        # its position array, and the value at timestep n + 1
        # the velocity is multiplied by dt to get the change
        # velocity at step n is accessed by oscillators[0][1][nn]
        # and the position before the change is added
        # TODO: the position calculation for each mass is similar.
        # Use the following for loop to do the position calculation for
        # each mass (i) at the current step (nn)
        for i in range(n):
            oscillators[i][0][nn+1] = oscillators[i][1][nn] * dt \
            + oscillators[i][0][nn]

        # now we need to do the discretization for the velocity.
        # check the equations in the instructions, and apply it here
        # backslashes can be used to break the equation across
        # multiple lines since it is so long
        # NOTE: As mentioned in the instructions, the first and last masses
        # have unique equations, and all the inner masses have a similar
        # form. First implement the equations for the first and last masses
        # Pay attention to when n is used and when nn is used
        oscillators[0][1][nn+1] = (-k/m*oscillators[0][0][nn]       \
        + k/m*(oscillators[1][0][nn] - oscillators[0][0][nn])) * dt \
        + oscillators[0][1][nn]

        # now do it for the last mass.
        oscillators[n-1][1][nn+1] = (-k/m*(oscillators[n-1][0][nn] - oscillators[n-2][0][nn]) \
        - k/m*oscillators[n-1][0][nn]) * dt + oscillators[n-1][1][nn]

        # do it for the rest of the masses. Put in the parameters for
        # the for loop to do this for the second and second to last mass
        for i in range(1 , n - 1):
            # implement the discretization for mass i
            oscillators[i][1][nn+1] = (-k/m*(oscillators[i][0][nn] - oscillators[i-1][0][nn] ) \
            + k/m*(oscillators[i+1][0][nn] - oscillators[i][0][nn])) * dt \
            + oscillators[i][1][nn]

    return(oscillators)


def oscillator(n):

    steps = 10**4

    finaltime = 100

    dt = finaltime/steps

    print("Time step is", dt)

    time = np.linspace(0, finaltime, steps + 1.0)

    # call for function time_evolution(steps, finaltime)
    # and plot position of the oscillator as a function of time
    # since the time_evolution function returns everything we need
    # in one variable, lets save this in data
    data = time_evolution(steps, finaltime, n)

    # with this data, we want to separately plot the position of
    # each mass
    # data[0] gets info for the first mass, and the next index
    # gets either position or velocity. [0] for position
    # NOTE: with n oscillators, we have to loop through these.
    # We need a color for each oscillator, so we'll make a list of these
    # options. Extend this or come up for a solution to go beyond the
    # length of this list if n is greater.
    colors = ['r-', 'b-', 'g-', 'y-', 'o-', 'r--', 'b--']
    
    # We will plot directly from the dataset
    for i in range(n):
        plt.plot(time, data[i][0], colors[i])

    plt.xlabel('t', fontsize = 15)
    plt.ylabel('x(t)', fontsize = 15)
    plt.title("N oscillators with time step={}"
    .format(dt))

    plt.legend()

    plt.show()

    return



# Change this input to change the number of oscillators
oscillator(4)
