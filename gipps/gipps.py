import numpy as np
import matplotlib.pyplot as plt
import time
from colour import Color

# ===========
t0 = 0
tf = 30
dt = 1
t = t0
# ===========
nbv = 2

"""# ===========       VARIABBLES
Xn(t) # position au temps t
Vn(t) # vitesse au temps t
An(t+Tr) # accel au temps t + Tr
ln # ?
k # ?
m # ?
"""

# ===========       CONSTANTES
An = 1.7 # accel max                                          sampled from a normal distribution. N(1.7,0.3²) m/s²
Bn = -2 * An # frein max                                          equated to - 2An
Sn =  6.5 # taille de la voiture plus marge                    sampled from a normal distribution. N(6.5,0.3²) m
Vd = 20.0 # vitesse désirée                                    sampled from a normal distribution. N(20.0,3.2²) m/sec
# X*n # position fin de freinage (calculable)
Tr = 2/3 + (2/3)/2 # temps de réaction + sûreté                 (= tau + θ = 2/3 + tau/2)
# B supposé égal à Bn-1 (si pas égal alors amplifications ??)


def rainbow_gradient(num_colors):
    colors = []
    base_color = Color("violet")
    gradient = list(base_color.range_to(Color("red"), num_colors))
    for color in gradient:
        hex_code = color.hex_l
        colors.append(hex_code)
    return colors
colors = rainbow_gradient(nbv)

def px(xx):             # Avance au cours du temps
    xx += 1
    return xx

def vitesseatt(t, yy):       # Vitesse qu'il peut réellement atteindre d'un point de vue dynamique



    Vnt = yy[-1]
    
    value = Vnt + 2.5 * An * Tr * ( 1 - (Vnt/Vd) ) * np.sqrt( ( 0.025 + (Vnt/Vd) ))
    print('value: ', value)

    yy[0] = value
    newyy = yy
    print('newyy: ', newyy)
    return newyy
    

def vitesseadop(t, yy):      # Vitesse qu'il est possible d'adopter en connaissant les contraintes de sécurité liées à la présence du véhicule leader
    t = t + Tr
    pass

def vitessereelle(t, yyold):    # Vitesse du véhicule
    print(len(yy))
    t = t + Tr
    if (t>= 0) and (t<=10):
        yy[-1] = 0              # Arrêt du leader
    elif (t>= 15) and (t<=20):

    else:
        yy[-1] = Vd           # Leader avance normalement


# a = np.where(t <= 10, (Umax - Umin) / 10, - (Umax - Umin) / 10)
# vt = np.where(t <= 10, Umin + a * t, Umax + 2 * a * (t - 10))




    vatt = vitesseatt(t, yyold)
    vadop = vitesseadop(t, yyold)
    # return min(vatt, vadop)
    return vatt


xxbase = np.linspace(-nbv, -1, nbv)
yybase = np.linspace(0, 0, nbv)

xxold = xxbase.copy()
yyold = yybase.copy()

while(t<tf):
    plt.figure(1,figsize=[16,9])
    plt.clf()
    plt.xlim([-1,31])
    plt.ylim([-0.5, Vd+1])
    
    
    xx = px(xxold)
    print('xx: ', len(xx))

    yy = vitessereelle(t, yyold)
    print('yyold: ', len(yyold))
    print('yy: ', len(yy))

    
    plt.scatter(xx, yy, c=colors)


    plt.plot([0,30],[Vd, Vd], color='k', linestyle='-', linewidth=1)
    plt.xlabel('temps en s')
    plt.ylabel('vitesse en m.s-¹')
    plt.title('Vitesse maximale désirée\nvitesse du leader : ' + str(Vd) + 'm.s-¹\ndistance minimale entre deux voitures : ' + str('') + 'm\n\nTemps : ' + str(t))
    plt.draw()
    # plt.savefig(str(t)+'.png')
    plt.pause(1)
    t += dt
    xxold = xx.copy()
    yyold = yy.copy()