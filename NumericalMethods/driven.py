# ASSIGNMENT NAME: HW 5
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 10/18/18
# DESCRIPTION: 3rd Order ODE approximated with Eulers method.
# OTHER NOTES: (if applicable)

import numpy as np, matplotlib.pyplot as plt

def drivenOscillator(steps, finaltime, F0, omega, gamma):
    dt = finaltime / steps
    print("Step size:", dt)
    time = np.linspace(0, finaltime, steps + 1)

    m = 1
    w = 5 * omega

    # Position and velocity arrays for the driven oscillator
    x = np.zeros(steps + 1)
    v = np.zeros(steps + 1)
    a = np.zeros(steps + 1)
    x[0] = 1

    # Eulers Method
    # I took the derivative of the integral-differential eqn given, so that it 
    # is "simply" a 3rd order ODE. 
    for i in range(0, steps):
        x[i+1] = v[i] * dt + x[i]
        v[i+1] = a[i] * dt + v[i]
        a[i+1] = ( F0/m * np.sin(w * i*dt) * x[i] - omega**2 * v[i] - 2*gamma * a[i] ) * dt + a[i]

    # Plots everything
    plt.plot(time, x, 'b-', label='Driven Oscillator')
    plt.show()

if __name__ == '__main__':
    # Plots for each time step.
    drivenOscillator(250, 25, 10, 1, 0.05)
    drivenOscillator(2500, 25, 10, 1, 0.05)
    drivenOscillator(25000, 25, 10, 1, 0.05)
    drivenOscillator(250000, 25, 10, 1, 0.05)