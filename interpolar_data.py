M = 1000000
import sys
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

costo_warm_glass_m_2 = [9000]  # materias primas, sin transporte, sin nada

costo_con_manofactura = [13000,10000,8000]

costo_vieja = 65000

precio_venta = [18000, 16990, 15000]

unidades_ferreterias = [10,20,35]

n_ferreterias = [25,100,1000]

inversion_inicial = 8000000
p= [0,0,0]
for i in range (3):
    if i == 0:
        p[i] = (unidades_ferreterias[i] * n_ferreterias[i] * (precio_venta[i]-costo_con_manofactura[i]) - inversion_inicial)
    else:
        p[i] = unidades_ferreterias[i] * n_ferreterias[i] * (precio_venta[i]-costo_con_manofactura[i]) 

p.insert(0,0)
p.pop()

e = [-5*M,-1.5*M,10*M]
print(p)
print(e)
def Pe(p, e):
    h = []
    for i in range(len(p)-1):
        h.append("")
        h[i] = [p[i], e[i] , p[i+1]]

    return h
#x va aser lista de listas con los numeros [[xi, ()/2, xi+1], []]. y lo mismo  


def interpolar (x, y):
  A = []
  for i in range(len(x)):
    if i == len(x)-1:
        break

    xi = np.array([ x[i], (x[i] + x[i+1])/2, x[i+1] ])
    V = np.vander(xi)
    yi = np.transpose(np.array(y[i]))
    coefs = np.linalg.solve(V,yi)

    coefs = coefs.tolist()
    A.append(coefs)
 
  return A

X = [0,3,12]

A = interpolar(X, Pe(p, e))
 
c = 0
ja = 0
for i in range(len(X)):
    plt.plot(X[i], p[i], 'go')
    if i == len(X)-1:
        break
    x = np.linspace(X[i], X[i+1], 20)
    plt.plot(x, np.polyval(A[c], x), color = "C0")
    c+=1

plt.xlabel('meses')
plt.ylabel('pesos')

plt.show()
