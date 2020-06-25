import sys
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# termo panel 0.068
# https://www.academia.edu/31068192/Coeficiente_de_conductividad_t%C3%A9rmica_para_Vidrio_Volcanita_y_Termopanel
# cilicona 0.22 
# 0,18 W/Km
# https://tecnologiadelosplasticos.blogspot.com/2011/06/propiedades-termicas.html
# http://ejemplosmaterialesconstruccion.blogspot.com/2014/07/valor-de-la-conductividad-termica-del.html
#espesores



"""
calor_vidrio = calor_por_conduccion(A, K_vidrio,e_vidrio, dif_T)
calor_con_policarbonato = calor_por_conduccion_2(A, K_vidrio, e_vidrio, K_policarbonato, e_policarbonato, dif_T)
print(calor_vidrio, calor_con_policarbonato)
eficiencia_energetica = (calor_con_policarbonato/calor_vidrio)*100
print("con el policarbonato obtenemos una eficiencia enegetica del", calor_vidrio,"%")
"""

eficiencia_chimenea = 0.7 
potencia = 22000 #wats
T_julio_31=[8,8,8,8,8,8,7,6,6,7,8,7,7,8,7,7,7,7,8,7,7,6,7,7,7,7,7,8,7,8,7]

A = 1
K_vidrio = 0.96
K_policarbonato = 0.19
e_vidrio = 0.004
e_policarbonato = 0.004
dif_T = 8
k_termo = 0.068
e_termo = 0.011


def calor_por_conduccion(A, K, e, dif_T):
    return (K*A)*(dif_T/e)


def calor_por_conduccion_2(A, K1, e1, K2, e2, dif_T):
    return (A*dif_T)/(e1/K1 + e2/K2)

for 

warm = calor_por_conduccion_2(A, K_vidrio, e_vidrio, K_policarbonato, e_policarbonato, dif_T)
vidrio = round(calor_por_conduccion(A, K_vidrio,e_vidrio, dif_T))
termo = round(calor_por_conduccion(A, k_termo, e_termo, dif_T))
acrilico = round(calor_por_conduccion(A, 0.23, e_vidrio, dif_T))


plt.bar(["Vidrio de 4mm","Warm Glass", "Acrílico","Termopanel"], [vidrio, warm, acrilico,termo])
plt.title("Pérdida Energética por Material")
plt.ylabel("[Watts]")
print(vidrio, warm)

plt.show()