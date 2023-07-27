import numpy as np
import matplotlib.pyplot as plt
import time
from colour import Color

t0 = 0
tf = 20
# tf=3
dt = 0.5
t = t0


U = 1.25 # vitesse m.s-¹
Wm = 0.3 # distance minimale entre la voiture et celle qui la précède m
Ws = 0.9 # m

def rainbow_gradient(num_colors):
    colors = []
    base_color = Color("violet")
    gradient = list(base_color.range_to(Color("red"), num_colors))
    for color in gradient:
        hex_code = color.hex_l
        colors.append(hex_code)
    return colors
colors = rainbow_gradient(11)


def phi(ww): # prend en entrée la distance entre les deux véhicules
    PHI = (U*(1 - np.exp(- (ww-Wm)/Ws)))
    return (ww >= Wm)* PHI  # retourne la vitesse du véhicule

y = np.linspace(0, 0, 11)
xxbase = np.linspace(0, 1, 11)

def position(fposition, newv):
    newp = fposition + newv * dt
    return newp

def vitesses(fposition):
    dist = np.diff(fposition)
    vitesses = phi(dist)
    newv = np.insert(vitesses, 10, 1.25)
    return newv

xxold = xxbase.copy()

while(t<tf):
    plt.figure(1,figsize=[16,9])
    plt.clf()
    plt.xlim([-1,20])
    plt.ylim([-0.5, 1.5])
    vt = vitesses(xxold)
    xx = position(xxold, vt)
    # color = ['#ff0000', '#ff5300', '#ffa500', '#ffd200', '#ffff00', '#80c000', '#008000', '#004080', '#0000ff', '#2600c1', '#4b0082']
    plt.scatter(xx, vt)
    plt.scatter(xx, y, c=colors)
    plt.plot([0,20],[1.25, 1.25], color='k', linestyle='-', linewidth=1)
    plt.xlabel('distance w  en m')
    plt.ylabel('vitesse en m.s-¹')
    plt.title('Evolution de la vitesse des voitures\nvitesse du leader : ' + str(U) + 'm.s-¹\ndistance minimale entre deux voitures : ' + str(Wm) + 'm')
    plt.draw()
    # plt.savefig(str(t)+'.png')
    plt.pause(0.2)
    t += dt
    xxold = xx.copy()
