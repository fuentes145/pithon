import re

a = open("2T_part1.txt", "r")
f = re.split("\t|\n",a.read())

#lo primero q se le entrega amap es una funcion q puede ser una lambda
f = list(filter(lambda x: x!="" ,f))
f = list(map(lambda primo:int(primo),f))




b=0
c=0
for i in f:
        if c <1000000:
            c += i
            if f.count(c) == 1:
                b = c
        else:
            break

print(b)






