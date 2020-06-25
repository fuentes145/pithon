from os import path
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import numpy as np

class MiVentana(QWidget):
    def __init__(self, tamano_planchas, piezas):
        super().__init__()
        self.tamano_planchas = tamano_planchas
        self.piezas = piezas
        self.P = 0
        self.setGeometry(200, 100, 900, 900)
        self.esquina_plancha_x = 100
        self.esquina_plancha_y = 100
        self.init_gui()

    def init_gui(self):
        self.poner_plancha()
        self.principal(self.piezas)


    def poner_plancha(self):
        self.nueva_plancha = [self.esquina_plancha_x, self.esquina_plancha_y, self.tamano_planchas[0], self.tamano_planchas[1] ]
        self.plancha = QLabel(self)
        self.current_sprite = QPixmap(path.join('sprites', 'rectangulo1.jpg'))
        self.plancha.setPixmap(self.current_sprite)
        self.plancha.setGeometry(self.nueva_plancha[0]-4, self.nueva_plancha[1]-4, self.nueva_plancha[2]+8, self.nueva_plancha[3]+8)
        self.plancha.setScaledContents(True)

    def siguiente_plancha(self):
        if self.P != 4:
            self.esquina_plancha_x += 200
        else:
            self.esquina_plancha_y += 300
            self.esquina_plancha_x = 100
        self.poner_plancha()

    def principal(self, piezas):
        #margen = 0.3
        
        piezas_por_plancha = []
        planchas = [self.tamano_planchas]
        piezas_colocadas = []
        pedasos_perdidos = []
        while True:
            for pieza in piezas:
                for plancha in planchas:
                    if pieza[0] <= plancha[0] and  pieza[1] <= plancha[1]:

                        piezas_colocadas.append(pieza)
                        planchas.remove(plancha)
                        
                        #los primeros 2 valores de plancha son sus dimenciones y las segundas 2 son donde esta su esquina izquierda
                        plancha_1 = [plancha[0] - pieza[0], plancha[1], plancha[2]+pieza[0], plancha[3]]
                        planchas.append(plancha_1)

                        plancha_2 = [pieza[0], plancha[1] - pieza[1], plancha[2], plancha[3]+pieza[1] ]
                        planchas.append(plancha_2)

                        self.poner_pieza(plancha[2],plancha[3],pieza[0], pieza[1])
                        break

                    elif pieza[0] <= plancha[1] and  pieza[1] <= plancha[0]:
                        piezas_colocadas.append(pieza)
                        planchas.remove(plancha)

                        plancha_1 = [plancha[0] - pieza[1], plancha[1], plancha[2]+pieza[1], plancha[3]]
                        planchas.append(plancha_1)

                        plancha_2 = [pieza[1], plancha[1] - pieza[0],plancha[2], plancha[3]+pieza[0]]
                        planchas.append(plancha_2)

                        self.poner_pieza(plancha[2],plancha[3],pieza[1], pieza[0])
                        break
                        
            self.P += 1
            piezas_por_plancha.extend([self.P , piezas_colocadas])
            for i in piezas_colocadas:
                if i in piezas:
                    piezas.remove(i)      
            piezas_colocadas = []
            
            pedasos_perdidos.extend(planchas)
            planchas = [self.tamano_planchas]
            
            # no estoy haciendo nada con los pedasos_perdidos
            if len(piezas) == 0:
                print(self.P, piezas_por_plancha)
                return 
                
            else:
                self.siguiente_plancha()

    def poner_pieza(self,p1,p2,x,y):
        self.corte = QLabel(self)
        self.current_sprite = QPixmap(path.join('sprites', 'cuadrado.png'))
        self.corte.setPixmap(self.current_sprite)
        self.corte.setGeometry(p1+self.esquina_plancha_x, p2+self.esquina_plancha_y, x, y)
        self.corte.setScaledContents(True)




tamaño_planchas = input(print("de que tamaño son tus planchas"))
tamaño_planchas = tamaño_planchas.split("x")
tamaño_planchas.append(0)
tamaño_planchas.append(0)
tamaño_planchas[0] = int(tamaño_planchas[0])
tamaño_planchas[1] = int(tamaño_planchas[1])
piezas = []

 #ojo con plancha[2 y 3] nose si estan bien definidos

print("cuando termines solo escrive listo")
while True:
    a = input(print("cuantas piezas"))
    if a == "listo":
        break
    b = input(print("de que porte"))
    
    b = b.split("x")
    b[0] = int(b[0])
    b[1] = int(b[1])
    for i in range(0, int(a)):
        piezas.append(b)




# tamaño_planchas = [122, 244,0,0]
# tamaño_planchas = [100, 200,0,0]
# piezas = [[30,60], [70,70], [40,40], [40,40],[30,60], [70,70], [40,40], [40,40]]
piezas = np.sort(piezas, axis=0)
piezas = np.flip(piezas, axis=None)

piezas = piezas.tolist()

aui = [i[0]+i[1] for i in piezas ]


#la funcio no acepta piezas de tamaño , mayor a tamaño_planchas













app = QApplication([])
ventana = MiVentana(tamaño_planchas, piezas)
ventana.show()
sys.exit(app.exec_())