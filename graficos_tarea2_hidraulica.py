#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:26:43 2020

@author: felipe
"""
     
import math as m
import numpy as np
import matplotlib.pyplot as plt


def alfa(h):
    return m.asin((h-4)/4)
alfa = np.vectorize(alfa)


def A1(h):
    return 3/4*h

def A2 (h):
    return (7/8)*h**2+h-5/2

def A3(h):
    return 15.5 + alfa(h)*4 + (h-4)*m.cos(alfa(h))*4
A3=np.vectorize(A3)


def P1(h):
    return 2.53*h

def P2(h):
    return 2.66*h + 1.23

def P3(h):
    return 8*alfa(h)+11.87

def l1(h):
    return 3/2*h

def l2(h):
    return 7/4*(h-2)+4.5

def l3(h):
    return 8 * m.cos(alfa(h))
l3 = np.vectorize(l3)

def R1(h):
    return 0.296*h 

def R2(h):
    return (0.875*h**2 + h - 2.5)/(2.66*h+1.23)

def R3(h):
    return (4*alfa(h) + 15.5 + ((h-4)* m.cos(alfa(h))*4)) / (8*alfa(h)+11.87)
R3 = np.vectorize(R3)

def h1(h):
    return h/2

def h2(h):
    return (0.875*h**2+h-2.5)/(1.75*h+4.5)

def h3(h):
    return (15.5 + alfa(h)*4 + (h-4)*m.cos(alfa(h))*4 )/(8 * m.cos(alfa(h)))
h3= np.vectorize(h3)


A = [A1, A2, A3]
P = [P1, P2, P3]
l = [l1, l2, l3]
R = [R1, R2, R3]
h = [h1, h2, h3]

x = np.linspace(0,8,500)
yA = np.piecewise(x, [x<=2, np.logical_and(x>2,x<=4), np.logical_and(x>4,x<8) ], A )
yP = np.piecewise(x, [x<=2, np.logical_and(x>2,x<=4), np.logical_and(x>4,x<8) ], P )
yl = np.piecewise(x, [x<=2, np.logical_and(x>2,x<=4), np.logical_and(x>4,x<8) ], l )
yR = np.piecewise(x, [x<=2, np.logical_and(x>2,x<=4), np.logical_and(x>4,x<8) ], R )
yh = np.piecewise(x, [x<=2, np.logical_and(x>2,x<=4), np.logical_and(x>4,x<8) ], h )

plt.plot(x,yA, label='Area')
plt.plot(x,yP, label='perimetro mojado')
plt.plot(x,yl, label='ancho superficial')
plt.plot(x,yR, label='radio hidraulico')
plt.plot(x,yh, label='profundidad hidraulica')
plt.legend()
plt.show()



print((24.52 * 20)/(m.sqrt(9.81*2.91)))

print(4.42875*20/(m.sqrt(9.81*5.278)))
