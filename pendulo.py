import numpy as np
from matplotlib import pyplot

# constantes
g = 9.81
L = 2
u = 0.5

dt = 0.05
# condiciones iniciales
Theta = np.pi
d_Theta = -0.001

def ecuacion(theta, d_theta):
    return -u*d_theta - (g/L)*np.sin(theta)

def solucion(t):
    theta = Theta
    d_theta = d_Theta
    a = np.arange(0, t, dt)
    thetas = np.arange(0, t, dt)
    s = 0
    for i in a:
        thetas[s] = theta        
        dd_theta = ecuacion(theta, d_theta)
        d_theta = d_theta + dt * dd_theta 
        theta = theta + dt * d_theta
        s+=1

    
    pyplot.plot(a, thetas)
    pyplot.show()
    return theta

print(solucion(10))