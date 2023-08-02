import numpy as np
import matplotlib.pyplot as plt
import time
from colour import Color

t0 = 0
tf = 100
dt = 0.25
t = t0

nbv = 30

def rainbow_gradient(num_colors):
    colors = []
    base_color = Color("violet")
    gradient = list(base_color.range_to(Color("red"), num_colors))
    for color in gradient:
        hex_code = color.hex_l
        colors.append(hex_code)
    return colors
colors = rainbow_gradient(nbv)

U = 1.25 # vitesse m.s-¹
Wm = 0.3 # distance minimale entre la voiture et celle qui la précède m
Ws = 0.9 # m

def phi(ww): # prend en entrée la distance entre les deux véhicules
    PHI = (U*(1 - np.exp(- (ww-Wm)/Ws)))
    return (ww >= Wm)* PHI  # retourne la vitesse du véhicule

y = np.linspace(1, 1, nbv)
xxbase = np.linspace(0, 1, nbv)

def distances(fposition):
    # print('fposition', fposition)
    dist = np.diff(fposition)
    inter = fposition[0]+20-fposition[-1]
    newdist = np.insert(dist, len(dist), inter)
    return newdist

def position(fposition, newv):
    newp = fposition + newv * dt
    return newp

xxold = xxbase.copy()

while(t < tf):
    plt.figure(1, figsize=[11, 11])
    plt.clf()

    nb = 360
    r = np.linspace(1, 1, nb)
    theta = np.linspace(0, 2 * np.pi, nb)

    ax = plt.subplot(111, polar=True)

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.polar(theta, r, alpha=0)

    dst = distances(xxold)

    vt = phi(dst)
    xx = position(xxold, vt)

    plt.scatter(xx/10 * np.pi, y, c=colors)

    # plt.title("Modélisation de l'évolution de la distance entre les voitures (périodique)\n\nnombre de voiture : "+ str(nbv) +"\n\nau temps t = " + str(t) + 's\n')
    plt.grid(False)

    plt.draw()
    plt.savefig('test/polaired_nbv=30/frame_' + str(t)+'.png')
    plt.pause(0.1)
    t += dt

    xxold = xx.copy()