import numpy as np
import matplotlib.pyplot as plt
import time

t0 = 0
tf = 100
dt = 0.5
t = t0

U = 1.25 # vitesse m.s-¹
Wm = 0.3 # distance minimale entre la voiture et celle qui la précède m
Ws = 0.9 # m

def phi(ww): # prend en entrée la distance entre les deux véhicules
    PHI = (U*(1 - np.exp(- (ww-Wm)/Ws)))
    return (ww >= Wm)* PHI  # retourne la vitesse du véhicule

y = np.linspace(1, 1, 11)
xxbase = np.linspace(0, 1, 11)

def position(fposition, newv):
    newp = fposition + newv * dt
    return newp

def vitesses(fposition):
    print('fposition', fposition)
    dist = np.diff(fposition)
    print('distance : ', dist)
    vitesses = phi(dist)
    newv = np.insert(vitesses, 10, 1.25)
    return newv

xxold = xxbase.copy()

while(t<tf):
    plt.figure(1,figsize=[16,9])
    plt.clf()

    nb = 360

    r=np.linspace(1,1,nb)
    theta=np.linspace(0,2*np.pi,nb)

    plt.polar(theta, r)
    # plt.scatter(1*np.pi, 0.5)

    vt = vitesses(xxold)
    print('vitesses : ', vt)

    xx = position(xxold, vt)
    print('position : ', xx)

    color = ['#ff0000', '#ff5300', '#ffa500', '#ffd200', '#ffff00', '#80c000', '#008000', '#004080', '#0000ff', '#2600c1', '#4b0082']
    plt.scatter(xx/10*np.pi, y, c=color)

    plt.draw()
    plt.pause(0.00001)
    t += dt
    xxold = xx.copy()