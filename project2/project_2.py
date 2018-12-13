#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i,x,y,line,trace):

    if i >= np.shape(x)[0]:
        i = i % np.shape(x)[0]

    line.set_data(x[i],y[i])
    trace.set_data(x[:i],y[:i])

    return line,trace

def euler(final_time, steps, c,e,E,m,p0):
    dt = final_time/(steps-1)

    t = np.linspace(0,final_time,steps)
    x = np.zeros(steps)
    y = np.zeros(steps)
    vx = np.zeros(steps)
    vy = np.zeros(steps)
    x[0] = 0
    y[0] = 0
    vx[0] = 0
    vy[0] = p0

    for i in range(steps-1):
        x[i+1] = x[i] + vx[i]*dt
        y[i+1] = y[i] + vy[i]*dt
        vx[i+1] = c*e*E*t[i+1]/np.sqrt(c**2*m**2+(e*E*t[i+1])**2)
        vy[i+1] = p0*c/np.sqrt(c**2*m**2+(e*E*t[i+1])**2)

    return x,y

def analytical(final_time, steps, c,e,E,Ke_0,p_0):
    t = np.linspace(0,final_time,steps)

    x = np.zeros(steps)
    y = np.zeros(steps)

    x_func = lambda t: np.sqrt(Ke_0**2 + (c*e*E*t)**2)/(e*E) - Ke_0
    y_func = lambda t: np.arcsinh(c*e*E*t/Ke_0)*p_0*c/(e*E)

    for i in range(steps):
        x[i] = x_func(t[i])
        y[i] = y_func(t[i])

    return x,y

if __name__=="__main__":
    # plotting parameters
    steps = 1000
    final_time = pow(10,-6)

    # define constants/ parameters
    E = 1*pow(10,5)          # farads [s^4*A^2/m^2kg^2]
    e = 1.602177 * pow(10,-19) # elementary charge [coulombs or A/s]
    m = 9.10938 * pow(10,-31)  # electron mass in kg
    c = 3*10**8                 # speed of light through a vacuum
    v_0 = 1*10**8                # relativistic initial velocity

    # calculated from init vals
    v0 = [v_0, v_0/2, v_0/pow(10,4), v_0/pow(10,8)]
    p_0 = np.zeros(4)
    Ke_0 = np.zeros(4)
    for j in range(4):
        p_0[j] = m*v0[j] * 1/(np.sqrt(1-v0[j]**2/c**2))
        Ke_0[j] = c*np.sqrt(m**2*c**2 + p_0[j]**2)

    # we can use analytical result
    x_arr = np.zeros((4,steps))
    y_arr = np.zeros((4,steps))
    for i in range(4):
        x_arr[i],y_arr[i] = analytical(final_time,steps,c,e,E,Ke_0[i],p_0[i])

    # scipy quandrature integration result

    
    # and discretization from Euler
    x_num = np.zeros((4,steps))
    y_num = np.zeros((4,steps))
    for i in range(4):
       x_num[i],y_num[i] = euler(final_time,steps,c,e,E,m,p_0[i])

    # the result we expect to get (eqn 20.5) for relativistic systems
    # can be used to check all other methods, or first relativistic case
    catenary = lambda y,Ke_0,p_0: Ke_0/(e*E) * np.cosh(e*E*y/p_0/c) - Ke_0/(e*E)
    parabola = lambda y,m,v: e*E/(2*m*v**2)*y**2
    x = np.zeros((4,steps))
    xx = np.zeros((4,steps))

    # for j in range(4):
        # for i in range(steps):
            # x[j][i] = catenary(y_arr[j][i],Ke_0[j],p_0[j])
            # xx[j][i] = parabola(y_arr[j][i],m,v0[j])

    # also plot them all
    t = np.linspace(0,final_time,steps)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(2,2,1)
    ax2 = fig1.add_subplot(2,2,2,sharex=ax1)
    ax3 = fig1.add_subplot(2,2,3,sharex=ax1)
    ax4 = fig1.add_subplot(2,2,4,sharex=ax1)
    ax1.plot(x_arr[0],y_arr[0], label = "Analytical")
    ax1.plot(x_num[0],y_num[0], label = "Numerical")
    # ax1.plot(xx[0],y_arr[0])
    ax2.plot(x_arr[1],y_arr[1])
    ax2.plot(x_num[1],y_num[1])
    # ax2.plot(xx[1],y_arr[1])
    ax3.plot(x_arr[2],y_arr[2])
    ax3.plot(x_num[2],y_num[2])
    # ax3.plot(xx[2],y_arr[2])
    ax4.plot(x_arr[3],y_arr[3])
    ax4.plot(x_num[3],y_num[3])
    # ax4.plot(xx[3],y_arr[3])
    ax1.set_title('V0 = ' + str(round(v0[0]/c,4)) + 'c')
    ax2.set_title('V0 = ' + str(round(v0[1]/c,4)) + 'c')
    ax3.set_title('V0 = ' + str('{:0.3e}'.format(v0[2]/c,4)) + 'c')
    ax4.set_title('V0 = ' + str('{:0.3e}'.format(v0[3]/c,4)) + 'c')
    ax1.set_xlabel('x postion [m]')
    ax1.set_ylabel('y postion [m]')
    ax2.set_xlabel('x postion [m]')
    ax2.set_ylabel('y postion [m]')
    ax3.set_xlabel('x postion [m]')
    ax3.set_ylabel('y postion [m]')
    ax4.set_xlabel('x postion [m]')
    ax4.set_ylabel('y postion [m]')
    ax1.legend()

    fig2 = plt.figure()
    ax = fig2.add_subplot(111,xlim=(0,300),ylim=(0,9))
    line, = ax.plot([],[],'b*',lw=2, label='electron')
    trace, = ax.plot([],[],'r--',lw=2, label='catenary trajectory')
    x0 = x_arr[0][0]
    xf = x_arr[0][-1]
    efield, = ax.plot([0,xf],[1,1],'c-', label='E-field')
    efield, = ax.plot([0,xf],[3,3],'c-')
    efield, = ax.plot([0,xf],[5,5],'c-')
    efield, = ax.plot([0,xf],[7,7],'c-')
    ax.arrow(50, 1, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(50, 3, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(50, 5, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(50, 7, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(50, 9, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(250, 1, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(250, 3, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(250, 5, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(250, 7, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.arrow(250, 9, 10, 0, shape="full", lw=1, length_includes_head=True, head_length=4, head_width=.2, color="c")
    ax.set_xlabel('x position [m]')
    ax.set_ylabel('y position [m]')
    ax.legend(loc='upper left')
    ax.set_title('Motion of relativistic electron in constant uniform e-field')

    ani = FuncAnimation(fig2,animate,interval=10,blit=True,repeat=True,fargs=(x_arr[0][:],y_arr[0][:],line,trace))

    plt.show()
