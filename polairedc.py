import numpy as np
import matplotlib.pyplot as plt
import time
from colour import Color
import random

t0 = 0
tf = 200
dt = 0.5
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

arr = random.randint(0,nbv-1)

def distances(fposition):
    # print('fposition', fposition)
    dist = np.diff(fposition)
    inter = fposition[0]+20-fposition[-1]
    if (t>= 50) and (t<=60) :
        dist[arr] = 0
    newdist = np.insert(dist, len(dist), inter)
    return newdist

def position(fposition, newv):
    newp = fposition + newv * dt
    return newp

xxold = xxbase.copy()

while(t < tf):
    plt.figure(1, figsize=[16, 9])
    plt.clf()

    nb = 360
    r = np.linspace(1, 1, nb)
    theta = np.linspace(0, 2 * np.pi, nb)

    plt.polar(theta, r, alpha=0)

    dst = distances(xxold)
    vt = phi(dst)
    xx = position(xxold, vt)

    plt.scatter(xx/10 * np.pi, y, c=colors)

    plt.title('Vitesse maximale : ' + str(U) + ' m/s\ndistance minimale entre deux voitures : ' + str(Wm) + ' m\nnombre de voitures : ' + str(nbv) + '\n temps : ' + str(t)+ '\n la voiture qui va freiner est la ' + str(arr) + ' ème (à 50s)')
    plt.draw()
    plt.pause(0.00001)
    t += dt
    xxold = xx.copy()