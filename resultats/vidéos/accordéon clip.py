import numpy as np
import matplotlib.pyplot as plt
import time
from colour import Color

t0 = -10
tf = 100
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

def status(distances):
    num_colors = len(distances)
    colors = []
    base_color = Color("green")
    target_color = Color("red")
    luminance_start = base_color.get_luminance()
    luminance_end = target_color.get_luminance()
    for i in range(num_colors):
        moydist = distances[i]
        t = i / (num_colors - 1)
        adjusted_luminance = luminance_start + (luminance_end - luminance_start) * (1 - t) * (moydist - 1) / 18
        color = Color(rgb=(base_color.rgb[0] * (1 - t) + target_color.rgb[0] * t,
                           base_color.rgb[1] * (1 - t) + target_color.rgb[1] * t,
                           base_color.rgb[2] * (1 - t) + target_color.rgb[2] * t))
        color.set_luminance(adjusted_luminance)
        hex_code = color.hex_l
        colors.append(hex_code)
    return colors


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
while t<0:
    plt.figure(1,figsize=[16,9])
    plt.clf()

    plt.draw()
    plt.pause(1 )
    print(t)
    t += 2*dt
    
while(t<tf):
    plt.figure(1,figsize=[16,9])
    plt.clf()

    nb = 360

    r=np.linspace(1,1,nb)
    theta=np.linspace(0,2*np.pi,nb)

    # plt.polar(theta, r)
    # plt.scatter(1*np.pi, 0.5)

    dst = distances(xxold)
    statusc = status(dst)
    print(statusc)

    vt = phi(dst)
    # print('vitesses : ', vt)

    xx = position(xxold, vt)
    # print('position : ', xx)

    plt.scatter(xx/10*np.pi, y, c=colors)

    for i in range(len(xx)):
        plt.plot(xx[i]/10*np.pi, y[i], color=statusc[i])

    plt.title('Vitesse maximale : ' + str(U) + 'm.s-¹\ndistance minimale entre deux voitures : ' + str(Wm) + 'm\nnombre de voitures : ' + str(nbv))
    plt.draw()
    plt.pause(0.00001)
    t += dt
    xxold = xx.copy()