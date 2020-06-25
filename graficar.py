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


hidrdff
"""
trmopanel de 40 a 80 lucas
policarbonato de 5930
acrilico 
"""

warm = 10000
vidrio = 1000
termo = 120000
acrilico = 15000
Pwarm = 5930


plt.bar(["Policarbonato 4mm", "Acrilico 4mm", "Termopanel"], [warm, acrilico,termo])
plt.title("Precio por m²")
plt.ylabel("pesos $")

plt.show()