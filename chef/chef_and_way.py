#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 06:18:25 2020

@author: felipe
"""

N ,k = [int(i) for i in input().split()]
special = [int(i) for i in input().split() ]
resto = N%k
if resto!=0:
    product = resto
else:
    product = 1
for i in especial:
    product = product * (i*k+resto)
print(product)
        