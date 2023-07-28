import numpy as np
import matplotlib.pyplot as plt
import time

t0 = 0
tf = 20
# tf=3
dt = 1
t = t0


U = 1.25 # vitesse m.s-¹
Wm = 0.3 # distance minimale entre la voiture et celle qui la précède m
Ws = 0.9 # m

ww = np.linspace(0, 10, 200)

def phi(ww): # prend en entrée la distance entre les deux véhicules
    PHI = (U*(1 - np.exp(- (ww-Wm)/Ws)))
    return (ww >= Wm)* PHI  # retourne la vitesse du véhicule

y = np.linspace(0, 0, 11)
xxbase = np.linspace(0, 1, 11)

def position(fposition):
    dist = np.diff(fposition)
    vitesses = phi(dist)
    newv = np.insert(vitesses, 10, 1.25)
    newp = fposition + newv * dt
    return newp

xxold = xxbase.copy()

while(t<=tf):
    plt.figure(1,figsize=[12,5])
    # plt.clf()
    plt.xlim([-1,30])
    plt.ylim([-1, 21])
    xx = position(xxold)
    color = ['#ff0000', '#ff5300', '#ffa500', '#ffd200', '#ffff00', '#80c000', '#008000', '#004080', '#0000ff', '#2600c1', '#4b0082']

    # plt.plot([0,20],[t, t], color='k', linestyle='-', linewidth=1)

    plt.scatter(xx, np.linspace(t, t, 11), c=color)

    
    plt.xlabel('distance w  en m', )
    plt.ylabel('temps en s')
    # plt.title("Modélisation de l'évolution de la distance entre les voitures\n\nau temps t = " + str(t) + 's')


    plt.draw()
    if t == 20:
        plt.savefig('test/model/frame_' + str(t)+'.png')
    plt.pause(0.2)    
    t += dt
    xxold = xx.copy()