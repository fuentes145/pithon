#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 06:32:50 2020

@author: felipe
"""

T = int(input())

for _ in range(T):
    import itertools
    
    N = int(input())
    A = [int(i) for i in input().split()]
    
    def posicion(p,n):
        if p==1:
            puntos = option[-1] * n
            option.append(n)
        elif p==0:
            puntos = option[0] * n
            option.insert(0,n)
        return puntos
    
    
    total = 0
        
    for binario in itertools.product([0,1], repeat=N):
        option = [A[0]]
        points = 0
        for i in range(1, N+1):
            points += posicion(binario[i-1], A[i])
        total += points
       
        
    print(total)
        
        