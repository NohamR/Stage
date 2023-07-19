import numpy as np
import matplotlib.pyplot as plt

# ===========       CONSTANTES
An = 1.7 # accel max                                          sampled from a normal distribution. N(1.7,0.3²) m/s²
Bn = -2 * An # frein max                                          equated to - 2An
Sn =  6.5 # taille de la voiture plus marge                    sampled from a normal distribution. N(6.5,0.3²) m
Vd = 20.0 # vitesse désirée                                    sampled from a normal distribution. N(20.0,3.2²) m/sec
# X*n # position fin de freinage (calculable)
Tr = 2/3 + (2/3)/2 # temps de réaction + sûreté                 (= tau + θ = 2/3 + tau/2)
# B supposé égal à Bn-1 (si pas égal alors amplifications ??)


vv = np.linspace(0, 100, 200)

def vitesseatt(vv):       # Vitesse qu'il peut réellement atteindre d'un point de vue dynamique
    value = vv + 2.5 * An * Tr * ( 1 - (vv/Vd) ) * np.sqrt( ( 0.025 + (vv/Vd) ))
    return value
    

def vitesseadop(vv):      # Vitesse qu'il est possible d'adopter en connaissant les contraintes de sécurité liées à la présence du véhicule leader
    value = 1
    return value

def vitessereelle(vv):      # Vitesse maximale désirée
    vatt = vitesseatt(vv)
    vadop = vitesseadop(vv)
    return min(vatt, vadop)

plt.figure(figsize=[16,9])


plt.plot(vv, vitesseatt(vv), '-', color='red', label='No mask')
# plt.plot(vv, vitesseadop(vv), '-', color='green', label='No mask')


plt.legend()
plt.title('Variation de la vitesse de la voiture suivant en fonction de la voiture leader')
plt.xlabel('vitesse de la voiture leader en m.s-¹')
plt.ylabel('vitesse de la voiture qui suit en m.s-¹')
plt.savefig('gipps/graph.png')
plt.draw()  
plt.pause(4)