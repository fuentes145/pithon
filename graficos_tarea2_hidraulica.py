#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:26:43 2020

@author: felipe
"""
     
import math as m

def alfa(h):
    return m.asen((h-4)/4)

def A1(h):
    return 3/4*h

def A2 (h):
    return (7/8)*h**2+h-5/2

def A3(h):
    return 15.5 + alfa(h)*4 + (h-4)*m.cos(alfa(h))*4


def P1(h):
    return 2.53*h

def P2(h):
    return 2.66*h - 0.84

def P3(h):
    return 8*alfa(h)

def l1(h):
    return 3/2*h

def l2(h):
    return 7/4*(h-2)+4.5

def l3(h):
    return 8*m.cos(alfa(h))

def R1(h):
    return 0.296*h 

def R2(h):
    return (0.875*h**2 + h - 2.5)/(2.66*h-0.84)

def R3(h):
    return 1.94/alfa(h) + 0.5 + ((h-4)* m.cos(alfa(h))) / (2*alfa(h))



    