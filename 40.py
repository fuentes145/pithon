import sympy as sp
import re

a = open("2T_part1.txt", "r")
f = re.split("\t|\n",a.read())

#lo primero q se le entrega amap es una funcion q puede ser una lambda
f = list(filter(lambda x: x!="" ,f))
f = list(map(lambda primo:int(primo),f))
f = f[0:72382]

import itertools
c = 0
max = 1000000
fp = []
def max_prime_sum(max):
    cont = 0
    b = max
    while True:
        if sp.isprime(b):

            for j in range(len(list(itertools.combinations(f, cont)))):
                c = sum(list(itertools.combinations(f, cont))[j])


                if c == b:
                    return b
                c = 0
            cont += 1

        b-=1
        


print(max_prime_sum(max))