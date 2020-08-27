
"""
encontrar raizes de ecuaciones

Created on Tue Aug 18 07:07:08 2020

@author: felipe

"""

### parte 2 
#grafico de ecuacion
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def f_h(h):
    res= (9.81/150**2)-(((4/7)*(h-2)+4.5) / ((7/8)*h**2+(h)-5/2)**3) 
    return res

X = list(np.linspace(1.5, 4.5 , 50))

Y = list(map(f_h, X))

plt.plot(X, Y)
plt.show()

# resolver numericamente

def biseccion(a,b):
    c = a+b/2
    if h_f(c) < 0:
        return c, b
    if c>0 :
        return a, c
    
for i in range(20):
    


"""
### parte 3
import math
import numpy as np
import matplotlib.pyplot as plt

def f3_h(h):
    res= 0.000436-((4/7)*(h-2)+4.5) / ((7/8)*h**2+(h)-5/2) 
    return res

X = list(np.linspace(1.5, 4.5 , 50))

Y = list(map(f3_h, X))

plt.plot(X, Y)
plt.show()

"""