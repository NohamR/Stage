import numpy as np
import matplotlib.pyplot as plt
import time
from colour import Color
import imagesV1 as images
import imagesV2 as images2

fps = 2

# ===========
t0 = 0
tf = 40
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
Vmin = 1
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

def px(tt):             # Avance au cours du temps
    tt += 1/fps
    return tt

def vitesseatt(vtold):       # Vitesse qu'il peut réellement atteindre d'un point de vue dynamique
    value = vtold + 2.5 * An * Tr * ( 1 - (vtold/Vd) ) * np.sqrt( ( 0.025 + (vtold/Vd) ))
    return value
    

def vitesseadop(vtold, xxpold):      # Vitesse qu'il est possible d'adopter en connaissant les contraintes de sécurité liées à la présence du véhicule leader
    dst = np.diff(xxpold)
    value = Bn * Tr + np.sqrt( ((Bn)**2) * ((Tr)**2) - Bn * ( 2 * dst) - vtold[0] * Tr - ( (xxold[-1])**2 / Bn )  )
    newvalue = np.insert(value, 1, vtold[1])
    print('newvalue: ', newvalue)
    return newvalue

def vitessereelle(t, vtold, xxpold):    # Vitesse du véhicule
    # t+=t
    if t==0:
        vtold[-1] = 0.1
    elif (t> 0) and (t<=10):     # Accélération du leader
        a = (Vd - Vmin) / 10
        vtleader = Vmin + a * t
        vtold[-1] = vtleader
    elif (t>= 16) and (t<=20):  # Leader freine
        a = - (Vd - Vmin) / 10
        vtleader = Vd + 2 * a * (t - 16)
        vtold[-1] = vtleader
    elif (t> 20) and (t<=30):  # Accélération du leader
        a = (Vd - Vmin) / 10
        vtleader = Vmin + a * (t-20)
        vtold[-1] = vtleader
    else:                   # Leader avance normalement
        vtold[-1] = Vd
    
    vatt = vitesseatt(vtold)
    vadop = vitesseadop(vtold, xxpold)
    minimum = np.minimum(vatt, vadop)
    print('minimum: ', minimum)
    return minimum



def position(fposition, newv):
    newp = fposition + newv * dt
    return newp

xxbase = np.linspace(-nbv, 1, nbv)
xxpbase = np.linspace(0, 1, nbv)
yybase = np.linspace(0, 1, nbv)

xxold = xxbase.copy()
xxpold = xxpbase.copy()
vtold = yybase.copy()

while(t<=tf):
    plt.figure(1,figsize=[16,9])
    # plt.clf()
    plt.xlim([-1,41])
    plt.ylim([-0.5, Vd+1])
    
    xx = px(xxold)

    vt = vitessereelle(t, vtold, xxpold)

    xxp = position(xxpold, vt)

    plt.scatter(xx, vt, c=colors)

    plt.plot([0,40],[Vd, Vd], color='k', linestyle='-', linewidth=1)
    plt.xlabel('temps en s', fontsize = 16)
    plt.ylabel('vitesse en m.s-¹', fontsize = 16)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    # plt.title('Vitesse maximale désirée\nvitesse du leader : ' + str(Vd) + 'm.s-¹\ndistance entre deux voitures : ' + str(np.diff(xxpold)) + 'm\n\nTemps : ' + str(t))
    plt.draw()
    if t == tf:
        plt.savefig('gipps V2 (modélisation)/V1.png')
    plt.pause(0.00001)
    t += dt/fps
    xxold = xx.copy()
    xxpold = xxp.copy()
    vtold = vt.copy()

# images.merge()
# images2.merge(fps)