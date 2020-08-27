#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 08:20:09 2020

@author: felipe
"""
T = int(input())
for i in range(T):
    pa = 0
    pb = 0
    N = int(input())
    for i in range(N):
        puntos_a = 0
        puntos_b = 0
        a, b = input().split()
        for j in range(len(a)):
            pa += int(a[j])
        for j in range(len(b)):
            pb += int(b[j])
        if pb < pa :
            puntos_a +=1
        elif pb> pa:
            puntos_b +=1
        else:
            puntos_a+=1
            puntos_b+=1
    
    if puntos_a > puntos_b:
        print(0, puntos_a)
    elif puntos_b > puntos_a:
        print(1, puntos_b)
    else:
        print(2, puntos_a)
        
    