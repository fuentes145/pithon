
import math
import numpy as np 
from matplotlib import pyplot as plt 

def A(h,b):
    return (h**2)/2 + b*h

def fx2(h, b=8):
    return  (10**2)/(2*9.81*A(h,b)**2) +h

def fx1(h, b=5):
    return  (10**2)/(2*9.81*A(h,b)**2) +h

print(fx2(0.9)+0.24)


X = np.linspace(0.3,1.8,50)
Y2 = list(map(fx2, X))
plt.plot(Y2,X, label="2")
Y1 = list(map(fx1, X))
plt.plot(Y1,X, label="1")
plt.plot([1.16849]*50,X)
plt.legend()
plt.show()


"""

n = 79
a = 8
b = 0


if fx(a)<0 and fx(b)>0:
    print('todo bien')
else:
    print('no existe solucion unica')
    print(fx(a), fx(b))

for i in range(n):
    c = (a+b)/2
    if fx(c) < 0:
        a=c
    elif fx(c) > 0:
        b=c
    else:
        print('se encontro la solucion')
        break
print(c)




"""